# Laço `for` em Python

## Introdução

Já sabemos como o laço whille funciona, agora vamos conhecer uma nova estrutra de repetição. O laço `for` é uma das estruturas de controle mais versáteis em Python, permitindo iterar sobre sequências (coleções) e outros objetos iteráveis. Vamos conhecer em detalhes o funcionamento e as aplicações do laço `for`.

## Conceitos Básicos

Assim como o laço while, o for em Python é usado para criar um loop que percorre uma sequência de elementos, como uma lista, uma string ou um intervalo de números. Ele permite executar um bloco de código repetidamente para cada elemento da sequência.

### Sintaxe

A sintaxe básica do laço `for` é:

```python
for variavel in sequencia:
    # bloco de código
    # bloco de código
    # bloco de código

```
Na sintaxe do comando for, temos que:

- variavel: é uma variável que recebe cada elemento da lista em cada iteração do loop;
- sequencia: é a sequência de elementos a ser percorrida pelo loop, como uma lista, uma string ou um intervalo.



!!! exercise choice "Question"
    Qual das alternativas apresenta corretamente a sintaxe básica do laço `for` em Python?

    - [x] for variavel in sequencia:
              # bloco de código
    - [ ] for variavel; sequencia:
              # bloco de código
    - [ ] for variavel = sequencia:
              # bloco de código
    - [ ] for (variavel in sequencia):
              # bloco de código

    !!! answer
        A sintaxe correta do laço `for` em Python é `for variavel in sequencia:` seguido de um bloco de código indentado.


## Iterando sobre Sequências


Durante o loop for, o bloco de código é repetido para cada item da lista. A cada iteração, o elemento atual é atribuído à variável com base nesse elemento. O laço for pode iterar sobre qualquer objeto iterável em Python. As sequências mais comuns são listas, tuplas e strings.

listas

```python
números = [1, 2, 3, 4, 5]
for número in números:
    print(número)
```

Strings

```python
palavra = "Python"
for letra in palavra:
    print(letra)
```
Nesse exemplo a cada iteração é exibida um caractere da String.

```python
minha_lista = ["Pensamento", "computacional", "com", "Python"] 

for item in minha_lista:
    print(item)
```
Nesse exemplo a cada iteração do laço for um item da lista `minha_lista` é printado.

!!! exercise choice "Question"
    Qual das alternativas apresenta corretamente a iteração sobre uma string em Python?

    - [ ] for letra in "Python": print letra
    - [x] for letra in "Python": print(letra)
    - [ ] for "Python" as letra: print(letra)
    - [ ] for letra print("Python")

    !!! answer
        Para iterar sobre uma string em Python, usamos a sintaxe `for letra in "Python": print(letra)`.


## Função range()

A função `range()` é uma ferramenta poderosa quando combinada com o laço for, especialmente quando precisamos de uma sequência numérica. 

Ela é comumente usada em loops e iterações, permitindo especificar o início, o fim e o passo da sequência.

```python
range(início, fim, passo)

```

A função recebe até 3 parâmetros de entrada

- `start`: é o número de início da sequência (opcional). O valor padrão é `0`.
- `stop`: é o número final da sequência (`obrigatório`). O valor final não é incluído na sequência.
- `step`: é o valor de incremento entre os números da sequência (opcional). O valor padrão é 1.

```python
for i in range(5):
    print(i)

```
Neste exemplo o laço for vai iterar sobre a função range que gera valores inteiros de 0 até N-1.

```python

for x in range(10): 
    print(x) # x: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 


for x in range(3,10): 
    print(x) # x: 3, 4, 5, 6, 7, 8, 9 


for x in range(3,10,2): 
    print(x) # x: 3, 5, 7, 9 

```

!!! exercise choice "Question"
    Qual das alternativas apresenta corretamente a função `range()` para gerar uma sequência de 0 a 4?

    - [ ] range(0, 5, 2)
    - [ ] range(1, 5)
    - [x] range(5)
    - [ ] range(0, 4)

    !!! answer
        A função `range(5)` gera uma sequência de números de 0 a 4.


## Diferenças entre `while` e `for`

A principal distinção entre os loops while e for em Python está em como eles determinam as iterações:

O comando while permite repetir uma sequência de comandos enquanto uma condição específica for verdadeira. Por exemplo:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1

```
Neste exemplo, o bloco dentro do while será executado enquanto contador for menor que 5.

O comando for, por outro lado, é usado para iterar sobre elementos de um objeto iterável (como listas, tuplas, strings, dicionários, sets e outros). Por exemplo:

```python
for i in range(5):
    print(i)

