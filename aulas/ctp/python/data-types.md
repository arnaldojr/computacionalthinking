## Tipos de Dados em Python

O Python é uma linguagem de tipagem dinÂmica, ou seja, o tipo de uma variável é determinado em tempo de execução, com base no valor que ela contém. Isso significa que as variáveis não precisam ser explicitamente declaradas com um tipo específico. 

!!! tip
    Vale a pena mensionar que no Python, tudo é considerado um objeto. Isso significa que todos os valores, variáveis, funções e até mesmo tipos de dados são tratados como objetos. Mais adiante no curso vamos voltar e falar mais sobre isso.

### Tipos built-in

Os tipos primitivos em Python se referem aos tipos de dados básicos e fundamentais que são usados para representar valores simples. Vamos dar uma olhada e conhecer os principais. 

!!! tip
    Como sugestão leia a documentação oficial do python que trata deste assunto: [https://docs.python.org/pt-br/3.5/library/stdtypes.html](https://docs.python.org/pt-br/3.5/library/stdtypes.html) 

#### Números

Os números são uma parte essencial de qualquer linguagem de programação. Em Python, eles são definidos como objetos imutáveis, o que significa que seu valor não pode ser alterado após a criação.

- **Inteiros (int)**: São números sem uma parte decimal e podem ser positivos, negativos ou zero. Em Python, os inteiros são representados em base decimal por padrão, mas também podem ser expressos em base binária, octal ou hexadecimal.

  ```python
  decimal = 10
  binario = 0b10
  octal = 0o10
  hexadecimal = 0x10
  ```

- **Ponto Flutuante (float)**: Representam números reais e são escritos com uma parte decimal. Eles são especificados em notação decimal ou em notação científica.

  ```python
  decimal = 3.14
  notacao_cientifica = 2.5e3
  ```

#### Strings

Strings são sequências de caracteres Unicode. Em Python, as strings são imutáveis, o que significa que uma vez definidas, seus valores não podem ser alterados. Elas podem ser indexadas e fatiadas para obter sub-strings.
  
```python
texto = "Python"
primeira_letra = texto[0]  # Resultado: 'P'
sub_string = texto[1:4]  # Resultado: 'yth'
```

#### Booleanos

Os booleanos são usados para representar valores de verdade. Em Python, eles são subtipos de inteiros e têm apenas dois valores possíveis: `True` e `False`.

```python
verdadeiro = True
falso = False
```

### Exercícios sobre Tipos Primitivos

!!! exercise choice "Question"
    Qual dos seguintes é um exemplo válido de um número de ponto flutuante em Python?
    
    - [ ] `12345`
    - [x] `123.45`
    - [ ] `"123.45"`
    - [ ] `True`

    !!! answer
        `123.45` é um número de ponto flutuante válido em Python.

!!! exercise choice "Question"
    Qual é o valor da string após a execução do seguinte código: `texto = "Py" + "thon"`
    
    - [ ] `Py`
    - [ ] `thon`
    - [x] `Python`
    - [ ] `Pythonthon`

    !!! answer
        A string resultante da concatenação é `Python`.

!!! exercise choice "Question"
    Qual é o resultado da seguinte expressão booleana: `True and False`?
    
    - [ ] `True`
    - [x] `False`
    - [ ] `0`
    - [ ] `1`

    !!! answer
        O resultado da expressão `True and False` é `False`.


!!! progress
    Continuar...

### Variáveis e Atribuição

Variáveis em Python são referências a objetos na memória. A atribuição em Python é dinâmica, o que significa que o tipo de uma variável é determinado em tempo de execução.

```python
idade = 30
nome = "Maria"
```

#### Convenção para Nomes:

Nomes de variáveis devem ser minúsculos com palavras separadas por underlines.

```python
nome_completo = "João Silva"
idade_pessoa = 25
valor_total_compra = 150.50
```

#### Erros de Nomes:

No Python, cada variável deve ser atribuída antes de ser acessada. Se você tentar acessar uma variável que não foi atribuída, receberá um erro.

```python
# Isto causará um erro porque a variável 'salario' não foi definida antes de ser usada.
print(salario)
salario = 1000
```

### Atribuição Aumentada

A atribuição aumentada é a combinação, em uma única instrução, de uma operação binária e uma instrução de atribuição:

| Operação | Exemplo | Equivalente |
|----------|---------|-------------|
| +=       | a += b  | a = a + b   |
| -=       | a -= b  | a = a - b   |
| *=       | a *= b  | a = a * b   |
| /=       | a /= b  | a = a / b   |




### Exercícios sobre Variáveis e Atribuição

!!! exercise choice "Question"
    Após a execução do código `x = 5` e `y = x`, qual é o valor de `y`?
    
    - [ ] `0`
    - [x] `5`
    - [ ] `x`
    - [ ] `None`

    !!! answer
        O valor de `y` é `5`.

!!! exercise choice "Question"
    Se `nome = "Ana"`, qual é o resultado de `nome * 3`?
    
    - [ ] `AnaAnaAnaAna`
    - [x] `AnaAnaAna`
    - [ ] `Ana3`
    - [ ] `9`

    !!! answer
        O resultado é `AnaAnaAna`.

!!! exercise choice "Question"
    Qual é o tipo da variável após a execução do seguinte código: `valor = "123"`?
    
    - [ ] `int`
    - [x] `str`
    - [ ] `float`
    - [ ] `bool`

    !!! answer
        O tipo da variável `valor` é `str`.


!!! progress
    Continuar...


### Conversão de Tipos

Python permite a conversão explícita entre diferentes tipos de dados. Isso é útil quando você precisa operar valores de diferentes tipos juntos.

```python
# Convertendo float para int
numero_inteiro = int(7.8)  # Resultado: 7

# Convertendo int para float
numero_float = float(4)  # Resultado: 4.0

# Convertendo número para string
texto_numero = str(25)  # Resultado: '25'
```

### Exercícios sobre Conversão de Tipos

!!! exercise choice "Question"
    Qual é o resultado da seguinte conversão: `int("123")`?
    
    - [x] `123`
    - [ ] `"123"`
    - [ ] `12.3`
    - [ ] `None`

    !!! answer
        A conversão resulta no número inteiro `123`.

!!! exercise choice "Question"
    Se `x = 5.7`, qual é o valor de `int(x)`?
    
    - [x] `5`
    - [ ] `5.7`
    - [ ] `6`
    - [ ] `57`

    !!! answer
        O valor de `int(x)` é `5`.

!!! exercise choice "Question"
    Qual é o resultado da seguinte conversão: `float("123.45")`?
    
    - [ ] `123`
    - [x] `123.45`
    - [ ] `"123.45"`
    - [ ] `None`

    !!! answer
        A conversão resulta no número de ponto flutuante `123.45`.

!!! progress
    Continuar...


### Entrada e Saída

A interação com o usuário é fundamental para muitos programas. Python fornece funções simples para entrada e saída de dados. A função `input()` sempre retorna uma string, se queremos armazenar um valor numerico precisamos converter esse valor.

```python
nome_usuario = input("Qual é o seu nome? ")
print(f"Olá, {nome_usuario}!")
```


### Exercícios sobre Entrada e Saída

!!! exercise choice "Question"
    Qual função é usada em Python para obter entrada do usuário?
    
    - [x] `input()`
    - [ ] `print()`
    - [ ] `get()`
    - [ ] `read()`

    !!! answer
        A função `input()` é usada para obter entrada do usuário em Python.

!!! exercise choice "Question"
    Se usarmos o código `valor = input("Digite um número: ")`, e o usuário digitar `5`, qual será o tipo da variável `valor`?
    
    - [ ] `int`
    - [x] `str`
    - [ ] `float`
    - [ ] `bool`

    !!! answer
        Mesmo que o usuário digite um número, a função `input()` sempre retorna uma string. Portanto, o tipo da variável `valor` é `str`.

!!! exercise choice "Question"
    Qual é a saída do seguinte código: `print("Olá", "Mundo", sep="-")`?
    
    - [ ] `Olá Mundo`
    - [x] `Olá-Mundo`
    - [ ] `Olá, Mundo`
    - [ ] `OláMundo`

    !!! answer
        A saída do código é `Olá-Mundo` porque o argumento `sep` especifica o caractere usado para separar os valores.

!!! progress
    Continuar...


### Operadores

Os operadores são símbolos especiais que realizam operações em variáveis e valores.

#### Operadores Aritméticos

Os operadores aritméticos são usados para realizar operações matemáticas básicas. Eles seguem a ordem padrão de operações matemáticas.

| Operador | Significado       | Exemplo  |
|----------|-------------------|----------|
| +        | Adição            | a + b    |
| -        | Subtração         | a - b    |
| *        | Multiplicação     | a * b    |
| /        | Divisão           | a / b    |
| %        | Módulo            | a % b    |
| **       | Exponenciação     | a ** b   |
| //       | Divisão Inteira   | a // b   |

## Operadores Aritméticos

Os operadores aritméticos são usados para realizar operações matemáticas básicas. Durante o cálculo de uma expressão, o Python precisa decidir também o tipo do valor calculado.

Por exemplo, ao avaliar a expressão “5 * 3”, o Python tenta manter o tipo dos operandos. Neste caso, ambos os operandos são do tipo `int`, então o resultado é `15`, que também é do tipo `int`.

No entanto, a expressão “8 / 2” resulta em `4.0`, que é do tipo `float`. Isso ocorre porque a divisão em Python sempre retorna um número de ponto flutuante, mesmo que o resultado seja um número inteiro. Contudo, se usarmos o operador de divisão inteira `//`, o resultado será `4`, que é do tipo `int`.

```python
# Exemplos:
soma = 5 + 3  # 8
subtracao = 5 - 3  # 2
multiplicacao = 5 * 3  # Resultado: 15 (int)
divisao = 8 / 2  # Resultado: 4.0 (float)
divisao_inteira = 8 // 2 # Resultado: 4 (int)
```

Uma regra geral no Python é que, quando os operandos são de tipos distintos, como `int` e `float`, o operando de tipo "menor" é promovido ao tipo "maior" (ou mais abrangente, no caso o `float`). Assim, a operação é realizada no tipo mais abrangente.

A conversão entre tipos nativos do Python pode ser realizada usando funções com o nome do tipo desejado. Veja os exemplos abaixo:

```python
numero_float = float(4)         # Resultado: 4.0
numero_int = int(4.5)           # Resultado: 4
```

#### Operadores Relacionais

Os operadores relacionais são usados para comparar valores. Eles retornam um valor booleano (`True` ou `False`) com base na comparação.

| Operador | Significado               | Exemplo  |
|----------|---------------------------|----------|
| ==       | Igual a                   | a == b   |
| !=       | Diferente de              | a != b   |
| >        | Maior que                 | a > b    |
| <        | Menor que                 | a < b    |
| >=       | Maior ou igual a          | a >= b   |
| <=       | Menor ou igual a          | a <= b   |

```python
# Exemplos:
igual = (5 == 5)  # True
diferente = (5 != 3)  # True
menor = (3 < 5)  # True
maior = (5 > 3)  # True
```

#### Operadores Lógicos

Os operadores lógicos são usados para combinar múltiplas condições. Eles são fundamentais em estruturas de decisão e loops. Verdadeiro (V), Falso (F).

#### Operador `and` (E lógico)

| A | B | Resultado |
|---|---|-----------|
| V | V | V         |
| V | F | F         |
| F | V | F         |
| F | F | F         |

**Exemplo:** `a and b`

#### Operador `or` (OU lógico)

| A | B | Resultado |
|---|---|-----------|
| V | V | V         |
| V | F | V         |
| F | V | V         |
| F | F | F         |

**Exemplo:** `a or b`

#### Operador `not` (NÃO lógico, barrado, inversor)

| A | Resultado |
|---|-----------|
| V | F         |
| F | V         |

**Exemplo:** `not a`

```python
# Exemplos:
resultado1 = True and False  # False
resultado2 = True or False  # True
resultado3 = not True  # False
```

### Exercícios sobre Operadores

!!! exercise choice "Question"
    Qual é o resultado da seguinte operação: `10 % 3`?
    
    - [ ] `3`
    - [ ] `0`
    - [x] `1`
    - [ ] `10`

    !!! answer
        O resultado da operação `10 % 3` é `1`.

!!! exercise choice "Question"
    Se `x = 5` e `y = 3`, qual é o valor de `x ** y`?
    
    - [ ] `8`
    - [ ] `15`
    - [x] `125`
    - [ ] `2`

    !!! answer
        O valor de `x ** y` é `125`.

!!! exercise choice "Question"
    Qual é o resultado da seguinte expressão: `5 > 3 and 5 < 10`?
    
    - [x] `True`
    - [ ] `False`
    - [ ] `None`
    - [ ] `Error`

    !!! answer
        O resultado da expressão `5 > 3 and 5 < 10` é `True`.

!!! exercise choice "Question"
    Qual é o resultado da seguinte operação: `7 // 3`?
    
    - [x] `2`
    - [ ] `2.33`
    - [ ] `3`
    - [ ] `1`

    !!! answer
        O resultado da operação `7 // 3` é `2`, pois `//` é o operador de divisão inteira.

!!! exercise choice "Question"
    Dado `x = 10` e `y = 3`, qual é o valor de `x != y`?
    
    - [x] `True`
    - [ ] `False`
    - [ ] `None`
    - [ ] `Error`

    !!! answer
        A expressão `x != y` verifica se `x` é diferente de `y`. Como 10 é diferente de 3, o resultado é `True`.

!!! exercise choice "Question"
    Qual é o resultado da seguinte expressão: `not (5 <= 3)`?
    
    - [x] `True`
    - [ ] `False`
    - [ ] `None`
    - [ ] `Error`

    !!! answer
        A expressão `5 <= 3` é `False`, mas o operador `not` inverte o valor booleano. Portanto, o resultado é `True`.



!!! progress
    Continuar...

### Exercicios problema


!!! exercise "Question"
    Cálculo de Juros Compostos
    Você está planejando fazer um depósito em uma conta poupança que paga juros compostos mensalmente. Para ajudá-lo a entender quanto dinheiro você terá após um determinado período, você decide escrever um programa.
    
    Instruções:
    
    - O programa deve começar perguntando quanto você planeja depositar inicialmente.
    - Em seguida, o programa deve perguntar a taxa de juros anual (em porcentagem) que será paga.
    - Por fim, o programa deve perguntar por quantos anos o dinheiro ficará depositado.
    - O programa então calculará o montante final usando a fórmula de juros compostos e exibirá o resultado.
    
    - Fórmula de Juros Compostos:
    $$
    A = P(1 + \frac{r}{n})^{nt}
    $$
    
    Onde:
    
    - \( A \) é o valor futuro do investimento/empréstimo, incluindo juros.
    - \( P \) é o valor principal do investimento (depósito inicial ou valor do empréstimo).
    - \( r \) é a taxa de juro anual (em formato decimal).
    - \( n \) é o número de vezes que o juro é capitalizado por ano.
    - \( t \) é o número de anos que o dinheiro é investido ou emprestado.

    Teste o seu código com: 

        - Deposito inicial = 1000
        - taxa de juros = 5
        - tempo = 2
        - O resultado esperado é: 1104.94


    !!! answer
        Uma possivel solução é:
        ```python
        P = float(input("Quanto você planeja depositar inicialmente? "))
        r = float(input("Qual a taxa de juros anual (em porcentagem)? "))
        t = float(input("Por quantos anos o dinheiro ficará depositado? "))
        
        r = r/100 # Converte a taxa de juros de % para decimal dividindo por 100
        A = P * (1 + r/12)**(12*t) # equação de juros compostos
        A = round(A, 2) # arredonda o valor com 2 casas decimais
        print("Total após " + str(t) + " anos: " + str(A))
        ```


