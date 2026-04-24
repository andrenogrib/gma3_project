# gma3_project

Pacote de conhecimento e pesquisa tecnica para grandMA3, com foco em uso por IA, RAG, consulta humana e triagem de manutencao.

Este repositorio versiona os scripts, prompts, indices e notas produzidas no projeto. Os PDFs, ZIPs, DOCX, HTMLs espelhados e textos integrais extraidos de manuais de terceiros ficam locais por padrao, porque sao grandes e podem ter restricoes de redistribuicao.

## Conteudo versionado

- `knowledge/README.md`: visao geral do pacote de conhecimento grandMA3.
- `knowledge/tools/build_gma3_knowledge.py`: script para gerar Markdown e manifestos a partir dos PDFs locais.
- `knowledge/manifest.json`: auditoria da conversao local dos manuais.
- `knowledge/markdown/index.md`: indice dos documentos convertidos localmente.
- `knowledge/agent/`: prompt e instrucoes para montar um agente grandMA3.
- `knowledge/grandma3_maintenance_sources/README.md`: resumo da pesquisa de manutencao e pecas.
- `knowledge/grandma3_maintenance_sources/parts_index.csv`: indice de pecas encontradas em catalogos publicos.
- `knowledge/grandma3_maintenance_sources/manifest.csv`: manifesto dos arquivos locais baixados.
- `knowledge/grandma3_maintenance_sources/diagnostico_gma3_light_touch_fantasma.md`: checklist para touch fantasma em grandMA3 light.

## Artefatos locais ignorados

Estes caminhos ficam fora do Git por padrao:

- PDFs originais em `knowledge/sources/`.
- Markdown completo e chunks RAG gerados a partir dos manuais.
- Snapshots HTML, ZIPs e DOCX baixados de fontes oficiais/terceiros.
- Qualquer `*.pdf`, `*.zip` e `*.docx`.

Para publicar esses artefatos, prefira um reposititorio privado ou Git LFS, e confirme antes os termos/licencas das fontes.

## Regenerar base de conhecimento

Com os PDFs locais disponiveis:

```powershell
python knowledge\tools\build_gma3_knowledge.py
```

O processo gera Markdown, manifesto e arquivos prontos para ingestao por IA/RAG dentro de `knowledge/`.

## Manutencao grandMA3

A pesquisa de manutencao esta resumida em `knowledge/grandma3_maintenance_sources/README.md`. Ate agora, nao foi encontrado um service manual publico completo da grandMA3 com esquemas, exploded views ou procedimentos oficiais de bancada.

O material publico util inclui:

- manuais e quick manuals da MA Lighting;
- boletins tecnicos;
- paginas de help e seguranca;
- checklist alemao de manutencao da Lightpower;
- catalogos de pecas com codigos e compatibilidade parcial;
- informacoes de garantia/RMA da ACT Entertainment.

## Aviso

Este projeto organiza conhecimento tecnico e metadados de fontes publicas/locais. Ele nao substitui documentacao oficial, treinamento MA Lighting ou servico tecnico qualificado, especialmente para reparos internos de consoles.
