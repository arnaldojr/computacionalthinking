
## Listas e Tuplas em Python

Python oferece uma variedade de estruturas de dados compostas usadas para agrupar outros valores. As mais versáteis são as `listas` e as `tuplas`, que podem ser compostas por itens de diferentes tipos.

!!! tip
    Tanto listas quanto tuplas são parte integrante da linguagem Python e são usadas em uma variedade de aplicações.


## Listas

Uma lista (`list`) uma lista é uma estrutura de dados que pode armazenar múltiplos itens (coleção de itens) em uma única variável (vetor). Em outras palavras, trata-se de uma sequência ordenada de objetos que podem ser acessados por meio de seu índice (`index`), um marcador de sua posição. 


### Criação de Listas

Em Python, as listas são delimitadas por colchetes (`[]`) e separadas por vigulas (`,`). Esses itens podem ser de qualquer tipo, incluindo números, strings e até outras listas


```python
números = [1, 2, 3, 4, 5]
nomes = ["Alice", "Bob", "Charlie"]
misturada = [1, "Alice", [2, 3, 4]]
frutas = ["maçã", "banana", "cereja"]  # exemplo de uma lista com 3 valores
```

!!! exercise choice "Question"
    Qual das alternativas apresenta corretamenta uma lista?
    
    - [x] numeros = [10, 20, 30, 40]
    - [ ] numeros = 10, 20, 30, 40
    - [ ] numeros = {10, 20, 30, 40}
    - [ ] numeros = (10, 20, 30, 40)

    !!! answer
        as listas são delimitadas por colchetes `[]` e separadas por vigulas `,`.



### Acesso a Elementos

Cada item em uma lista tem um índice, começando do zero. Você pode acessar itens individuais usando esse índice.

```python
print(frutas[1])  # Saída: banana
print(nomes[0])  # Saída: Alice
print(misturada[2][1])  # ATENCÃO nesta Saída: 3
```
!!! tip
    Em python assim como em outras linguagens de programação, começamos a contar o indice a partir de zero, isso significa que o valor da primeira posição da lista possui indice `0` (zero).


!!! exercise choice "Question"
    Dada a lista `numeros = [10, 20, 30, 40]`, qual é a saída de `print(numeros[0])`?

    - [x] `10`
    - [ ] `20`
    - [ ] `30`
    - [ ] `40`
    
    !!! answer
        A saída de `print(numeros[0])` é `10`, pois as listas em Python são indexadas a partir de 0.


!!! exercise choice "Question"
    Dada a lista `numeros = [10, 20, 30, 40]`, qual é a saída de `print(numeros[-1])`?

    - [ ] `10`
    - [ ] `20`
    - [ ] `30`
    - [x] `40`
    
    !!! answer
        A saída de `print(numeros[-1])` é `40`, pois em Python, índices negativos referem-se aos elementos da lista de trás para frente.

!!! exercise choice "Questão 2"
    Dado a lista `frutas = ["maçã", "banana", "cereja"]`, qual é a saída de `print(frutas[1])`?
    
    - [ ] `maçã`
    - [x] `banana`
    - [ ] `cereja`
    - [ ] `frutas`
    
    !!! answer
        A saída de `print(frutas[1])` é `banana`, pois as listas em Python são indexadas a partir de 0.
    


!!! progress
    Continuar...


Quando criamos uma lista em Python, além de poder manipular essa estrutura pelo seu indice, ela já vem equipada com diversos métodos predefinidos que nos ajudam a operar e manipular essa estrutura de forma mais facil, vamos ver alguns deles.

### Adição, Remoção e Alteração de Elementos

Listas são estruturas de dados `mutáveis`, o que significa dizer que podemos alterar (editar), adicionar (expandir) e remover (reduzir) itens após a lista ser criada.

#### Adicionar

Método para adicionar item a uma lista

    - append(): Adiciona um item ao final da lista.
    - insert(): Insere um item em uma posição específica.

```python
frutas = ["maçã", "banana"]

frutas.append("uva")
frutas.insert(1, "laranja")
```

!!! exercise choice "Question"
    Qual dos seguintes é um método válido para adicionar um elemento ao final de uma lista em Python?

    - [x] `append()`
    - [ ] `add()`
    - [ ] `insertend()`
    - [ ] `put()`
    
    !!! answer
        O método `append()` é o método válido para adicionar um elemento ao final de uma lista em Python.

