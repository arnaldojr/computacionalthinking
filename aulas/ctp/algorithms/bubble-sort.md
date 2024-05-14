### bubble sort

Dentre os algoritmos de ordenação, o Bubble Sort é sem dúvida um dos mais simples de implementar. Também conhecido como ordenação por trocas ou flutuação, sua simplicidade vem com um custo: uma eficiência geralmente inferior quando comparado a outros métodos de ordenação. A complexidade de tempo do Bubble Sort é O(n²), o que significa que para grandes conjuntos de dados, pode não ser a escolha mais eficiente.

### Funcionamento do Algoritmo

O Bubble Sort trabalha repetidamente passando pela lista a ser ordenada, comparando cada par de elementos adjacentes e trocando-os de posição se estiverem na ordem errada. Esse processo se repete até que nenhuma troca seja necessária, o que indica que a lista está ordenada. O algoritmo recebe esse nome porque os elementos maiores "borbulham" para o final da lista a cada passagem, enquanto os menores "afundam" para o início.


![](https://panda.ime.usp.br/panda/static/pythonds_pt/_images/bubblepass.png)


### Bubble Sort em ação

Para visualizar o algoritmo em ação utilize o link a seguir:

[https://visualgo.net/en/sorting?slide=10](https://visualgo.net/en/sorting?slide=10)



### Implementação em Python

Aqui está uma implementação simples do Bubble Sort em Python:

```python 

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] ## troca de posição
    return lista

```

Neste caso, como exemplo:

```python

lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = bubble_sort(lista)
print("Lista Ordenada:", lista_ordenada)

```

### Intuição da Análise de Complexidade

- Complexidade de Tempo: O Bubble Sort tem uma complexidade de tempo quadrática O(n²), onde n é o número de elementos na lista. Isso ocorre porque ele precisa fazer duas passagens aninhadas sobre a lista para garantir que ela esteja ordenada.

- Complexidade de Espaço: A complexidade de espaço é O(1), pois requer apenas uma quantidade constante de espaço de memória adicional além da lista de entrada.


!!! exercise choice "Exercício de Ordenação"
    Suponha que você tenha a seguinte lista de números para ordenar: `[19, 1, 9, 7, 3, 10, 13, 15, 8, 12]` qual lista representa a lista parcialmente ordenada depois de três passagens completas do bubble sort?


    - [ ] [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
    - [x] [1, 3, 7, 9, 10, 8, 12, 13, 15, 19]
    - [ ] [1, 7, 3, 9, 10, 13, 8, 12, 15, 19]
    - [ ] [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]

    !!! answer
        A lista parcialmente ordenada depois de três passagens completas do bubble sort é B. `[1, 3, 7, 9, 10, 8, 12, 13, 15, 19]`.


Referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OBubbleSort.html
