# Capítulo 02 — Condições

[← Capítulo anterior](01-fundamentos.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](03-lacos-e-logica.md)

## O que é estudado

O código começa a tomar decisões: comparar valores, escolher caminhos com `if`/`elif`/`else`, validar entradas e criar pequenos jogos com sorteio.

## Conceitos

- `if`, `elif` e `else`
- comparações e operadores lógicos (`and`, `or`, `not`)
- operador de resto (`%`) para par/ímpar
- validação de dados
- `random.randint()` e `random.choice()`
- condições compostas e intervalos

## Exercícios

| Arquivo | O que faz | O que pratica |
|---|---|---|
| 01 - Par ou Ímpar.py | Diz se o número é par ou ímpar | Operador `%` (resto) — o truque mais útil de validação |
| 02 - Comparar Dois Números.py | Compara dois números | Analisar todos os casos: maior, menor ou iguais |
| 03 - Maior e Menor de Três.py | Maior e menor entre 3 números | Cadeia de comparações sem se apoiar em `elif` |
| 04 - Validação de Dados.py | Repete a pergunta até receber F ou M | Validação com `while ... not in` |
| 05 - Radar de Velocidade.py | Multa acima de 80 km/h | Limite + cálculo do excedente (R$7 por km) |
| 06 - Aumento de Salário.py | Aumento de 10% ou 15% conforme salário | Dois cenários em `if`/`else` |
| 07 - Preço da Viagem.py | R$0,50/km curto, R$0,45/km longo | Faixas de valores para o mesmo cálculo |
| 08 - Ano Bissexto.py | Descobre se o ano é bissexto | Operadores lógicos combinados |
| 09 - Classificação de Atleta.py | Classifica por idade (mirim a master) | `elif` encadeado para muitos cenários |
| 10 - Alistamento Militar.py | Diz o que a idade exige do alistamento | Intervalos fechados na decisão |
| 11 - Aprovação de Empréstimo.py | A parcela cabe em 30% do salário? | Condição de negócio comparando cálculo com limite |
| 12 - Verificar Triângulo.py | Os segmentos formam triângulo? | Condição composta com 3 variáveis |
| 13 - Adivinha o Número.py | Jogo: acertar número de 0 a 5 | `randint()` + comparação |
| 14 - Adivinha com Dicas.py | Mesmo jogo com dicas (maior/menor) | Melhorar a versão anterior do próprio código |
| 15 - Jokenpô.py | Pedra, papel, tesoura vs. computador | Mapear opções em números e cobrir cenários |
| 16 - Jogo do Par ou Ímpar.py | Par ou ímpar com placar | Jogo completo: condição + sorteio + acumulador |

## Como executar

```bash
python3 "02-condicoes/13 - Adivinha o Número.py"
```

## Por que este capítulo importa

Condições transformam cálculos em decisões. É aqui que o programa passa a responder a situações diferentes, em vez de seguir sempre a mesma linha.

[← Capítulo anterior](01-fundamentos.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](03-lacos-e-logica.md)
