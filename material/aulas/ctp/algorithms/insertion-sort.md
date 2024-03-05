### Insertion sort

O Insertion Sort é um algoritmo de ordenação simples que constrói a lista ordenada um elemento de cada vez. Ele é muito semelhante ao modo como as pessoas ordenam cartas em suas mãos durante um jogo de cartas, inserindo cada carta na posição correta entre as cartas já ordenadas.


### Funcionamento do Algoritmo

O algoritmo divide a lista de entrada em duas partes: a sublista de itens já ordenados, que é construída da esquerda para a direita na frente da lista, e a sublista de itens restantes a serem ordenados que ocupam o resto da lista. O algoritmo funciona repetidamente pegando cada elemento da parte não ordenada e inserindo-o na posição correta na parte ordenada.


![](https://panda.ime.usp.br/panda/static/pythonds_pt/_images/insertionsort.png)



<iframe sandbox="allow-popups allow-same-origin allow-scripts allow-top-navigation" src="https://pt.khanacademy.org/computer-programming/program/6529933716258816/embedded?embed=yes&amp;author=no&amp;editor=no&amp;width=688&amp;buttons=no&amp;settings=%7B%7D" class="perseus-scratchpad" allowfullscreen="" style="height: 400px; width: 100%;"></iframe>


### Insertion Sort em ação

Para visualizar o algoritmo em ação utilize o link a seguir:

![](https://visualgo.net/en/sorting)



### Implementação em Python

Aqui está uma implementação simples do Selection Sort em Python:

```python 
def insertion_sort(lista):
    n = len(lista)
    # Percorre a lista.
    for j in range(1, n):
        chave = lista[j]
        i = j - 1
        # Insere o elemento lista[j] na posição correta.
        while i >= 0 and lista[i] > chave:
            lista[i + 1] = lista[i]
            i = i - 1
        lista[i + 1] = chave

    return lista

```

Neste caso, como exemplo:

```python
lista = [12, 11, 13, 5, 6]
lista_ordenada = insertion_sort(lista)
print("Lista Ordenada:", lista_ordenada)

```

### Intuição da Análise de Complexidade

- Complexidade de Tempo: O Insertion Sort tem uma complexidade de tempo quadrática O(n²), onde n é o número de elementos na lista. No entanto, para listas pequenas ou parcialmente ordenadas, o algoritmo pode ser muito eficiente.

- Complexidade de Espaço: A complexidade de espaço é O(1), pois requer apenas uma quantidade constante de espaço de memória adicional além da lista de entrada.

!!! exercise choice "Exercício de Ordenação"
    Suponha que você tenha a seguinte lista de números para ordenar: `[15, 5, 4, 18, 12, 19, 14, 10, 8, 20]` qual lista representa a lista parcialmente ordenada depois três passagens completas da ordenação por inserção?

    - [ ] [4, 5, 12, 15, 14, 10, 8, 18, 19, 20]
    - [ ] [15, 5, 4, 10, 12, 8, 14, 18, 19, 20]
    - [x] [4, 5, 15, 18, 12, 19, 14, 10, 8, 20]
    - [ ] [15, 5, 4, 18, 12, 19, 14, 8, 10, 20]

!!! answer
    A lista parcialmente ordenada depois de três passagens insersão. `[4, 5, 12, 15, 14, 10, 8, 18, 19, 20]`.


Referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/AOrdenacaoPorInsercao.html
