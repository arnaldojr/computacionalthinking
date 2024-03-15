### Quick Sort

O Quick Sort é um algoritmo de ordenação eficiente, `rápido` baseado na `técnica de divisão e conquista`.

É conhecido por sua capacidade de ordenar rapidamente grandes conjuntos de dados. 

A complexidade de tempo média do Quick Sort é O(n log n), onde n é o número de elementos na lista. No 

### Funcionamento do Algoritmo

- `Escolha do Pivô`: Selecione um elemento da lista para ser o pivô. A escolha do pivô pode afetar significativamente o desempenho do algoritmo.
- `Partição`: Reorganize a lista de forma que todos os elementos menores que o pivô fiquem à esquerda dele, e todos os elementos maiores fiquem à direita.
- `Recursão`: Aplique o Quick Sort recursivamente às duas sublistas divididas pelo pivô.


![](https://cdn.kastatic.org/ka-perseus-images/9876d4dc59e01a4742860ae1831c20f654ed7959.png)


### Quick Sort em ação

Para visualizar o algoritmo em ação, utilize o link a seguir:

[https://visualgo.net/en/sorting?slide=9](https://visualgo.net/en/sorting?slide=9)


### Implementação em Python

Aqui está uma implementação simples do Merge Sort em Python:

```python
def quickSort(alist):
    quicksort(alist, 0, len(alist) - 1)

def quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = dividir(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1)
        quicksort(lista, pivo + 1, fim)

def dividir(lista, inicio, fim):
    pivo = lista[fim]
    posicao_pivo = inicio
    for i in range(inicio, fim):
        if lista[i] < pivo:
            lista[i], lista[posicao_pivo] = lista[posicao_pivo], lista[i]
            posicao_pivo += 1
    lista[posicao_pivo], lista[fim] = lista[fim], lista[posicao_pivo]
    return posicao_pivo
```

Neste caso, como exemplo:

```python
# Testa o algoritmo.
lista = [13, 30, 17, -1, -2, 27, 3]
quickSort(lista)
print("Lista ordenada:", lista)
```

### Intuição da Análise de Complexidade

- Complexidade de Tempo: A complexidade de tempo média do Quick Sort é O(n log n), tornando-o eficiente para grandes listas. No entanto, no pior caso, pode ser O(n²), especialmente se o pivô for escolhido de forma inadequada.

- Complexidade de Espaço: A complexidade de espaço é O(log n) devido à pilha de chamadas de recursão.


!!! exercise
    Rode o código quick-sort utilizando o python tutor. (https://pythontutor.com/)[https://pythontutor.com/]. Execute o código passo a passo compare a complexidade de espaço de memória com o bubble-sort. Ele ocupa mais ou menos espaço de memoria?


!!! exercise
    Escreva uma função recursiva baseada no método do quick-sort que ordene de forma decrescente um vetor aleatório de 15 posições. 


!!! progress
    continuar...


Algumas referências: 

    - https://panda.ime.usp.br/algoritmos/static/algoritmos/20-divisao-e-conquista.html#dividir-para-conquistar
    
    - https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/mergesort/

    - https://algs4.cs.princeton.edu/22mergesort/
