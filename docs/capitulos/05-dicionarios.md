# Capítulo 05 — Dicionários

[← Capítulo anterior](04-listas-e-tuplas.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](06-funcoes.md)

## O que é estudado

A mudança de chave: em vez de buscar pela posição, o dado fica atrás de um nome. É o começo dos registros estruturados, como um banco de dados simples.

## Conceitos

- criação e acesso por chave
- `dado['chave'] = valor`
- percorrer chaves, valores e itens
- listas como valores de um dicionário
- `sorted()` com `itemgetter`
- `.copy()` e o cuidado com referências

## Exercícios

| Arquivo | O que faz | O que pratica |
|---|---|---|
| Ex90 - Cadastro do Aluno.py | Nome + média + situação em um dicionário | `dado['chave'] = valor` |
| Ex91 - Ranking de Jogadores.py | Sorteia nota de 4 visitantes e ranqueia | `sorted()` com `itemgetter` em dicionário |
| Ex93 - Aproveitamento do Jogador.py | Gols por partida viram lista no dicionário | Valor complexo (lista) como valor |
| Ex94 - Cadastro do Grupo.py | Várias pessoas com nome, sexo e idade | Lista de dicionários com `.copy()` — atenção ao `clear()` |
| Ex95 - Tabela de Jogadores.py | Vários jogadores e seus gols | Dados complexos embutidos |

> O Ex92 não faz parte deste registro. Os cinco exercícios acima são os que existem na pasta.

## Como executar

```bash
python3 "05-dicionarios/Ex91 - Ranking de Jogadores.py"
```

## Por que este capítulo importa

Dicionários dão nome aos dados. Isso deixa o código mais legível e prepara o caminho para estruturas maiores, como registros de usuários e resultados de consultas.

[← Capítulo anterior](04-listas-e-tuplas.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](06-funcoes.md)