!!! exercise choice "Question"
    Dado o código Python a seguir, qual é a saída de `print(frutas)`?Qual dos seguintes métodos remove o último item de uma lista?
    
    ```python
    numeros = []
    soma = 0
    n = 1
    
    while soma <= 100:
        numeros.append(n)
        soma += n
        n += 1
    
    print(f"Números na lista: {numeros}")
    ```
    
    - [ ] `Números na lista: soma, n, numeros`
    - [x] `Números na lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
    - [ ] `Números na lista: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]`
    - [ ] `Números na lista: [[...], [...], [...], [...], [...], [...], [...], [...], [...], [...], [...], [...], [...], [...]]`
    
    !!! answer
        O código cria uma lista vazia e armazena os valores do contador `n` na lista numeros até o valor da soma ser maior ou igual a 100. Números na lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#### Remoção

Método para remoção de item da lista:

    - remove(): Remove o primeiro item com o valor especificado.
    - pop(): Remove o item em um índice específico (ou o último item se o índice não for especificado).
    - clear(): Limpa todos os itens da lista.

```python
frutas.remove("banana")
frutas.pop()
frutas.clear()
```
!!! exercise choice "Question"
    Qual dos seguintes métodos remove o último item de uma lista?
    
    - [ ] `delete()`
    - [x] `pop()`
    - [ ] `removeend()`
    - [ ] `discard()`
    
    !!! answer
        O método `pop()` remove e retorna o último item de uma lista se nenhum índice for especificado.

#### Alteração

Você pode alterar um item referenciando seu índice.

```python
frutas[0] = "manga"
```
!!! exercise choice "Question"
    Dada a lista `animais = ["cachorro", "gato", "peixe", "pássaro"]`, qual das opções a seguir irá substituir "peixe" por "hamster"?

    - [x] 
        ```python
        animais[2] = "hamster"
        ```
    - [ ] 
        ```python
        animais.replace("peixe", "hamster")
        ```
    - [ ] 
        ```python
        animais[3] = "hamster"
        ```
    - [ ] 
        ```python
        animais.insert(2, "hamster")
        ```

!!! answer
    A opção que substitui o item "peixe" por "hamster" na lista é `animais[2] = "hamster"`. Em Python, as listas são indexadas a partir de 0, então o índice 2 corresponde ao terceiro item da lista.


### Métodos mais utilizados de Listas

Alguns dos métodos mais utilizados são:
 
    - len(): Retorna o número de itens em uma lista.
    - extend(): Adiciona elementos de outra lista (ou qualquer iterável) ao final da lista atual.
    - index(): Retorna o índice do primeiro item com o valor especificado.
    - count(): Retorna o número de vezes que um valor aparece na lista.
    - sort(): Ordena a lista.
    - reverse(): Inverte a ordem da lista.

!!! exercise choice "Question"
    Dada a lista `numeros = [2, 5, 8, 1, 7]`, qual será a saída do código `print(len(numeros))`?

    - [ ] `2`
    - [x] `5`
    - [ ] `8`
    - [ ] `1`

    !!! answer
        A saída será `5`, pois o método `len()` retorna o número de itens na lista.

!!! exercise choice "Question"
    Se temos `listaA = [1, 2, 3]` e `listaB = [4, 5, 6]`, e executamos `listaA.extend(listaB)`, qual será o valor de `listaA`?

    - [ ] `[1, 2, 3]`
    - [ ] `[4, 5, 6]`
    - [x] `[1, 2, 3, 4, 5, 6]`
    - [ ] `[1, 2, 3, [4, 5, 6]]`

    !!! answer
        O valor de `listaA` será `[1, 2, 3, 4, 5, 6]` após o uso do método `extend()`.


!!! exercise choice "Question"
    Dada a lista `cores = ["verde", "azul", "vermelho"]`, qual será a saída de `print(cores.index("azul"))`?

    - [ ] `0`
    - [x] `1`
    - [ ] `2`
    - [ ] `3`

    !!! answer
        A saída será `1`, pois o método `index()` retorna o índice do primeiro item com o valor especificado.

!!! exercise choice "Question"
    Na lista `letras = ['a', 'b', 'c', 'a', 'a', 'b']`, qual será a saída de `print(letras.count('a'))`?

    - [ ] `1`
    - [ ] `2`
    - [x] `3`
    - [ ] `4`
    
    !!! answer
        A saída será `3`, pois o método `count()` retorna o número de vezes que o valor 'a' aparece na lista.

!!! exercise choice "Question"
    Dada a lista `valores = [3, 1, 4, 1, 5, 9, 2]`, após executar `valores.sort()`, qual será o primeiro elemento da lista?

    - [x] `1`
    - [ ] `2`
    - [ ] `3`
    - [ ] `4`

    !!! answer
        Após ordenar a lista, o primeiro elemento será `1`.
    
!!! exercise choice "Question"
    Se temos a lista `ordem = [1, 2, 3, 4]` e executamos `ordem.reverse()`, qual será o valor de `ordem`?

    - [ ] `[1, 2, 3, 4]`
    - [ ] `[4, 3, 2, 1, 0]`
    - [x] `[4, 3, 2, 1]`
    - [ ] `[1, 0, 4, 3]`

    !!! answer
        Após a execução do método `reverse()`, a lista `ordem` terá os elementos na ordem `[4, 3, 2, 1]`.

Teste o código a seguir:

```python
# definimos uma lista de listas (com nome, senha e cargo de usuários)
usuarios = [
    ['alberto', '1234'],
    ['mario', '6282'],
    ['maria', '5274'],
    ['joana', '9943']
]

