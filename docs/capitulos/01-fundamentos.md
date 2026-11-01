# Capítulo 01 — Fundamentos

[← Voltar ao índice](../README.md) · [Próximo capítulo →](02-condicoes.md)

## O que é estudado

A estreia com código: conversar com o computador, guardar valores, fazer contas e usar as primeiras bibliotecas. É a base de tudo o que vem depois.

## Conceitos

- `print()` e `input()`
- variáveis e tipos de dados
- conversão de texto para número
- operadores aritméticos
- f-strings e formatação de saída
- `import` e bibliotecas (`math`, `random`)
- bibliotecas externas (`pygame`)

## Exercícios

| Arquivo | O que faz | O que pratica |
|---|---|---|
| 01 - Calculadora Simples.py | As 4 operações, escolhidas pelo usuário | Primeiro `if`/`elif` escolhendo caminhos |
| 02 - Dobro, Triplo e Raiz.py | Mostra dobro, triplo e raiz de um número | Operadores aritméticos e `** (1/2)` para raiz |
| 03 - Conversão de Medidas.py | Converte metros em centímetros e milímetros | Multiplicação encadeada e saída formatada |
| 04 - Área da Parede.py | Calcula a área de uma parede | Variáveis guardando resultados intermediários |
| 05 - Média de Notas.py | Média de 2 ou 3 notas, conforme a quantidade | Condição sobre a própria entrada |
| 06 - Calculadora de Desconto.py | Aplica % de desconto sobre o preço | Cálculo de porcentagem |
| 07 - Conversor de Moeda.py | Converte reais em dólares | Cálculo direto e f-strings |
| 08 - Tabuada Simples.py | Monta a tabuada do número escolhido | Organizar resultados de cálculo em colunas |
| 09 - Primeiro Módulo (Math).py | Mostra a porção inteira de um decimal | `import` — biblioteca pronta (`math.trunc()`) |
| 10 - Sorteio Aleatório.py | Sorteia 1 entre 4 alunos digitados | `random.choice()` — decisão aleatória |
| 11 - Embaralhar Ordem (Shuffle).py | Sorteia a ordem de apresentação dos alunos | `random.shuffle()` — misturar uma lista |
| 12 - Tocar MP3 com Pygame.py | Toca uma música MP3 | Bibliotecas externas (`pygame`) exigem instalação |

## Como executar

```bash
python3 "01-fundamentos/01 - Calculadora Simples.py"
```

O exercício 12 precisa do `pygame`:

```bash
python3 -m pip install pygame
```

## Por que este capítulo importa

Sem entrada, saída, variáveis e operadores não existe programa. Este capítulo também marca o primeiro contato com código de outra pessoa: as bibliotecas.

[← Voltar ao índice](../README.md) · [Próximo capítulo →](02-condicoes.md)
