# grandMA3 Knowledge Package

Pacote local de conhecimento criado a partir de PDFs grandMA3.

## Conteudo gerado

- `sources/pdfs/`: copia local dos PDFs originais usados como fonte.
- `markdown/documents/`: 13 arquivos Markdown locais, um por PDF.
- `markdown/index.md`: indice humano dos documentos convertidos, versionado no Git.
- `markdown/combined.md`: todos os Markdown reunidos em um arquivo unico local.
- `manifest.json`: auditoria da conversao, com paginas, caracteres, hashes e status.
- `agent/pages.jsonl`: um registro por documento, bom para contexto amplo.
- `agent/chunks.jsonl`: 3.052 chunks locais prontos para embeddings, RAG e busca semantica.
- `agent/pages/`: copia limpa local dos Markdown usada pelo pacote de agente.
- `agent/AGENT_PROMPT.md`: prompt-base para criar um agente grandMA3.
- `tools/build_gma3_knowledge.py`: script para regerar o Markdown a partir dos PDFs.

## Como usar em qualquer AI

Para uma AI com upload de arquivos, comece com:

1. `markdown/combined.md`, se ela aceita um arquivo grande.
2. `markdown/documents/*.md`, se ela aceita varios arquivos.
3. `agent/chunks.jsonl`, se a plataforma usa base vetorial, embeddings ou RAG.

Para criar um agente, use `agent/AGENT_PROMPT.md` como instrucao do agente e coloque
o `agent/chunks.jsonl` local como base de conhecimento principal.

## Observacao importante

Isto nao "treina" o modelo no sentido de alterar pesos internos. O pacote deixa o
conteudo pronto para retrieval/RAG, agentes e uploads em ferramentas de AI. Na pratica,
e o formato mais portatil para dar conhecimento tecnico de grandMA3 a varias AIs.

A conversao principal usa a camada de texto dos PDFs (`pypdfium2-text-layer`).
Esse caminho foi escolhido porque o manual completo tem 2.198 paginas e o pipeline
completo de layout/OCR do Docling ficaria bem lento em CPU para esta base inteira.

## Regenerar

Com um ambiente Python que tenha `pypdfium2` instalado:

```powershell
python knowledge\tools\build_gma3_knowledge.py
```

Os arquivos `agent/chunks.jsonl`, `agent/pages.jsonl` e `agent/pages/` foram gerados
localmente a partir do Markdown extraido. Eles ficam fora do Git por padrao.

Neste repositorio, os PDFs originais e o texto integral extraido ficam ignorados por padrao
para evitar arquivos grandes e redistribuicao integral de manuais de terceiros.