nome = input('Nome do usuário: ')
pin = input('Código PIN: ')

# Verificando se a combinação nome e PIN está na lista de usuários
usuario_encontrado = [nome, pin] in usuarios

if usuario_encontrado:
    msg = f'Acesso liberado'
else:
    msg = 'Acesso negado'

print(msg)
```
Neste código estamos usando a expressão [nome, pin] in usuarios para verificar se a combinação de nome e PIN existe na lista usuarios. Esta expressão retornará True se a combinação for encontrada e False caso contrário.

    
!!! progress
    Continuar...




### Fatiamento (slices)

Além de acessar elementos da lista por meio de índices, podemos realizar o fatiamento de listas. O fatiamento é uma operação que permite extrair uma sublista de uma lista. A sintaxe de fatiamento é representada por colchetes `[]` e dois pontos `:`.

A notação básica do fatiamento é: `lista[início:fim]`, onde:

- início: é o índice inicial do fatiamento (inclusivo).
- fim: é o índice final do fatiamento (exclusivo).

Por exemplo, lista[1:4] retorna uma sublista que começa no índice 1 e vai até (mas não inclui) o índice 4.

A notação [:] pode ser expandida para incluir um terceiro parâmetro, `o passo`, usando a sintaxe `lista[início:fim:passo]`:

- passo: especifica a "distância" entre os índices. Por exemplo, um passo de 2 pula um índice entre cada item incluído na sublista.

A notação [:] por si só cria uma cópia superficial da lista original. Isso significa que você obtém uma nova lista com os mesmos elementos, mas é uma lista diferente em termos de identidade (ou seja, está armazenada em um local diferente da memória).

Alguns exemplos comuns incluem:

lista[::2]: retorna todos os elementos em índices pares.
lista[::-1]: inverte a lista.
lista[1:5:2]: retorna os elementos nos índices 1 e 3 (começa no índice 1, termina antes do índice 5, com um passo de 2).

```python
números = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_lista = números[2:7]  # [2, 3, 4, 5, 6]
```
!!! exercise choice "Question"
    Dada a lista `numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, qual fatiamento retorna `[2, 3, 4, 5]`?

    - [ ] `numeros[2:5]`
    - [x] `numeros[2:6]`
    - [ ] `numeros[3:6]`
    - [ ] `numeros[2:7:2]`

    !!! answer
        O fatiamento `numeros[2:6]` retorna a sublista `[2, 3, 4, 5]`.
    

!!! exercise choice "Question"
    Dada a lista `numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, qual fatiamento retorna todos os números pares da lista?

    - [ ] `numeros[::2]`
    - [ ] `numeros[1::2]`
    - [x] `numeros[0::2]`
    - [ ] `numeros[::-2]`
    
    !!! answer
        O fatiamento `numeros[0::2]` retorna todos os números em índices pares, ou seja, `[0, 2, 4, 6, 8]`.


!!! exercise choice "Question"
    Em `numeros[2:8:2]`, qual é o propósito do último `2`?

    - [ ] Indica o início do fatiamento.
    - [ ] Indica o fim do fatiamento.
    - [x] Especifica o passo do fatiamento, ou seja, a "distância" entre os índices.
    - [ ] Dobra os valores no intervalo especificado.
    
    !!! answer
        No fatiamento `numeros[2:8:2]`, o último `2` especifica o passo, ou seja, a "distância" entre os índices. Isso resultaria na sublista `[2, 4, 6]`.

juntando as coisas, varrendo uma lista com while.

```python 
primos = [2, 3, 5, 7, 11]
i = 0
while i < len(primos):
    print( "elemento de indice %d = %d"%(i, primos[i]) )
    i = i + 1
```
!!! progress
    Continuar...


### Tuplas

Tuplas são uma estrutura de dados em Python semelhante às listas. No entanto, enquanto as listas são mutáveis (ou seja, podem ser alteradas após a criação), as tuplas são `imutáveis`. Isso significa que, uma vez que uma tupla é criada, seus elementos não podem ser modificados, adicionados ou removidos.

!!! tip
    A principal diferença entre listas e tuplas é que listas são mutáveis, enquanto tuplas são imutáveis.


#### Definindo Tuplas

Uma tupla é definida colocando-se uma sequência de valores separados por vírgulas entre parênteses `()`:

```python
tupla_exemplo = (1, 2, 3, 4, 5)
print(tupla_exemplo)  # Saída: (1, 2, 3, 4, 5)
```

É possível definir uma tupla sem parênteses, usando apenas vírgulas:

```python
tupla_simples = 1, 2, 3
print(tupla_simples)  # Saída: (1, 2, 3)

