# Capítulo 04 — Listas e tuplas

[← Capítulo anterior](03-lacos-e-logica.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](05-dicionarios.md)

## O que é estudado

Coleções: guardar vários valores em uma única variável, percorrer, ordenar, fatiar e montar estruturas com listas dentro de listas. As tuplas entram como a versão imutável das sequências.

## Conceitos

- listas e tuplas
- índices, fatiamento e `len()`
- `append()`, `insert()`, `pop()`, `sort()`, `index()`, `count()`
- `in` e `not in`
- listas dentro de listas (matrizes)
- laços para percorrer coleções
- tuplas imutáveis e desempacotamento por índice

## Exercícios

### listas/ — Ex78 a Ex89

| Arquivo | O que faz | O que pratica |
|---|---|---|
| Ex78 - Maior e Menor nas Posições.py | 5 valores: maior/menor e a posição de cada | `index()` + recorde em lista |
| Ex79 - Valores sem Repetição.py | Rejeita número repetido com aviso | `not in` + `sort()` |
| Ex80 - Inserção Ordenada.py | Insere já em ordem crescente | `insert(pos)` buscando o ponto certo |
| Ex81 - Ordem Decrescente.py | Lista invertida + o valor 5 está lá? | `sort(reverse=True)` e `len()` |
| Ex82 - Pares e Ímpares em Listas.py | Divide os valores em 2 listas | Duas listas paralelas no mesmo laço |
| Ex83 - Pilha de Parênteses.py | Valida expressão por `(` e `)` | Pilha com `append`/`pop` |
| Ex84 - Cadastro com Peso.py | Lista de nome+peso de várias pessoas | Lista dentro de lista com `[:]` e `clear()` |
| Ex85 - Pares e Ímpares na Matriz.py | Matriz organiza pares numa linha, ímpares na outra | Percorrer matriz por linha |
| Ex86 - Matriz 3x3.py | Monta uma matriz 3x3 completa | Notação `matriz[i][j]` |
| Ex87 - Soma na Matriz.py | Soma pares, coluna 3 e a maior linha | Coordenadas específicas na matriz |
| Ex88 - Mega Sena.py | Sorteia jogos da mega sena com timer | `randint` + evitar repetidos + `sort()` |
| Ex89 - Boletim de Alunos.py | Alunos com 2 notas, média e boletim | Listas dentro de listas + colunas com `:<4` |

### tuplas/ — práticas

| Arquivo | O que faz | O que pratica |
|---|---|---|
| Tupla - Análise de Valores.py | 4 números: vezes que o 9 apareceu e posição do 3 | Tupla é imutável, mas tem `count()` e `index()` |
| Tupla - Maior e Menor Sorteio.py | 5 sorteados e maior/menor | Recorde com tupla |
| Tupla - Número por Extenso.py | Número 0-20 como texto completo | Escolher pelo índice evita ifs gigantes |
| Tupla - Tabela de Preços.py | Listagem formatada em tabela | Fatiar alternado (nome/preço) + `>.2f` |
| Tupla - Times do Brasileirão.py | Tabela do brasileirão por fatias | `[:5]`, `[-4:]` e `sorted()` |
| Tupla - Vogais nas Palavras.py | Vogais de cada palavra da tupla | `for` dentro de `for` por caractere |

## Como executar

```bash
python3 "04-listas-e-tuplas/listas/Ex83 - Pilha de Parênteses.py"
```

## Por que este capítulo importa

Quase todo programa real lida com vários dados ao mesmo tempo. Listas e tuplas são a primeira ferramenta para organizar, percorrer e transformar coleções.

[← Capítulo anterior](03-lacos-e-logica.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](05-dicionarios.md)
