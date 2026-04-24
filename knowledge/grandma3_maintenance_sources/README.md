# grandMA3 maintenance sources

Coleta feita em 2026-04-24 para concentrar material publico sobre manutencao, reparo, pecas e suporte de grandMA3. A busca incluiu fontes oficiais MA Lighting, ACT Entertainment e fontes alemas como Lightpower, Lichtboxx e Lightspares.

## Resultado curto

Nao encontrei um manual publico de servico de bancada para grandMA3 com esquemas, exploded views, procedimento de desmontagem, ajuste de motorfader ou troca de telas passo a passo.

O que existe publicamente e util:

- Manuais oficiais e quick manuals da MA Lighting.
- Boletins tecnicos oficiais sobre limpeza/desinfeccao e nivel de ruido.
- Paginas oficiais de help com manutencao operacional e avisos de seguranca.
- Checklist comercial de manutencao da Lightpower para grandMA3.
- Catalogos de pecas de reposicao com codigos, fabricantes e compatibilidade parcial.
- Paginas de garantia/RMA da ACT Entertainment para suporte na America do Norte.

## Estrutura local

- `official_ma/`: PDFs e ZIPs oficiais baixados da pagina de downloads da MA Lighting em alemao/ingles.
- `german_sources/`: paginas alemas/oficiais salvas como HTML, incluindo Lightpower e help MA.
- `act_sources/`: paginas salvas da ACT Entertainment.
- `parts_catalog/`: paginas de catalogo de pecas Lichtboxx/Lightspares.
- `extracted_zips/`: conteudo extraido dos ZIPs oficiais baixados.
- `manifest.csv`: lista de arquivos locais, tamanho e data de modificacao.
- `parts_index.csv`: indice resumido das paginas de pecas baixadas.
- `cad/`: deixado vazio; os CAD ZIPs oficiais exigem aceite/lightbox no site.

## Fontes principais

- MA Lighting downloads grandMA3: https://www.malighting.com/de/downloads/produkt/grandma3/
- MA Help, consoles maintenance: https://help.malighting.com/grandMA3/2.3/HTML/key_consoles_maintenance.html
- MA Help, processing unit maintenance: https://help.malighting.com/grandMA3/2.3/HTML/key_processing_maintenance.html
- Lightpower Wartung grandMA: https://www.lightpower.de/service/wartung-grandma/
- Lightpower Reparatur/Wartung: https://www.lightpower.de/service/reparatur-wartung/
- ACT Entertainment warranty/service: https://actentertainment.com/warranty/
- Lichtboxx search grandMA3: https://lichtboxx.com/catalogsearch/result/?q=grandma3
- Lightspares grandMA3 parts: https://lightspares.com/catalogsearch/result/?q=grandma3

## Achados de manutencao

A Lightpower publica a lista mais direta de manutencao para grandMA3. O pacote inclui:

- Inspecao visual interna/externa.
- Controle funcional.
- Verificacao de funcao e movimento de faders, encoders e botoes, exceto processing unit, replay unit e xPort Nodes.
- Limpeza com ar comprimido.
- Limpeza interna ampliada.
- Limpeza e selagem de contatos, exceto onPC command wing.
- Ensaio VDE conforme DIN/VDE 0701/0702 ou DGUV V3.
- Controle funcional final.
- Limpeza final.
- Pecas e tempo extra cobrados separadamente.

Codigos Lightpower de servico grandMA3:

- `600315`: Wartung grandMA3 full-size.
- `600316`: Wartung grandMA3 light.
- `600317`: Wartung grandMA3 compact/compact XT.
- `600322`: Wartung grandMA3 extension.
- `600318`: Wartung grandMA3 onPC command wing XT.
- `600319`: Wartung grandMA3 onPC command wing.
- `600323`: Wartung grandMA3 processing unit.
- `600321`: Wartung grandMA3 replay unit.
- `600320`: Wartung grandMA3 xPort Node.

## Pecas uteis encontradas

Tambem gerei `parts_index.csv` com as paginas baixadas. Alguns itens relevantes:

- `007-212`: Fader motorisiert 100 mm, fabricante `RFM1005K0A`.
- `007-213`: Fader motorisiert 60 mm, fabricante `RFM0605K0A`.
- `007-209`: Dual Encoder `4033176`, substitui `4011395` e `4032852`, tambem listado como `SE00BGE434`.
- `007-226`: Touch-Sensor 14,9 Rev.B, `4022703`, `1500008012`.
- `007-228`: Touch-Controller Board 14,9, `4011547`, `1000202591`.
- `007-225`: Display/Touch-Sensor 15,6.
- `007-244`: Display 3,9, `4022025`, para nodes e I/O nodes.
- `007-215`: Netzteil 500W, `4011398`, `1000202461`.
- `007-207`: Netzschalter beleuchtet, `4011400`, `SNLRA32H2D`.
- `007-208`: MA SSD M.2 128GB, `4030981`, substitui `4011556`, tambem listado como `1000202262`.
- `007-205`: SO-DIMM DDR4 RAM 1x8GB, `4011555`, `1000202512`.
- `007-214`: Luftfilter 254x51x12.
- `007-187`: Rotary encoder RGB LED 90, `1500RGBEH1`.
- `007-211`: Rotary encoder sem LED.
- `007-227`: Cabo I2C 8pin/10pin, `4022443`, `1000K02821`.
- `007-217`: Cabo ZIF 10pin/0.5mm 50mm, `4011878`, `1000K07101`.
- `007-218`: Cabo ZIF 10pin/1.0mm 100mm, `4022241`, `1000K07241`.

Uma pagina direta falhou por fechamento de conexao durante download:

- `https://lichtboxx.com/ma-lighting-grandma3-knopf-fuer-fader-leitfaehig`

O item aparece nas paginas de busca/catalogo como knob/fader conductive, SKU `007-206`.

## Limites e cuidado

As fontes oficiais indicam que reparos internos devem ser feitos por tecnicos qualificados/treinados. Para uma base de IA, eu trataria este pacote como conhecimento de triagem, manutencao preventiva, identificacao de pecas e encaminhamento de servico, nao como autorizacao para procedimento interno energizado.

Nao baixei imagens de sistema/software grandes da MA porque sao gigabytes e nao sao documentacao de manutencao. Tambem nao baixei os CAD ZIPs oficiais porque o site exige aceite/lightbox; a pagina oficial foi arquivada em `official_ma/ma_downloads_grandma3_de.html`.

## Proximo passo util

Para transformar isso em base pesquisavel para IA, falta converter os PDFs/HTMLs para texto limpo e criar chunks com metadados de fonte. Nesta maquina nao encontrei `pdftotext` nem bibliotecas Python de PDF instaladas, entao deixei os PDFs originais intactos.