```

Para tuplas com um único elemento, é necessário incluir uma vírgula após o elemento:

```python
tupla_simples = 1,
print(tupla_simples)  # Saída: (1,)

```
!!! exercise choice "Question"
    Qual das opções a seguir define corretamente uma tupla com os elementos 5, 10 e 15?

    - [ ] `tupla = 5; 10; 15`
    - [ ] `tupla = [5, 10, 15]`
    - [x] `tupla = (5, 10, 15)`
    - [ ] `tupla = {5, 10, 15}`

    !!! answer
        A opção correta é `tupla = (5, 10, 15)`.
    

#### Acessando Elementos de Tuplas

Assim como as listas, as tuplas são ordenadas e indexadas. Você pode acessar elementos de uma tupla usando índices:

```python
tupla = (10, 20, 30, 40, 50)
print(tupla[1])  # Saída: 20

```

!!! exercise choice "Question"
    Dada a tupla `cores = ("vermelho", "verde", "azul")`, qual é o resultado de `cores[1]`?

    - [ ] `"vermelho"`
    - [x] `"verde"`
    - [ ] `"azul"`
    - [ ] `TypeError`
    
    !!! answer
        O resultado de `cores[1]` é `"verde"`.
    


#### Imutabilidade das Tuplas

A principal característica das tuplas é sua imutabilidade:


```python
tupla = (1, 2, 3)
# tupla[1] = 4  # Isso causará um TypeError

```

Mesmo que você não possa modificar os elementos de uma tupla após sua criação, você pode concatenar ou repetir tuplas para formar novas tuplas:

```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)  # Saída: (1, 2, 3, 4, 5, 6)
```

!!! exercise choice "Question"
    O que acontece se tentarmos modificar um elemento de uma tupla existente, como `tupla[0] = 100`?

    - [ ] A tupla é modificada com sucesso.
    - [ ] A tupla é recriada com o novo valor.
    - [x] Um `TypeError` é lançado.
    - [ ] O programa encerra sem erros.

    !!! answer
        Um `TypeError` é lançado porque as tuplas são imutáveis.
    

#### Fatiamento em Tuplas

Assim como as listas, as tuplas também suportam operações de fatiamento:


```python
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
fatiado = tupla[2:6]
print(fatiado)  # Saída: (2, 3, 4, 5)

```

!!! exercise choice "Question"
    Dada a tupla `numeros = (0, 1, 2, 3, 4, 5)`, qual é o resultado de `numeros[1:4]`?

    - [ ] `(0, 1, 2)`
    - [x] `(1, 2, 3)`
    - [ ] `(2, 3, 4)`
    - [ ] `(1, 2, 3, 4)`
    
    !!! answer
        O resultado de `numeros[1:4]` é `(1, 2, 3)`.


#### Funções com Tuplas

Várias funções que funcionam com listas também são aplicáveis às tuplas:

- len(tupla): Retorna o número de itens na tupla.
- min(tupla): Retorna o menor item da tupla.
- max(tupla): Retorna o maior item da tupla.

!!! exercise choice "Question"
    Qual é o resultado da função `max()` aplicada à tupla `(5, 3, 8, 1)`?

    - [ ] `1`
    - [ ] `3`
    - [ ] `5`
    - [x] `8`

    !!! answer
        O resultado da função `max()` aplicada à tupla `(5, 3, 8, 1)` é `8`.
    


#### Por que usar Tuplas?

Você pode se perguntar: "Por que usar tuplas se as listas são mais flexíveis?". Em geral, as tuplas são usadas em situações onde a imutabilidade é necessária ou benéfica. Por exemplo, tuplas podem ser usadas como chaves em dicionários (veremos isso em breve no curso    ), enquanto listas não podem. Além disso, as tuplas, por serem imutáveis, podem ser mais seguras para certos tipos de operações onde não queremos que os dados sejam alterados acidentalmente.



--------para testar --------


<iframe title="Lista" width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=uma_lista%20%3D%20%20%5B%22ola%22,%202.0,%205,%20%5B10,%2020%5D%5D%0Aprint%28len%28uma_lista%29%29%0Aprint%28len%28%5B'spam!',%201,%20%5B'Brie',%20'Roquefort',%20'Pol%20le%20Veq'%5D,%20%5B1,%202,%203%5D%5D%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=3&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>