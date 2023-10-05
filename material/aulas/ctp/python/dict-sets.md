
## Dicionários em Python

Dicionários são estruturas de dados que permitem armazenar pares de chave-valor. Em Python, dicionários são delimitados por chaves `{}`.

### Criação de Dicionários

Dicionários são criados usando chaves `{}`, contendo pares chave-valor separados por dois pontos `:`.

```python
pessoa = {"nome": "Alice", "idade": 30, "profissão": "Engenheira"}
print(pessoa["nome"])  # Saída: Alice
```

!!! exercise choice "Question"
    Qual é a saída do código a seguir?
    ```python
    d = {"a": 1, "b": 2, "c": 3}
    print(d["b"])
    ```
    - [ ] 1
    - [x] 2
    - [ ] 3
    - [ ] KeyError

    !!! answer
        A saída é `2`.

### Acesso a Elementos

Para acessar o valor associado a uma chave, use a chave como índice.

```python
print(pessoa["idade"])  # Saída: 30
```

Se tentarmos acessar uma chave que não existe, obteremos um `KeyError`.

### Adição, Remoção e Alteração de Elementos

Dicionários são mutáveis, portanto podemos adicionar, remover ou alterar pares chave-valor.

```python
pessoa["nacionalidade"] = "Brasileira"
pessoa["idade"] = 31
del pessoa["profissão"]
```

### Métodos mais utilizados de Dicionários

- `keys()`: Retorna uma lista de todas as chaves.
- `values()`: Retorna uma lista de todos os valores.
- `items()`: Retorna uma lista de tuplas (chave, valor).
- `get(key, default)`: Retorna o valor para a chave especificada ou o valor default.

```python
print(pessoa.keys())    # Saída: dict_keys(['nome', 'idade', 'nacionalidade'])
print(pessoa.values())  # Saída: dict_values(['Alice', 31, 'Brasileira'])
print(pessoa.get("cidade", "Não especificado"))  # Saída: Não especificado
```

### Iterando em Dicionários

Podemos iterar pelas chaves, valores ou pares chave-valor de um dicionário.

```python
for chave, valor in pessoa.items():
    print(chave, ":", valor)
```

## Conjuntos em Python

Conjuntos são uma coleção de elementos únicos. Em Python, conjuntos são similares a listas ou dicionários, mas não podem ter elementos duplicados e não são ordenados.

### Criação de Conjuntos

Conjuntos são criados usando chaves `{}` ou a função `set()`.

```python
frutas = {"maçã", "banana", "cereja"}
print("maçã" in frutas)  # Saída: True
```

### Operações com Conjuntos

Podemos realizar operações típicas de conjuntos, como união, interseção e diferença.

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # União: {1, 2, 3, 4, 5}
print(a & b)  # Interseção: {3}
print(a - b)  # Diferença: {1, 2}
```

### Métodos mais utilizados de Conjuntos

- `add(elem)`: Adiciona um elemento ao conjunto.
- `remove(elem)`: Remove um elemento do conjunto.
- `pop()`: Remove e retorna um elemento do conjunto.
- `clear()`: Limpa todos os elementos do conjunto.

```python
frutas.add("uva")
frutas.remove("banana")
print(frutas)  # Saída: {"maçã", "cereja", "uva"}
```

### Iterando em Conjuntos

Assim como listas e dicionários, podemos iterar pelos elementos de um conjunto.

```python
for fruta in frutas:
    print(fruta)
```

!!! exercise choice "Question"
    Considere os conjuntos `a = {1, 2, 3, 4}` e `b = {3, 4, 5, 6}`. Qual é a saída de `print(a & b)`?
    - [ ] {1, 2}
    - [ ] {5, 6}
    - [x] {3, 4}
    - [ ] {1, 2, 3, 4, 5, 6}

    !!! answer
        A saída é {3, 4} porque essa é a interseção dos conjuntos `a` e `b`.








