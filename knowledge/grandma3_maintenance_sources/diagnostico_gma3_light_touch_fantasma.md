# Diagnostico: grandMA3 light com touch fantasma na tela inferior direita

Caso relatado: grandMA3 light com a tela menor abaixo da tela principal direita gerando cliques sozinha. Factory reset, fresh install da versao mais recente e limpeza externa nao resolveram.

## Leitura provavel

Depois de reset/fresh install/limpeza, a chance maior deixa de ser software e passa a ser hardware no caminho do touch:

1. Touch sensor/digitizer da tela de 14,9".
2. Cabo interno entre main/MM/MC board e controladora de touch.
3. Touch-controller board 14,9".
4. Contaminacao/umidade/pressao mecanica no vidro ou moldura.
5. Aterramento/ruido eletrico, menos provavel, mas facil de testar.

## Pecas que batem com a tela inferior de 14,9"

- `007-226`: MA Lighting GrandMA3 Touch-Sensor 14,9 Rev.B. Numeros `4022703`, `1500008012`. Compatibilidade listada: grandMA3 full-size, full-size CRV, light, light CRV. Substitui `4011546` Rev.A.
- `007-228`: MA Lighting GrandMA3 Touch-Controller Board 14,9. Numeros `4011547`, `1000202591`. Compatibilidade listada: grandMA3 full-size, full-size CRV, light, light CRV.
- `007-227`: Cabo I2C 8pin/10pin. Numeros `4022443`, `1000K02821`. Descrito como ligacao interna de MM/MC board para Touch-Controller 14,9"; indicado para cabo quebrado ou problema de contato.

Se a tela afetada for a principal de 15,6", a peca correspondente no catalogo e:

- `007-225`: Display/Touch-Sensor 15,6", listado para grandMA3 Full-Size e grandMA3 Light.

## Testes seguros antes de abrir

1. Ligar a mesa sem nada externo: sem USB, mouse, teclado, rede, DMX, MIDI, LTC, hub ou monitor externo.
2. Testar em outra tomada/circuito, de preferencia com aterramento real.
3. Deixar a mesa parada numa tela onde os cliques sejam visiveis e filmar 1 a 3 minutos mostrando a area que toca sozinha.
4. Ver se o problema aparece frio, depois de aquecer, ou ao pressionar levemente a moldura ao redor da tela.
5. Ver se ha pelicula, umidade, residuo de produto de limpeza ou borda fazendo pressao no vidro.
6. Criar uma janela de System Monitor e observar se ha mensagens relevantes enquanto os toques falsos acontecem.
7. Se o software permitir trabalhar com mouse/teclado externo temporariamente, evitar usar a regiao afetada ate resolver o hardware.

## Ordem de bancada recomendada

Com a mesa desligada, desconectada da rede eletrica e por tecnico qualificado:

1. Inspecao visual do conjunto de 14,9": vidro/touch, moldura, pontos de pressao, trinca, umidade, oxidação.
2. Reassentar cabos internos do touch/controller, olhando travas ZIF e marcas de dobra.
3. Conferir o cabo I2C 8pin/10pin `007-227`, especialmente porque o catalogo o descreve justamente como ligacao para Touch-Controller 14,9".
4. Se o problema mudar/sumir ao mexer/reassentar cabo, suspeitar cabo/conector.
5. Se continuar identico, trocar/testar a Touch-Controller Board 14,9 `007-228`.
6. Se continuar ou se houver dano fisico/umidade no touch, trocar o Touch-Sensor 14,9 Rev.B `007-226`.

## Observacao importante

A documentacao oficial de manutencao da MA avisa que reparo/servico interno deve ser feito exclusivamente por tecnico qualificado, pois partes energizadas podem ficar expostas ao abrir/remover tampas. Para uso pratico, trate este documento como guia de triagem e identificacao de pecas, nao como autorizacao para reparo interno energizado.
