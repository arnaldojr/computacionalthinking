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

!!! exercise choice "Questão"
    Dado `x = 5` e `y = 10`, qual das seguintes afirmações é verdadeira?
    
    - [x] `x < y`
    - [ ] `x > y`
    - [ ] `x == y`
    - [ ] `x >= y`

    !!! answer
        `x < y` é verdadeiro porque 5 é menor que 10.

!!! exercise choice "Questão"
    Se `a = "hello"` e `b = "world"`, qual das seguintes condições é verdadeira?
    
    - [ ] `a == b`
    - [x] `a != b`
    - [ ] `a > b`
    - [ ] `a < b`

    !!! answer
        `a != b` é verdadeiro porque "hello" é diferente de "world".

#### Operadores Lógicos

Estes operadores são usados para combinar condições:

- `and`: Retorna verdadeiro se ambas as condições forem verdadeiras
- `or`: Retorna verdadeiro se pelo menos uma das condições for verdadeira
- `not`: Inverte o resultado da condição

### Exercícios sobre Operadores Lógicos

!!! exercise choice "Questão"
    Dado `x = True` e `y = False`, qual das seguintes expressões retorna `True`?
    
    - [x] `x and not y`
    - [ ] `not x and y`
    - [ ] `x and y`
    - [ ] `not x or y`

    !!! answer
        `x and not y` retorna `True` porque `x` é verdadeiro e `y` é falso (e `not y` é verdadeiro).

!!! exercise choice "Questão"
    Se `m = False` e `n = False`, qual das seguintes expressões é `True`?
    
    - [ ] `m and n`
    - [ ] `m or n`
    - [x] `not m and not n`
    - [ ] `not m or n`

    !!! answer
        `not m and not n` é verdadeiro porque ambos `m` e `n` são falsos e a negação de ambos é verdadeira.


!!! progress
    Continuar...


### A Estrutura `if`

A estrutura `if` é a base das estruturas de decisão em Python. Ela avalia uma condição e, se essa condição for verdadeira, executa o bloco de código indentado sob ela.

```python
temperatura = 30
if temperatura > 25:
    print("Está quente!")
```

### Exercícios sobre `if`

!!! exercise choice "Questão"
    Qual será a saída do seguinte código se `valor = 50`?
    
    ```python
    if valor > 100:
        print("Alto")
    else:
        print("Baixo")
    ```
    
    - [ ] `Alto`
    - [x] `Baixo`
    - [ ] Não haverá saída
    - [ ] Ocorrerá um erro

    !!! answer
        A saída será `Baixo` porque a condição `valor > 100` é falsa.

### A Estrutura `else`

O `else` captura qualquer condição que não tenha sido capturada pelas cláusulas `if` e `elif`. Não tem uma condição associada a ela, pois serve como um coletor padrão.

### Exercícios sobre `else`

!!! exercise choice "Questão"
    Dado o código abaixo, qual será a saída se `num = 10`?
    
    ```python
    if num % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
    ```
    
    - [x] `Par`
    - [ ] `Ímpar`
    - [ ] Não haverá saída
    - [ ] Ocorrerá um erro

    !!! answer
        A saída será `Par` porque 10 é divisível por 2.

!!! exercise choice "Questão"
    Usando o mesmo código, qual será a saída se `num = 15`?
    
    - [ ] `Par`
    - [x] `Ímpar`
    - [ ] Não haverá saída
    - [ ] Ocorrerá um erro

    !!! answer
        A saída será `Ímpar` porque 15 não é divisível por 2.


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

!!! exercise choice "Questão"
    Dado o código abaixo, qual será a saída se `pontos = 75`?
    
    ```python
    if pontos > 90:
        print("Excelente!")
    elif pontos > 80:
        print("Muito bom!")
    elif pontos > 70:
        print("Bom!")
    else:
        print("Tente novamente")
    ```
    
    - [ ] `Excelente!`
    - [ ] `Muito bom!`
    - [x] `Bom!`
    - [ ] `Tente novamente`

    !!! answer
        A saída será `Bom!` porque 75 é maior que 70 mas menor que 80.

!!! exercise choice "Questão"
    Considerando o código acima, qual será a saída se `pontos = 50`?
    
    - [ ] `Excelente!`
    - [ ] `Muito bom!`
    - [ ] `Bom!`
    - [x] `Tente novamente`

    !!! answer
        A saída será `Tente novamente` porque 50 é menor do que todos os pontos de corte especificados.


!!! progress
    Continuar...


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

!!! exercise choice "Questão"
    Usando o código acima, qual será a saída se `idade = 13` e `acompanhado = False`?
    
    - [ ] `Menor de idade, mas está acompanhado.`
    - [x] `Menor de idade e desacompanhado.`
    - [ ] `Maior de idade.`
    - [ ] Não haverá saída

    !!! answer
        A saída será `Menor de idade e desacompanhado.` porque a idade é menor que 18 e a variável `acompanhado` é `False`.

### Dicas e Boas Práticas

1. **Mantenha a legibilidade**: Evite aninhar muitos níveis de condições. Se um `if` tem muitos `elif` ou níveis profundos de aninhamento, pode ser um sinal de que o código precisa ser refatorado.
2. **Evite condições complexas**: Se uma condição está se tornando muito complexa, considere dividi-la ou use variáveis intermediárias para tornar a lógica mais clara.
3. **Use parênteses para clareza**: Em condições complexas com múltiplos operadores lógicos, use parênteses para tornar a ordem das avaliações clara.
