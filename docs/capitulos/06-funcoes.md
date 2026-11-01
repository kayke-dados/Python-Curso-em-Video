# Capítulo 06 — Funções

[← Capítulo anterior](05-dicionarios.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](07-proximos-aprendizados.md)

## O que é estudado

A última etapa do curso: escrever as próprias ferramentas. Dar nome à lógica, receber parâmetros, devolver resultados e reutilizar código sem copiar e colar.

## Conceitos

- definir e chamar funções
- parâmetros e argumentos
- `return` e funções sem retorno
- parâmetros opcionais e valores padrão
- `*args` e empacotamento
- docstrings
- validação encapsulada
- `help()` e cores ANSI no terminal

## Exercícios

| Arquivo | O que faz | O que pratica |
|---|---|---|
| Ex96 - Área com Função.py | `area(larg, compr)` calcula o terreno | Definir e chamar a primeira função |
| Ex97 - Escrita Destacada.py | `escreva(msg)` com bordas de `~` | Função que executa, sem retornar |
| Ex98 - Contagem com Função.py | Contagem com início, fim e passo | Parâmetros + `sleep()` dentro da função |
| Ex99 - Função Maior.py | Recebe quantidade de valores, acha o maior | Laço + acumulador dentro de função |
| Ex100 - Soma dos Pares.py | Sorteia 5 valores e soma os pares | Função que conduz o próprio fluxo |
| Ex101 - Função do Voto.py | Voto negado, facultativo ou obrigatório | Regra de negócio em função |
| Ex102 - Fatorial com Função.py | Fatorial com conta opcional | Docstring e parâmetro opcional (`show=False`) |
| Ex103 - Parâmetros Opcionais.py | `jogador(nome, gols)` aceita enter vazio | Valores default e `.isnumeric()` |
| Ex104 - Validar Inteiro.py | `leiaInt()` só aceita inteiro válido | Validação encapsulada e reutilizável |
| Ex105 - Analisando e gerando Dicionários.py | Analisa notas, calcula média e retorna dicionário | Empacotamento `*n` e parâmetros opcionais |
| Ex106 - Sistema de ajuda em Python.py | Mini PyHELP interativo com cores ANSI | Uso de cores e loop de ajuda com `help()` |

## Como executar

```bash
python3 "06-funcoes/Ex105 - Analisando e gerando Dicionários.py"
```

## Por que este capítulo importa

Funções são a primeira grande ferramenta de organização. Elas permitem dar nome a uma regra, testar isoladamente e reaproveitar a mesma lógica em vários programas.

[← Capítulo anterior](05-dicionarios.md) · [Voltar ao índice](../README.md) · [Próximo capítulo →](07-proximos-aprendizados.md)
