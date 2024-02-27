
A `busca sequencial` ou como tambem é conhecida `busca linear`, é um método simples para encontrar um valor específico em uma lista. Ele funciona iterando através de cada elemento da lista, um por um, até encontrar o valor desejado.

![](https://algoritmosempython.com.br/images/algoritmos-python/pesquisa-ordenacao/PesquisaLinear.gif)


**Simplicidade**: Uma das principais vantagens da busca sequencial é a sua simplicidade. Ela não requer que os dados estejam ordenados.

**Eficiência**: Não é o método mais eficiente para encontrar um elemento em uma lista. Ela tem uma complexidade de tempo de O(n), o que significa que, no pior caso, ela precisa percorrer todos os n elementos da lista para encontrar o elemento desejado. No entanto, para listas pequenas ou quando a distribuição dos dados é desconhecida, a busca sequencial pode ser uma boa escolha.

**Uso de memória**: Não requer memória adicional, ao contrário de alguns outros algoritmos de busca e ordenação que precisam de espaço extra para funcionar.

**Aplicações**: A busca sequencial é útil em aplicações onde os dados não estão ordenados e a eficiência não é uma preocupação primordial. Ela também é útil quando a lista é atualizada frequentemente, pois outros métodos de busca que requerem dados ordenados precisariam reordenar a lista cada vez que um elemento é adicionado ou removido.

### Exemplo de implementação passo a passo de uma busca sequencial:

1. Defina a lista de valores e o valor que você está procurando.

```python
lista = [1, 3, 5, 7, 9]
valor_procurado = 5
```

2. Crie uma função para realizar a busca sequencial. A função deve percorrer cada elemento da lista. Se o elemento atual for igual ao valor procurado, a função deve retornar o índice desse elemento. Se o valor não for encontrado, a função deve retornar -1.

Podemos fazer de diversas formas, tais como: 


```python
def busca_sequencial(lista, valor_procurado):
    indice = 0
    for numero in lista:
        if numero == valor_procurado:
            return indice
        indice = indice + 1
    return -1

```

ou, foram alternativa:

```python
def busca_sequencial(lista, valor_procurado):
    for i in range(len(lista)):
        if lista[i] == valor_procurado:
            return i
    return -1

```

ou, de uma forma mais `pythonica`:


```python
def busca_sequencial(lista, valor_procurado):
    for indice,numero in enumerate(lista):
        if numero == valor_procurado:
            return indice
    return -1

```
alternativa:

```python
def busca_sequencial(lista, valor_procurado):
    try:
        return lista.index(valor_procurado)
    except ValueError:
        return -1
```


3. Chame a função de busca sequencial e imprima o resultado.

```python
indice = busca_sequencial(lista, valor_procurado)
if indice != -1:
    print(f"Valor encontrado no índice {indice}")
else:
    print("Valor não encontrado")
```

Realizamos a busca linear de diversas formas, incluse com o recurso (try/except) na função de busca. Fizemos isso porque o método index() retorna o índice em que o elemento aparece na lista de entrada (caso esse elemento esteja presente) e ValueError caso o elemento não esteja na lista

!!! warning
    Uma pergunta natural a se fazer é: existe alguma forma de se pesquisar por um elemento em uma lista de modo mais eficiente?

    A resposta a essa pergunta depende da forma como os elementos estão organizados no vetor. Se eles não estiverem em uma ordem específica, não há como fugir da pesquisa linear. Se os elementos estiverem ordenados de alguma forma, podemos usar `busca binária`.



!!! progress
    continuar ...

### Exercicos para compreensão


!!! exercise choice "Questão 1"
    Qual das seguintes afirmações descreve corretamente a busca sequencial?

    - [ ] A busca sequencial é mais rápida que a busca binária.
    - [x] A busca sequencial verifica cada elemento da lista um por um até encontrar o elemento desejado.
    - [ ] A busca sequencial requer que a lista esteja ordenada.
    - [ ] A busca sequencial divide a lista em duas partes iguais a cada passo.

    !!! answer
        A busca sequencial verifica cada elemento da lista um por um até encontrar o elemento desejado. Não requer que a lista esteja ordenada e é geralmente mais lenta que a busca binária em listas grandes.


!!! exercise choice "Questão 2"
    Em uma lista de 100 elementos, qual é o número máximo de comparações que a busca sequencial pode fazer para encontrar um elemento?

    - [ ] 50
    - [ ] 99
    - [x] 100
    - [ ] 101

    !!! answer
        No pior caso, a busca sequencial pode fazer até 100 comparações para encontrar um elemento em uma lista de 100 elementos, se o elemento estiver na última posição ou não estiver na lista.


!!! exercise choice "Questão 3"
    Qual das seguintes situações é mais adequada para usar a busca sequencial?

    - [ ] Quando a lista está ordenada e tem muitos elementos.
    - [ ] Quando a lista está ordenada e tem poucos elementos.
    - [x] Quando a lista não está ordenada e tem poucos elementos.
    - [ ] Quando a eficiência não é importante.

    !!! answer
        A busca sequencial é mais adequada para listas não ordenadas com poucos elementos, pois nesse caso, a simplicidade do algoritmo pode compensar a falta de eficiência.


!!! exercise choice "Questão 4"
    Qual é a complexidade de tempo da busca sequencial em termos de notação Big O?

    - [ ] O(log n)
    - [x] O(n)
    - [ ] O(n^2)
    - [ ] O(1)

    !!! answer
        A complexidade de tempo da busca sequencial é O(n), pois no pior caso, é necessário verificar cada elemento da lista uma vez.


!!! exercise choice "Questão 5"
    Se você estiver usando a busca sequencial para encontrar um elemento em uma lista, qual é a melhor posição para o elemento, se você deseja minimizar o número de comparações?

    - [x] No início da lista.
    - [ ] No meio da lista.
    - [ ] No final da lista.
    - [ ] A posição do elemento não afeta o número de comparações.

    !!! answer
        Se o elemento estiver no início da lista, a busca sequencial encontrará o elemento na primeira comparação, minimizando o número de comparações necessárias.

