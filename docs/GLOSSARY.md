# Glossário

[← Voltar ao README](../README.md)

Termos que aparecem nos exercícios deste repositório, explicados de forma curta para quem está começando.

## Fundamentos

- **Variável** — nome que guarda um valor para usar depois. Ex.: `idade = 18`.
- **`input()`** — lê texto digitado pelo usuário. O retorno é sempre `str`.
- **`print()`** — mostra um valor na tela.
- **`int()` / `float()`** — convertem texto para número inteiro ou decimal.
- **f-string** — texto com valores embutidos. Ex.: `f"Olá, {nome}"`.
- **Operador aritmético** — `+`, `-`, `*`, `/`, `**`, `//` e `%`.
- **`//`** — divisão inteira, sem a parte decimal.
- **`%`** — resto da divisão; muito usado para par/ímpar.
- **`import`** — traz um módulo ou biblioteca para o arquivo.

## Decisões

- **`if` / `elif` / `else`** — escolhem qual bloco de código executar.
- **Operador lógico** — `and`, `or` e `not`, usados para combinar condições.
- **Validação** — repetir ou bloquear uma entrada até ela ser aceitável.

## Repetição

- **`for`** — repete para cada item de uma sequência ou intervalo.
- **`range()`** — gera uma sequência de números para o `for`.
- **`while`** — repete enquanto uma condição for verdadeira.
- **`break`** — encerra o laço imediatamente.
- **Contador** — variável que soma 1 a cada repetição. Ex.: `cont += 1`.
- **Acumulador** — variável que guarda uma soma ou produto. Ex.: `soma += valor`.

## Coleções

- **Lista** — sequência mutável, escrita entre colchetes. Ex.: `[1, 2, 3]`.
- **Tupla** — sequência imutável, escrita entre parênteses. Ex.: `(1, 2, 3)`.
- **Dicionário** — conjunto de pares chave/valor. Ex.: `{"nome": "Kayke"}`.
- **Índice** — posição de um item, começando em 0.
- **Fatiamento** — pegar um trecho da sequência. Ex.: `lista[1:4]`.
- **Matriz** — lista dentro de lista, acessada por linha e coluna.
- **`append()` / `insert()`** — adicionam itens a uma lista.
- **`pop()`** — remove e devolve um item.
- **`sort()`** — ordena a própria lista.
- **`len()`** — devolve o tamanho da coleção.
- **`in` / `not in`** — verificam se um valor está ou não na coleção.

## Funções

- **Função** — bloco de código com nome, que pode ser chamado várias vezes.
- **Parâmetro** — nome recebido pela função na definição.
- **Argumento** — valor enviado na chamada da função.
- **`return`** — devolve um resultado para quem chamou a função.
- **Parâmetro opcional** — tem um valor padrão. Ex.: `def f(x, show=False)`.
- **`*args`** — recebe vários argumentos posicionais em uma tupla.
- **Docstring** — texto de documentação logo abaixo de `def`.
- **Módulo / biblioteca** — arquivo ou pacote de código pronto para reutilizar.

## Bibliotecas usadas

- **`math`** — funções matemáticas, como `math.trunc()`.
- **`random`** — sorteios, como `random.randint()` e `random.choice()`.
- **`time`** — pausas e contagem de tempo, como `time.sleep()`.
- **`datetime`** — datas e horas.
- **`operator.itemgetter`** — critério de ordenação para `sorted()`.
- **`pygame`** — biblioteca externa usada no exercício de MP3; precisa ser instalada.
- **`help()`** — mostra a documentação de um comando ou biblioteca no terminal.

[← Voltar ao README](../README.md)
