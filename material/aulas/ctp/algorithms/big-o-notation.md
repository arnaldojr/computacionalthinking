## bntrodução à Notação Big O

A notação Big O é uma maneira de expressar a eficiência de um algoritmo em termos de seu tempo de execução ou espaço utilizado, em função do tamanho da entrada. É uma ferramenta fundamental na análise de algoritmos, pois permite comparar a eficiência de diferentes abordagens sem se preocupar com as diferenças específicas de hardware ou linguagem de programação.

### Intuição por trás da Notação Big O

Imagine que você tenha uma biblioteca com milhares de livros e precise encontrar um livro específico. Se os livros estiverem desorganizados, você terá que olhar cada livro um por um até encontrar o que procura. Esse processo é ineficiente e o tempo que leva para encontrar o livro aumenta à medida que o número de livros aumenta. Agora, imagine que os livros estão organizados alfabeticamente. Nesse caso, você pode usar uma busca binária para encontrar o livro, o que é muito mais rápido. A notação Big O nos ajuda a quantificar essa diferença de eficiência.

### Definição Formal

A notação Big O descreve o limite superior do tempo de execução de um algoritmo em termos do tamanho da entrada. Por exemplo, um algoritmo com tempo de execução O(n) significa que o tempo para executar o algoritmo aumenta linearmente com o tamanho da entrada n. Da mesma forma, um algoritmo O(n²) significa que o tempo de execução aumenta proporcionalmente ao quadrado do tamanho da entrada.

### Exemplos Comuns de Notação Big O

- `O(1)`: Tempo constante - O tempo de execução não depende do tamanho da entrada.
- `O(log n)`: Tempo logarítmico - O tempo de execução aumenta logaritmicamente com o tamanho da entrada.
- `O(n)`: Tempo linear - O tempo de execução aumenta linearmente com o tamanho da entrada.
- `O(n log n)`: Tempo log-linear - Comum em algoritmos de ordenação eficientes como o quicksort.
- `O(n²)`: Tempo quadrático - O tempo de execução aumenta proporcionalmente ao quadrado do tamanho da entrada. Comum em algoritmos de ordenação menos eficientes, como o bubble sort.

### Exemplos de Complexidades de Tempo

- `O(1)`: Tempo constante

Exemplo: Acessar um elemento em um array.

```python
def acessar_elemento(array, indice):
    return array[indice]
```
Explicação: O tempo de execução não muda, independentemente do tamanho do array, pois estamos acessando diretamente um elemento específico.

- `O(log n)`: Tempo logarítmico

Exemplo: Busca binária em um array ordenado.

```python
def busca_binaria(array, elemento):
    inicio = 0
    fim = len(array) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if array[meio] == elemento:
            return meio
        elif array[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
```

Explicação: A cada iteração, o algoritmo divide o espaço de busca pela metade, resultando em um tempo de execução logarítmico.

- `O(n)`: Tempo linear

Exemplo: Encontrar o valor máximo em um array.

```python
def encontrar_maximo(array):
    maximo = array[0]
    for elemento in array:
        if elemento > maximo:
            maximo = elemento
    return maximo
```

Explicação: O algoritmo percorre cada elemento do array uma vez para encontrar o máximo, portanto, o tempo de execução aumenta linearmente com o tamanho do array.

- `O(n log n)`: Tempo log-linear

Exemplo: Algoritmo de ordenação Merge Sort.

```python
def merge_sort_iterativo(array):
    if len(array) > 1:
        meio = len(array) // 2
        esquerda = array[:meio]
        direita = array[meio:]
        merge_sort(esquerda)
        merge_sort(direita)
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1
            else:
                array[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1
```

Explicação: O Merge Sort divide o array pela metade em cada nível de recursão (log n) e depois combina os elementos ordenadamente (n), resultando em um tempo de execução O(n log n).

- `O(n²)`: Tempo quadrático

Exemplo: Algoritmo de ordenação Bubble Sort.

```python
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
```

Explicação: O Bubble Sort compara cada par de elementos adjacentes e os troca se estiverem na ordem errada, repetindo esse processo para cada elemento do array, resultando em um tempo de execução que aumenta proporcionalmente ao quadrado do tamanho do array.



