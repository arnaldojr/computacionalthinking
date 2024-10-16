## Estruturas de Decisão

Em Python, as estruturas de decisão são fundamentais para controlar o fluxo de execução de um programa. Elas permitem que o código tome decisões e execute diferentes blocos de instruções com base em diferentes condições. Estas estruturas são essenciais para a lógica de programação e representam a base de muitos algoritmos.

### Entendendo Condições

As estruturas de decisão em Python dependem das condições que são avaliadas como verdadeiras (`True`) ou falsas (`False`). Estas condições são frequentemente baseadas em operadores de comparação e lógicos.

#### Operadores de Comparação

Estes operadores são usados para comparar valores:

- `==`: Igual a
- `!=`: Diferente de
- `<`: Menor que
- `>`: Maior que
- `<=`: Menor ou igual a
- `>=`: Maior ou igual a

### Exercícios sobre Operadores de Comparação

<?quiz?>

question: Dado `x = 5` e `y = 10`, qual das seguintes afirmações é verdadeira?
answer-correct: x < y
answer: x > y
answer: x == y
answer: x >= y
content:
`x < y` é verdadeiro porque 5 é menor que 10.
<?/quiz?>

<?quiz?>

question: Se `a = "hello"` e `b = "world"`, qual das seguintes condições é verdadeira?
answer: a == b
answer-correct: a != b
answer: a > b
answer: a < b
content:
`a != b` é verdadeiro porque "hello" é diferente de "world".
<?/quiz?>

#### Operadores Lógicos

Estes operadores são usados para combinar condições:

- `and`: Retorna verdadeiro se ambas as condições forem verdadeiras
- `or`: Retorna verdadeiro se pelo menos uma das condições for verdadeira
- `not`: Inverte o resultado da condição

### Exercícios sobre Operadores Lógicos

<?quiz?>

question: Dado `x = True` e `y = False`, qual das seguintes expressões retorna `True`?
answer-correct: x and not y
answer: not x and y
answer: x and y
answer: not x or y
content:
`x and not y` retorna `True` porque `x` é verdadeiro e `y` é falso (e `not y` é verdadeiro).
<?/quiz?>

<?quiz?>

question: Se `m = False` e `n = False`, qual das seguintes expressões é `True`?
answer: m and n
answer: m or n
answer-correct: not m and not n
answer: not m or n
content:
`not m and not n` é verdadeiro porque ambos `m` e `n` são falsos e a negação de ambos é verdadeira.
<?/quiz?>


### A Estrutura `if`

A estrutura `if` é a base das estruturas de decisão em Python. Ela avalia uma condição e, se essa condição for verdadeira, executa o bloco de código indentado sob ela.

```python
temperatura = 30
if temperatura > 25:
    print("Está quente!")
```

### Exercícios sobre `if`

```quiz
{
    "questao": "Qual será a saída do seguinte código se `valor = 50`?",
    "opcoes": {
        "a": "`Alto`",
        "b": "`Baixo`",
        "c": "Não haverá saída",
        "d": "Ocorrerá um erro",
    },
    "correta": "c",
    "code": """
```python
a = 10
valor = a
valor = a**2
if valor < 100:
    print("Baixo")
```"""
}
```

### A Estrutura `else`

O `else` captura qualquer condição que não tenha sido capturada pelas cláusulas `if` e `elif`. Não tem uma condição associada a ela, pois serve como um coletor padrão.

### Exercícios sobre `else`


```quiz
{
    "questao": "Dado o código abaixo, qual será a saída se `num = 10`?",
    "opcoes": {
        "a": "`Par`",
        "b": "`Impar`",
        "c": "Não haverá saída",
        "d": "Ocorrerá um erro",
    },
    "correta": "a",
    "code": """
```python
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")
```"""
}
```


<?quiz?>

question: Usando o mesmo código, qual será a saída se `num = 15`?
answer: `Par`
answer-correct: `Ímpar`
answer: Não haverá saída
answer: Ocorrerá um erro
content:
A saída será `Ímpar` porque 15 não é divisível por 2.
<?/quiz?>


### A Estrutura `elif`

A palavra-chave `elif` é uma abreviação de "else if". É útil quando você precisa verificar várias condições em sequência. Ela segue um `if` ou outro `elif` e sua condição é avaliada apenas se as condições anteriores não forem satisfeitas.

```python
temperatura = 20
if temperatura > 25:
    print("Está quente!")
elif temperatura < 18:
    print("Está frio!")
else:
    print("Está ameno!")
```

### Exercícios sobre `elif`

```quiz
{
    "questao": "Dado o código abaixo, qual será a saída se `pontos = 75`?",
    "opcoes": {
        "a": "`Bom!`",
        "b": "`Excelente!`",
        "c": "Tente novamente",
        "d": "Muito bom!",
    },
    "correta": "a",
    "code": """
    ```python
if pontos > 90:
    print("Excelente!")
elif pontos > 80:
    print("Muito bom!")
elif pontos > 70:
    print("Bom!")
else:
    print("Tente novamente")
```"""
}
```


<?quiz?>

question: Considerando o código da questão anterior, qual será a saída se `pontos = 50`?
answer: `Excelente!`
answer: `Muito bom!`
answer: `Bom!`
answer-correct: `Tente novamente`
content:
A saída será `Tente novamente` porque 50 é menor do que todos os pontos de corte especificados.
<?/quiz?>


### Aninhamento

É possível aninhar estruturas `if` dentro de outras estruturas `if`. Isso permite criar avaliações mais complexas. No entanto, é importante garantir que o código permaneça legível e evitar aninhamentos excessivamente profundos.

```python
idade = 15
acompanhado = True

if idade < 18:
    if acompanhado:
        print("Menor de idade, mas está acompanhado.")
    else:
        print("Menor de idade e desacompanhado.")
else:
    print("Maior de idade.")
```

### Exercícios sobre Aninhamento

<?quiz?>

question: Usando o código acima, qual será a saída se `idade = 13` e `acompanhado = False`?
answer: `Menor de idade, mas está acompanhado.`
answer-correct: `Menor de idade e desacompanhado.`
answer: `Maior de idade.`
answer: Não haverá saída
content:
A saída será `Menor de idade e desacompanhado.` porque a idade é menor que 18 e a variável `acompanhado` é `False`.
<?/quiz?>

### Dicas e Boas Práticas

1. **Mantenha a legibilidade**: Evite aninhar muitos níveis de condições. Se um `if` tem muitos `elif` ou níveis profundos de aninhamento, pode ser um sinal de que o código precisa ser refatorado.
2. **Evite condições complexas**: Se uma condição está se tornando muito complexa, considere dividi-la ou use variáveis intermediárias para tornar a lógica mais clara.
3. **Use parênteses para clareza**: Em condições complexas com múltiplos operadores lógicos, use parênteses para tornar a ordem das avaliações clara.
