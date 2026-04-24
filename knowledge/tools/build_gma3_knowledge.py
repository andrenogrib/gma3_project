from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

import pypdfium2 as pdfium


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = ROOT / "sources" / "pdfs"
DEFAULT_MARKDOWN_DIR = ROOT / "markdown" / "documents"
DEFAULT_INDEX_PATH = ROOT / "markdown" / "index.md"
DEFAULT_COMBINED_PATH = ROOT / "markdown" / "combined.md"
DEFAULT_MANIFEST_PATH = ROOT / "manifest.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def title_from_stem(stem: str) -> str:
    title = re.sub(r"^\d{4}_\d{2}_\d{2}_", "", stem)
    title = title.replace("_", " ")
    title = re.sub(r"\s+", " ", title).strip()
    return title or stem


def normalize_page_text(text: str) -> str:
    text = repair_mojibake(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", line).rstrip() for line in text.splitlines()]
    compacted: list[str] = []
    blank_seen = False
    for line in lines:
        if not line.strip():
            if not blank_seen:
                compacted.append("")
            blank_seen = True
            continue
        compacted.append(line)
        blank_seen = False
    return "\n".join(compacted).strip()


def repair_mojibake(text: str) -> str:
    markers = ("Ã", "Â", "â€")
    if not any(marker in text for marker in markers):
        return text
    try:
        fixed = text.encode("cp1252").decode("utf-8")
    except UnicodeError:
        return text
    original_score = sum(text.count(marker) for marker in markers)
    fixed_score = sum(fixed.count(marker) for marker in markers)
    return fixed if fixed_score < original_score else text


def extract_pdf_text(pdf_path: Path) -> tuple[list[str], list[str]]:
    pages: list[str] = []
    errors: list[str] = []
    document = pdfium.PdfDocument(str(pdf_path))
    try:
        for page_index in range(len(document)):
            try:
                page = document[page_index]
                textpage = page.get_textpage()
                text = textpage.get_text_range()
                pages.append(normalize_page_text(text))
                try:
                    textpage.close()
                except Exception:
                    pass
                try:
                    page.close()
                except Exception:
                    pass
            except Exception as exc:
                pages.append("")
                errors.append(f"page {page_index + 1}: {exc}")
    finally:
        try:
            document.close()
        except Exception:
            pass
    return pages, errors


def build_markdown(pdf_path: Path, pages: list[str], generated_at: str) -> str:
    title = title_from_stem(pdf_path.stem)
    digest = sha256(pdf_path.read_bytes()).hexdigest()
    lines = [
        "---",
        f"title: {yaml_string(title)}",
        f'source_url: {yaml_string("local:" + pdf_path.as_posix())}',
        f"canonical_url: {yaml_string('')}",
        f"fetched_at_utc: {yaml_string(generated_at)}",
        f"last_updated_utc: {yaml_string('')}",
        f"source_file: {yaml_string(pdf_path.as_posix())}",
        f"source_sha256: {yaml_string(digest)}",
        f"page_count: {len(pages)}",
        'extraction_method: "pypdfium2-text-layer"',
        "---",
        "",
        f"# {title}",
        "",
        f"- Source PDF: `{pdf_path.name}`",
        f"- Pages: `{len(pages)}`",
        f"- Extraction: `pypdfium2-text-layer`",
        "",
    ]
    for index, page_text in enumerate(pages, start=1):
        lines.append(f"## Page {index}")
        lines.append("")
        if page_text:
            lines.append(page_text)
        else:
            lines.append("_No extractable text found on this page._")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_index(records: list[dict[str, object]], index_path: Path, generated_at: str) -> None:
    total_pages = sum(int(record["page_count"]) for record in records)
    total_chars = sum(int(record["text_chars"]) for record in records)
    lines = [
        "# grandMA3 Knowledge Base",
        "",
        f"- Generated at (UTC): `{generated_at}`",
        f"- Documents: `{len(records)}`",
        f"- PDF pages: `{total_pages}`",
        f"- Extracted text chars: `{total_chars}`",
        "",
        "## Documents",
        "",
    ]
    for record in records:
        title = str(record["title"])
        path = str(record["markdown_path"])
        pages = int(record["page_count"])
        chars = int(record["text_chars"])
        lines.append(f"- [{title}]({path}) - `{pages}` pages, `{chars}` chars")
    index_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_combined(records: list[dict[str, object]], combined_path: Path, generated_at: str) -> None:
    lines = [
        "# grandMA3 Combined Markdown",
        "",
        f"- Generated at (UTC): `{generated_at}`",
        f"- Documents: `{len(records)}`",
        "",
    ]
    for record in records:
        md_path = ROOT / "markdown" / str(record["markdown_path"])
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append(md_path.read_text(encoding="utf-8").strip())
        lines.append("")
    combined_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_knowledge(source_dir: Path, markdown_dir: Path, clean: bool) -> list[dict[str, object]]:
    if not source_dir.exists():
        raise SystemExit(f"Source directory not found: {source_dir}")

    if clean and markdown_dir.exists():
        shutil.rmtree(markdown_dir)
    markdown_dir.mkdir(parents=True, exist_ok=True)

    generated_at = utc_now()
    records: list[dict[str, object]] = []

    for pdf_path in sorted(source_dir.glob("*.pdf")):
        print(f"Extracting {pdf_path.name}", flush=True)
        pages, errors = extract_pdf_text(pdf_path)
        markdown = build_markdown(pdf_path, pages, generated_at)
        target_path = markdown_dir / f"{pdf_path.stem}.md"
        target_path.write_text(markdown, encoding="utf-8")

        text_chars = sum(len(page) for page in pages)
        record = {
            "title": title_from_stem(pdf_path.stem),
            "source_pdf": pdf_path.relative_to(ROOT).as_posix(),
            "markdown_path": target_path.relative_to(ROOT / "markdown").as_posix(),
            "page_count": len(pages),
            "text_chars": text_chars,
            "blank_pages": sum(1 for page in pages if not page.strip()),
            "errors": errors,
            "source_sha256": sha256(pdf_path.read_bytes()).hexdigest(),
            "status": "SUCCESS" if not errors else "PARTIAL_SUCCESS",
        }
        records.append(record)

    payload = {
        "generated_at_utc": generated_at,
        "source_dir": source_dir.resolve().as_posix(),
        "markdown_dir": markdown_dir.resolve().as_posix(),
        "document_count": len(records),
        "page_count": sum(int(record["page_count"]) for record in records),
        "text_chars": sum(int(record["text_chars"]) for record in records),
        "records": records,
    }
    DEFAULT_MANIFEST_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    DEFAULT_INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_index(records, DEFAULT_INDEX_PATH, generated_at)
    write_combined(records, DEFAULT_COMBINED_PATH, generated_at)
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the grandMA3 Markdown knowledge package.")
    parser.add_argument("--source-dir", default=str(DEFAULT_SOURCE_DIR))
    parser.add_argument("--markdown-dir", default=str(DEFAULT_MARKDOWN_DIR))
    parser.add_argument("--no-clean", action="store_true")
    args = parser.parse_args()

    records = build_knowledge(
        source_dir=Path(args.source_dir),
        markdown_dir=Path(args.markdown_dir),
        clean=not args.no_clean,
    )
    print(f"Done. Documents: {len(records)}", flush=True)


if __name__ == "__main__":
    main()
