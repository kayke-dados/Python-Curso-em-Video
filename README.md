![Python — Curso em Vídeo: 87 exercícios em 6 capítulos](banner.svg)

# Python — Curso em Vídeo

Meus exercícios do [curso de Python do Curso em Vídeo](https://www.youtube.com/@CursoemVideo), de Gustavo Guanabara, do primeiro `print()` às minhas próprias funções.

![Python 3](https://img.shields.io/badge/Python-3.x-2DD4BF?style=for-the-badge&logo=python&logoColor=0b0b0a&labelColor=141414)
![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-2DD4BF?style=for-the-badge&labelColor=141414)

Este repositório é um **registro de estudo**, não um projeto. Cada arquivo é um exercício como eu o escrevi na hora, inclusive quando ainda há o que melhorar. Meus projetos de análise ficam em outros repositórios, listados em [kayke-space.vercel.app](https://kayke-space.vercel.app).

## Conteúdo

Reorganizei o curso na ordem em que aprendi, em vez de seguir a divisão original.

| Capítulo | Exercícios | O que pratiquei | Guia |
|---|---:|---|---|
| [01 — Fundamentos](01-fundamentos) | 12 | `print()`, `input()`, variáveis, tipos, operadores, f-strings, `import` | [abrir](docs/capitulos/01-fundamentos.md) |
| [02 — Condições](02-condicoes) | 16 | `if`/`elif`/`else`, operadores lógicos, validação, `random` | [abrir](docs/capitulos/02-condicoes.md) |
| [03 — Laços e lógica](03-lacos-e-logica) | 25 | `for`, `while`, `range()`, `break`, contadores, acumuladores, menus | [abrir](docs/capitulos/03-lacos-e-logica.md) |
| [04 — Listas e tuplas](04-listas-e-tuplas) | 18 | índices, fatiamento, ordenação, `append`/`insert`/`pop`, matrizes | [abrir](docs/capitulos/04-listas-e-tuplas.md) |
| [05 — Dicionários](05-dicionarios) | 5 | chave/valor, listas como valores, `sorted()`, `itemgetter` | [abrir](docs/capitulos/05-dicionarios.md) |
| [06 — Funções](06-funcoes) | 11 | parâmetros, `return`, valores padrão, `*args`, docstrings, `help()` | [abrir](docs/capitulos/06-funcoes.md) |

Total: **87 exercícios** em 6 capítulos. A contagem é conferida nos arquivos (última conferência: 01/11/2026).

## Como executar

Na raiz do repositório:

```bash
python3 "02-condicoes/13 - Adivinha o Número.py"
```

A maioria usa `input()`, então espera digitação no terminal. Só o exercício `01-fundamentos/12 - Tocar MP3 com Pygame.py` precisa de dependência externa (`pip install pygame`). Os outros usam apenas a biblioteca padrão.

## Limites conhecidos

- O exercício 24 de laços lista os números de 1 até N, mas ainda não verifica quais são primos. Deixei como foi escrito.
- Os exercícios acompanham as aulas e não passaram por revisão de estilo ou testes mais profundos.

## Próximos passos

Tratamento de exceções, arquivos, orientação a objetos, ambientes virtuais, SQL e análise de dados. Nada disso conta como concluído até existir aqui. O plano está em [docs/ROADMAP.md](docs/ROADMAP.md) e o histórico em [docs/STUDY-LOG.md](docs/STUDY-LOG.md).

---

*A organização da documentação contou com apoio de IA, a partir dos exercícios reais do repositório. O código dos exercícios é o registro do meu aprendizado. Licença MIT.*
