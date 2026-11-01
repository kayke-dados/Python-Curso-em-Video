# Auditoria — Python-Journey

**Data:** 01/11/2026  
**Commit auditado:** `abb5e38` (`Add files via upload`)  
**Escopo:** estrutura, exercícios, documentação, configurações e consistência do repositório.

Esta auditoria foi feita antes de qualquer alteração. A regra principal do projeto é preservar os exercícios Python exatamente como estão.

> Os caminhos abaixo refletem o estado auditado em `abb5e38`. Durante a modernização, a pasta `06-Funções` foi renomeada para `06-funcoes`, sem alterar nenhum arquivo.

## Estrutura encontrada

```text
Python-Journey/
├── .github/workflows/check.yml
├── .gitignore
├── 01-fundamentos/            12 arquivos
├── 02-condicoes/              16 arquivos
├── 03-lacos-e-logica/         25 arquivos
├── 04-listas-e-tuplas/        18 arquivos (12 listas + 6 tuplas)
├── 05-dicionarios/             5 arquivos (sem Ex92)
├── 06-Funções/                11 arquivos (Ex96 a Ex106)
├── 07-proximos-aprendizados/   apenas README
├── LICENSE                     MIT
├── README.md
└── banner.svg
```

## Contagem real

A contagem foi feita diretamente nos arquivos `.py`, sem confiar no README.

| Capítulo | Arquivos | Linhas |
|---|---:|---:|
| 01-fundamentos | 12 | 100 |
| 02-condicoes | 16 | 252 |
| 03-lacos-e-logica | 25 | 421 |
| 04-listas-e-tuplas | 18 | 387 |
| 05-dicionarios | 5 | 150 |
| 06-Funções | 11 | 226 |
| **Total** | **87** | **1.536** |

- Tamanho total dos exercícios: **37.586 bytes**.
- Nenhum arquivo vazio.
- Nenhum erro de sintaxe detectado com `ast.parse`.
- Nenhum arquivo com encoding inválido.
- Imports encontrados: `datetime`, `math`, `operator`, `pygame`, `random`, `time`.
- Única dependência externa: `pygame`, no exercício `01-fundamentos/12 - Tocar MP3 com Pygame.py`.

## Problemas de documentação

1. O README informa **86 exercícios**, mas existem **87**.
2. O README informa o capítulo 06 com **10 arquivos**; existem **11** (Ex96 a Ex106).
3. O README marca `ex105` como pendente e o capítulo 06 como **9/10**; os dois já existem.
4. O banner informa **85/86**, desatualizado em relação ao README e ao repositório.
5. O badge de exercícios usa `exerc%C3%idados`, encoding inválido: a URL retorna **HTTP 400**.
6. A árvore do README usa `Programação/` como raiz, mas a raiz real é `Python-Journey/`.
7. A árvore usa `06-Funcoes`, enquanto a pasta real é `06-Funções`.
8. O README concentra tabelas com todos os 87 exercícios em um único arquivo, o que gera rolagem longa no celular.
9. A pasta `06-Funções` foge do padrão das demais: minúsculas e sem acento.
10. Não existem documentos de auditoria, roadmap, glossário, diário de evolução ou verificação de integridade.

## Configurações atuais

- **GitHub Actions:** apenas `python -m compileall -q .` em push e pull request.
- **.gitignore:** cobre Python, ambientes virtuais, arquivos de sistema/editor e `*.output`.
- **Licença:** MIT, Kayke, 2026.
- **Banner:** SVG válido, paleta `#141414`, `#343434`, `#9B8AC4`, `#A6A29C`, `#F5F3EF`.
- **Segredos:** nenhuma ocorrência de senha, token ou chave privada na varredura textual.

## Oportunidades de melhoria

- Corrigir a contagem oficial para **87/87**.
- Separar o detalhe dos exercícios em guias por capítulo, mantendo o README enxuto.
- Criar índice navegável e links internos confiáveis.
- Criar glossário com conceitos que realmente aparecem nos exercícios.
- Criar roadmap com o que está concluído, em andamento e planejado.
- Criar diário de evolução baseado em marcos reais do Git.
- Criar manifesto SHA-256 e script de verificação de integridade.
- Ampliar o workflow para validar sintaxe, links, contagens e hashes.
- Padronizar `06-Funções` para `06-funcoes`.

## Restrições identificadas

- Os exercícios são **intocáveis**, inclusive formatação e comentários.
- Muitos exercícios usam `input()`; não devem ser executados automaticamente.
- O `pygame` não deve ser dependência obrigatória da verificação.
- Não há evidência de estudo de POO, bancos de dados, SQL, Pandas ou visualização; esses temas ficam apenas no roadmap.

## Conclusão

O repositório tem conteúdo real e consistente, mas a documentação está atrasada em relação aos arquivos. A contagem correta é **87 exercícios**. A modernização deve corrigir a documentação, organizar a navegação e criar verificações, sem alterar nenhum exercício.