### Regras para Análise de Complexidade

Uma forma simples de determinar a complexidade é pela soma das complexidades de todos os fragmentos de código que o compõem. Para analisar a complexidade de um algoritmo, precisamos entender a complexidade de cada bloco de código individual e depois combiná-las para obter a complexidade total. Abaixo, apresentamos exemplos de complexidades de trechos de código simples e mostramos como elas são utilizadas para calcular a complexidade de uma função completa.

- `Sentenças Simples`: Essas sentenças têm complexidade constante, ou seja, O(1).

```python
# Exemplo de sentenças simples
s = "Brasil"
i = 42
i += 1
```

- `Laços Simples`: Laços que percorrem a entrada uma vez têm complexidade linear em relação ao tamanho da entrada, ou seja, O(n), onde n é o tamanho da entrada.

```python
# Exemplo de laço simples
for i in range(n):
    # Sentenças simples

```
- `Laços Aninhados`: Laços aninhados resultam em uma complexidade quadrática em relação ao tamanho da entrada, ou seja, O(n²), onde n é o tamanho da entrada.

```python
# Exemplo de laços aninhados
for i in range(n):
    for j in range(n):
        # Sentenças simples
```

### Comparação Visual das Complexidades de Tempo

A imagem abaixo mostra uma comparação gráfica das diferentes complexidades de tempo discutidas. Ela ilustra como o tempo de execução cresce com o aumento do tamanho da entrada (n) para cada complexidade.

![](https://algoritmosempython.com.br/images/algoritmos-python/analise-complexidade/ModeloCustos.png)


### Importância na Análise de Algoritmos

Entender a notação Big O é crucial para avaliar a eficiência de um algoritmo. Isso ajuda a identificar gargalos e a escolher o algoritmo mais adequado para um determinado problema, especialmente à medida que o tamanho da entrada aumenta. Na prática, isso pode significar a diferença entre um programa que executa em segundos e um que leva horas.


## Exercicios

!!! exercise
    Análise de Algoritmos: Dado o seguinte algoritmo, determine sua complexidade de tempo usando a notação Big O.

    ```python
    def soma_elementos(lista):
        soma = 0
        for elemento in lista:
            soma += elemento
        return soma
    ```
    !!! answer
        Complexidade O(n). Isso ocorre porque o algoritmo percorre cada elemento da lista uma vez para somá-los.    


!!! exercise
    Comparação de Algoritmos: Considere dois algoritmos de ordenação, um com complexidade O(n log n) e outro com O(n²). Como o tempo de execução de cada algoritmo cresce com o aumento do tamanho da entrada?

    !!! answer
        Para um algoritmo de ordenação com complexidade O(n log n), o tempo de execução aumenta de forma log-linear com o tamanho da entrada. Isso significa que, para entradas grandes, o tempo de execução cresce mais devagar do que para um algoritmo com complexidade O(n²), onde o tempo de execução aumenta proporcionalmente ao quadrado do tamanho da entrada. Portanto, para entradas grandes, o algoritmo O(n log n) será geralmente mais rápido que o algoritmo O(n²).

!!! exercise
    Aplicação Prática: Dada uma lista de números desordenada, qual algoritmo de ordenação você escolheria para ordená-la? Justifique sua escolha com base na notação Big O.

    !!! answer
        Para ordenar uma lista de números desordenada, seria preferível escolher um algoritmo de ordenação com complexidade O(n log n), como o quicksort ou o mergesort, em vez de um algoritmo com complexidade O(n²), como o bubble sort ou o insertion sort. Isso se deve ao fato de que, para listas grandes, algoritmos O(n log n) tendem a ser mais rápidos e eficientes.


### referencias

- https://pt.wikipedia.org/wiki/Grande-O
- https://algoritmosempython.com.br/cursos/algoritmos-python/analise-complexidade/modelo-custos/
- https://www.freecodecamp.org/portuguese/news/o-que-e-a-notacao-big-o-complexidade-de-tempo-e-de-espaco/
- https://www.alura.com.br/artigos/como-classificar-algoritmos-big-o-notation