```

Aqui, o loop for itera sobre cada número produzido pela função range(5).


!!! Tip
    É possível reescrever um loop for usando um loop while. Além disso, com criatividade e uso de funções auxiliares, também é possível reescrever um loop while usando um loop for. No entanto, a escolha entre eles deve ser baseada na clareza e legibilidade do código.



## Laços Aninhados

É possível ter um laço for dentro de outro, permitindo combinações mais complexas e sofisticadas em seu código. Ao aninhar loops, você pode executar um conjunto de instruções repetidamente dentro de outro conjunto de instruções repetidas.


```python
for i in range(3):
    for j in ["a", "b"]:
        print(i, j)

```

O loop externo (for i in range(3)) itera sobre os valores 0, 1 e 2. Para cada valor de i, o loop interno (for j in ["a", "b"]) itera sobre as letras "a" e "b". Isso resulta em cada combinação de i e j sendo impressa.

!!! exercise choice "Question"
    Qual das alternativas apresenta corretamente um laço `for` aninhado?

    - [ ] for i in range(3): print(i, j)
    - [ ] for i in range(3) for j in ["a", "b"]: print(i)
    - [x] for i in range(3):
              for j in ["a", "b"]:
                  print(i, j)
    - [ ] for i, j in range(3), ["a", "b"]: print(i, j)

    !!! answer
        Laços `for` aninhados são representados por um laço `for` dentro de outro, como no exemplo `for i in range(3): for j in ["a", "b"]: print(i, j)`.


### Exemplos

Multiplicação de Matrizes. Vamos supor que você queira multiplicar duas matrizes 2x2.

```python
def multiplica_matriz(A, B):
    # Inicializando a matriz resultante com zeros
    resultado = [[0, 0], [0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado

# Definindo as matrizes 2x2
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 3]]

C = multiplica_matriz(A, B)
print(C)

```


!!! exercise choice "Question"
    Qual das alternativas apresenta corretamente o resultado do exemplo acima?

    - [ ] [[1, 2], [3, 4]]
    - [ ] [[2, 0], [1, 3]]
    - [x] [[4, 6], [10, 12]]
    - [ ] [[6, 4], [10, 3]]

    !!! answer
        [[4, 6], [10, 12]]


Busca de Pares: Suponha que você tenha uma lista de números e queira encontrar todos os pares de números cuja soma seja 10:

```python
numeros = [1, 2, 3, 7, 4, 6, 5, 5, 9]
pares = []

for i in range(len(numeros)):
    for j in range(i+1, len(numeros)):
        if numeros[i] + numeros[j] == 10:
            pares.append((numeros[i], numeros[j]))

print(pares)
```
!!! exercise choice "Question"
    Qual das alternativas apresenta corretamente o resultado do exemplo acima?

    - [ ] [[1, 9], [3, 7], [4, 6], [5, 5]]
    - [ ] [1, 9, 3, 7, 4, 6, 5, 5]
    - [x] [(1, 9), (3, 7), (4, 6), (5, 5)]
    - [ ] [[1, 9, 3, 7, 4, 6, 5, 5]]

    !!! answer
        [(1, 9), (3, 7), (4, 6), (5, 5)] # lista de tuplas



## Compreensão de Listas

A compreensão de listas, ou list comprehension, é uma característica poderosa e expressiva da linguagem Python que permite a criação de listas de maneira concisa. Aqui está uma análise detalhada:

### Estrutura Básica:

A estrutura básica de uma compreensão de lista é:

```python
[expressão_de_saída for variável in iteravel]
```
onde:

- `expressão_de_saída`: A expressão que determina os valores que serão inseridos na lista resultante.
- `variável`: A variável temporária que assume cada valor no iterável.
- `iterável`: Qualquer objeto pelo qual se pode iterar (listas, tuplas, strings, etc.).

Exemplo

```python
quadrados = [x**2 for x in range(5)]
print(quadrados)
```
A compreensão da lista está criando uma lista dos quadrados dos números de 0 a 4. A saída seria: [0, 1, 4, 9, 16]


!!! exercise choice "Question"
    Qual das alternativas apresenta corretamente uma compreensão de lista para gerar os quadrados dos números de 0 a 4?

    - [ ] quadrados = [x for x in range(5)]
    - [ ] quadrados = [x, x**2 for x in range(5)]
    - [x] quadrados = [x**2 for x in range(5)]
    - [ ] quadrados = for x in range(5): x**2

    !!! answer
        A compreensão de lista correta é `quadrados = [x**2 for x in range(5)]`.

### Compreensão de Lista com Condição:

Uma compreensão de lista também pode incluir uma condição para filtrar quais elementos do iterável são processados:

```python
[expressão_de_saída for variável in iteravel  if condição]
```

Por exemplo, se quisermos apenas os quadrados dos números pares de 0 a 4:

```python
quadrados_pares = [x**2 for x in range(5) if x % 2 == 0]
print(quadrados_pares)

```

a saida seria: [0, 4, 16]

