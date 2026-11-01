# Capítulo 03 — Laços e lógica

[← Capítulo anterior](02-condicoes.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](04-listas-e-tuplas.md)

## O que é estudado

Repetição e controle de fluxo: `for`, `while`, contadores, acumuladores, menus, `break` e os primeiros algoritmos clássicos. É o capítulo com mais exercícios do projeto.

## Conceitos

- `for` com `range()`
- `while` e `while True`
- contadores e acumuladores
- `break` e flags de parada
- laços aninhados
- menus interativos
- sequências (Fibonacci, progressão aritmética, fatorial)
- divisão inteira (`//`) e resto (`%`)

## Exercícios

| Arquivo | O que faz | O que pratica |
|---|---|---|
| 01 - Pares com For.py | Mostra os pares de 0 a 100 | `for` com `range` e passo diferente de 1 |
| 02 - Contagem Regressiva.py | Conta de N até 1 com `while` | Decremento manual |
| 03 - Contagem com Pausa.py | Contagem com efeito dramático | `time.sleep()` — pausar a execução |
| 04 - Soma de Seis Valores.py | Lê 6 números e soma | Acumulador dentro de `for` |
| 05 - Maior e Menor Peso.py | Maior e menor peso entre 5 pessoas | Começar pelo 1º valor e atualizar o recorde |
| 06 - Menu de Cálculos.py | Menu: somar, multiplicar, maior, sair | Menus com `while True` |
| 07 - Analisador de Grupo.py | De 5 pessoas: média, mais velho, mulher<20 | Condições + acumuladores na mesma leitura |
| 08 - Média do Aluno.py | Situação: reprovado, recuperação, aprovado | Classificar por faixas de valor |
| 09 - Maiores de Idade.py | Conta quantos de 7 são maiores de idade | Contador com condição |
| 10 - Maior, Menor e Soma.py | Vários números até a pessoa desistir | Leitura ilimitada + 3 cálculos em paralelo |
| 11 - Somando até 999.py | Soma números até digitar 999 | Flag de parada no valor consumido |
| 12 - Parada com Break.py | Versão 2 do exercício anterior | `break` — sair do `while` no meio |
| 13 - Tabuada com For.py | Tabuadas infinitas | `for` dentro de `while` — laços aninhados |
| 14 - Tabuada com Break.py | Tabuada que encerra com número negativo | `break` em laço aninhado |
| 15 - Progressão Aritmética.py | Os 10 primeiros termos de uma PA | Guardar a razão separada do termo corrente |
| 16 - PA com Mais Termos.py | PA que pede mais termos em execução | Estender o laço enquanto roda |
| 17 - Fibonacci.py | N termos da sequência de Fibonacci | Troca de valores entre variáveis (ANT/FAB) |
| 18 - Fatorial.py | Fatorial com a conta visível | Acumulador de produto e `end=' '` |
| 19 - Cadastro com Contadores.py | Conta maiores, homens e mulher<20 | Vários contadores rodando no mesmo laço |
| 20 - Cálculo de IMC.py | IMC e categoria (abaixo/ideal/sobrepeso...) | Faixas de saúde com classificação |
| 21 - Formas de Pagamento.py | Á vista, cartão 2x/3x — descontos e juros | Tabela de opções com `%` por escolha |
| 22 - Loja Super Baratão.py | Carrinho: total, itens >R$1000, mais barato | O compilado do capítulo: acumular + comparar + validar |
| 23 - Tipos de Triângulo.py | Se é equilátero, isósceles ou escaleno | Validar e depois categorizar |
| 24 - Números Primos.py | Lista os números de 1 até N | `for` com `range`; a checagem de primos ainda não foi feita |
| 25 - Caixa Eletrônico.py | Saque em cédulas de R$50, R$10 e R$1 | `//` (divisão inteira) + `%` para decompor cédulas |

> **Observação:** o exercício 24 foi preservado como estava quando foi escrito. Ele lista os números de 1 até N, mas ainda não verifica divisores.

## Como executar

```bash
python3 "03-lacos-e-logica/17 - Fibonacci.py"
```

## Por que este capítulo importa

Laços permitem repetir trabalho sem repetir código. Contadores, acumuladores e menus são a base de programas maiores e de quase todo exercício que lê vários dados.

[← Capítulo anterior](02-condicoes.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](04-listas-e-tuplas.md)
