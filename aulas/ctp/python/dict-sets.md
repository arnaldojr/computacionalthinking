## Dicionários em Python

Dicionários são estruturas de dados que permitem armazenar pares de `chave-valor`. Em Python, dicionários são delimitados por chaves `{}`. As strings, listas e tuplas utilizam inteiros como indices. Se voce tentar utilizar
qualquer outro tipo como indice, voce receberá um erro. O dicionario vai nos ajudar nisso.

### Criação de Dicionários


Dicionários são criados usando chaves `{}`, contendo pares chave-valor separados por dois pontos `:`.

```python
meu_dict = dict()    # primeira forma de inicializar um dicionario
meu_dict = {}        # segunda forma de inicializar um dicionario

```
Podemos inicializar um dicionário com valores

```python
pessoa = {"nome": "Alice", "idade": 30, "profissão": "Engenheira"}
```

!!! exercise choice "Question"
    Qual alternativa indica um dicionário?

    - [ ] ['nome': 'arnaldo', 'idade': 10, 'sexo': 'masculino']
    - [x] {'nome': 'arnaldo', 'idade': 10, 'sexo': 'masculino'}
    - [ ] ('nome': 'arnaldo'), ('idade': 10), ('sexo': 'masculino')
    - [ ] [['nome': 'arnaldo'], ['idade': 10], ['sexo': 'masculino']]

    !!! answer
        A saída é {'nome': 'arnaldo', 'idade': 10, 'sexo': 'masculino'}.

!!! progress
    Continuar...

### Acesso a Elementos

Para acessar o valor associado a uma chave, use a chave como índice.

```python
pessoa = {"nome": "Alice", "idade": 30, "profissão": "Engenheira"}

print(pessoa["idade"])  # Saída: 30
```

Se tentarmos acessar uma chave que não existe, obteremos um `KeyError`.

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


### Adição, Remoção e Alteração de Elementos

Dicionários em Python são mutáveis, o que significa que você pode adicionar, alterar ou remover pares chave-valor após sua criação.

#### Adição
Para adicionar um novo par chave-valor a um dicionário, você simplesmente atribui um valor a uma nova chave:

```python
pessoa = {}
pessoa["nome"] = "Carlos"

```

Após executar o código acima, o dicionário pessoa conterá `{"nome": "Carlos"}`.

#### Alteração

Se você atribuir um valor a uma chave já existente, o valor anterior associado a essa chave será substituído:

```python
pessoa["nome"] = "Roberto"

```
Agora, o dicionário `pessoa` foi atualizado para `{"nome": "Roberto"}`.

O método `update()` é usado para inserir pares chave-valor de um dicionário em outro dicionário. Se a chave já existir no dicionário original, o valor para essa chave será atualizado. Se a chave não existir, o par chave-valor será adicionado.

#### Remoção

Para remover um par chave-valor de um dicionário, você pode usar a instrução `del` seguida da chave que deseja remover:

```python
del pessoa["nome"]
```
Após a execução deste código, a chave "nome" e seu valor associado serão removidos do dicionário pessoa, deixando-o vazio.


!!! exercise choice "Question"
    Dado o dicionário:
    
    ```python
    dados = {
        "alunos": {
            "Ana": {"idade": 20, "curso": "Engenharia"},
            "Pedro": {"idade": 25, "curso": "Matemática"},
        },
        "professores": {
            "Dr. Silva": {"idade": 40, "disciplina": "Física"},
            "Dra. Fernanda": {"idade": 35, "disciplina": "Química"},
        },
    }
    ```

    Qual será a saída do código a seguir?


    ```python
    print(dados["alunos"]["Pedro"]["curso"])
    ```

    - [ ] Engenharia
    - [ ] Física
    - [x] Matemática
    - [ ] Química
    
    !!! answer
        A saída é `Matemática`, pois estamos acessando o curso do aluno "Pedro" no dicionário aninhado.


!!! exercise choice "Question"
    Considere os dicionários:
    
    ```python 
    d1 = {"a": 1, "b": 2, "c": 3} 
    d2 = {"b": 3, "c": 4, "d": 5} 
    ```
    
    Após executar o código a seguir, qual será o valor associado à chave "b" em d1?
    
    ```python 
    d1.update(d2) 
    ```
    
    - [ ] 1
    - [x] 3
    - [ ] 4
    - [ ] 5
   
    !!! answer
        O valor associado à chave "b" em `d1` será `3`, pois o método `update()` atualiza o dicionário `d1` com os pares chave-valor de `d2`, sobrescrevendo valores de chaves existentes em `d1`.

!!! progress
    Continuar...

### Métodos mais utilizados de Dicionários

Os dicionários possuem uma série de métodos incorporados que facilitam a manipulação e interação com os dados. Vamos abordar alguns dos métodos mais usados:

- `keys()`: Retorna uma lista de todas as chaves.
- `values()`: Retorna uma lista de todos os valores.
- `items()`: Retorna uma lista de tuplas (chave, valor).
- `get(key, default)`: Retorna o valor para a chave especificada ou o valor default.

Vamos usar o dicionario `d` neste exemplo:

```python
d = {"nome": "Alice", "idade": 31, "nacionalidade": "Brasileira"}
```

**`keys()`**

```python
d = {"nome": "Alice", "idade": 31, "nacionalidade": "Brasileira"}
print(d.keys())  # Saída: dict_keys(['nome', 'idade', 'nacionalidade'])
```

**`value()`**

```python
print(d.values())  # Saída: dict_values(['Alice', 31, 'Brasileira'])
```

**`items()`**

```python
# Jeito simples
print(d.items()) 
```

**`get()`**

O método get() é uma maneira segura de acessar os valores de um dicionário. Se a chave especificada não for encontrada, ele retorna o valor default especificado (ou None se nenhum valor default for fornecido).

```python
cidade = d.get("cidade", "Não especificado")
print(cidade)  # Saída: Não especificado
```
!!! Tip
    Note que usar `d["cidade"]` diretamente causaria um `KeyError`, mas com `get()`, evitamos esse erro e temos uma saída controlada.


!!! exercise choice "Question"
    Dado o dicionário:

    ```python 
    produtos = { "maçã": {"preço": 0.5, "estoque": 100},"banana": {"preço": 0.3, "estoque": 50}, "cereja": {"preço": 2.0, "estoque": 20} } 
    ```

    Qual será a saída do código a seguir?

    ```python 
    print(produtos.get("pêssego", {}).get("preço", "Produto não encontrado"))
    ```

    - [ ] 0.5
    - [ ] 0.3
    - [ ] 2.0
    - [x] Produto não encontrado

    !!! answer
        A saída é `Produto não encontrado`. O método `get()` tenta buscar a chave "pêssego", que não existe no dicionário `produtos`. Como resultado, ele retorna um dicionário vazio (`{}`). O segundo `get()` tenta buscar a chave "preço" neste dicionário vazio e, como ela não existe, retorna a string "Produto não encontrado".


!!! exercise choice "Question"
    Considerando o seguinte dicionário:

    ```python 
    alunos = { "Ana": [8.5, 9.0, 7.5], "Pedro": [6.0, 7.0, 8.0], "Mariana": [9.5, 8.5, 9.0] } 
    ```

    Após executar o código abaixo, qual será a saída?

    ```python 
    notas = alunos.get("Ana") 
    media = sum(notas) / len(notas)
    print(media)
    ```

    - [x] 8.33
    - [ ] 7.0
    - [ ] 8.5
    - [ ] 9.0

    !!! answer
        A média das notas de "Ana" é (8.5 + 9.0 + 7.5)/3 = 8.33. Portanto, a saída correta é 8.33.

 
!!! progress
    Continuar...       

### Iterando em Dicionários

Podemos iterar pelas chaves, valores ou pares chave-valor de um dicionário.

Considerando o dicionário pessoa:

```python
pessoa = {"nome": "Alice", "idade": 30, "profissão": "Engenheira"}
```

```python
for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, ":", valor)
```

!!! Tip
    Ao usar o método `items()` em um dicionário e `desempacotar` os resultados em `chave` e `valor`, você obtém acesso direto a ambos os componentes do `par chave-valor` durante a iteração.


!!! progress
    Continuar...


### Aninhamento em Dicionários

Podemos encontrar estruturas de Dicionários que conter outros dicionários, um conceito conhecido como aninhamento. Isso é especialmente útil quando se deseja representar informações estruturadas de forma hierárquica.

Por exemplo, suponha que queremos representar informações sobre uma pessoa, incluindo seu endereço:

```python
pessoa = {
    "nome": "Alice",
    "idade": 30,
    "endereço": {
        "rua": "Av. Central",
        "número": 123,
        "cidade": "Campinas",
        "estado": "SP"
    }
}
```

Para acessar informações aninhadas, você pode encadear os índices:

```python
print(pessoa["endereço"]["cidade"])  # Saída: Campinas
```

!!! Tip
    Dicionários aninhados são comuns ao trabalhar com dados estruturados, como `arquivos JSON`.


### Listas de Dicionários

Listas de dicionários são uma estrutura de dados comum em Python. Elas permitem armazenar um conjunto de registros, onde cada registro é um dicionário com pares chave-valor.


Consideremos uma lista que representa uma série de produtos:

```python
produtos = [
    {"nome": "camiseta", "preço": 29.99, "estoque": 100},
    {"nome": "calça", "preço": 59.99, "estoque": 50},
    {"nome": "tênis", "preço": 129.99, "estoque": 25}
]

```
#### Iterando pela Lista

Para iterar pela lista e acessar cada dicionário:

```python
for produto in produtos:
    print(produto["nome"], "-", produto["preço"])
```

#### Adicionando um Novo Dicionário

Para adicionar um novo produto:

```python
novo_produto = {"nome": "boné", "preço": 19.99, "estoque": 30}
produtos.append(novo_produto)

```

#### Atualizando um Dicionário

Para atualizar o preço do primeiro produto:

```python
produtos[0]["preço"] = 24.99

```

#### Removendo um Dicionário

Para remover um produto da lista (por exemplo, o terceiro produto):


```python
del produtos[2]

```

Ou, se você quiser remover um produto com base em um critério específico:

```python
produtos = [produto for produto in produtos if produto["nome"] != "tênis"]

```

Este último exemplo utiliza `list comprehension` para criar uma nova lista, excluindo o produto cujo nome é "tênis".

!!! exercise choice "Question"
    Considerando a seguinte lista de dicionários `biblioteca`:
    
    ```python
    biblioteca = [
        {
            "título": "Orgulho e Preconceito",
            "autor": "Jane Austen",
            "ano": 1813,
            "categoria": "Romance"
        },
        {
            "título": "1984",
            "autor": "George Orwell",
            "ano": 1949,
            "categoria": "Ficção distópica"
        },
        {
            "título": "Moby Dick",
            "autor": "Herman Melville",
            "ano": 1851,
            "categoria": "Aventura"
        }
    ]
    ```
    
    Após executar o código abaixo, qual será a saída?
    
    ```python
    resultado = [livro["título"] for livro in biblioteca if livro["categoria"] == "Romance"]
    print(resultado)
    ```
    
    - [x] ["Orgulho e Preconceito"]
    - [ ] ["Orgulho e Preconceito", "1984"]
    - [ ] ["Moby Dick", "1984"]
    - [ ] ["Moby Dick"]
    
    !!! answer
        O código está utilizando list comprehension para filtrar livros da categoria "Romance". O único livro desta categoria na lista `biblioteca` é "Orgulho e Preconceito". Portanto, a saída correta é ["Orgulho e Preconceito"].
    

!!! progress
    Continuar...

## Conjuntos em Python

Conjuntos são uma coleção de `elementos únicos`. Em Python, conjuntos são similares a listas ou dicionários, mas `não podem ter elementos duplicados` e `não são ordenados`.


### Criação de Conjuntos

Conjuntos são criados usando chaves `{}` ou a função `set()`.

```python
moradia = set()

frutas = {"maçã", "banana", "cereja"}

```

!!! Tip 
    Cuidado para não confundir conjunto com dicionario. 
    Diferentemente dos dicionarios, os conjuntos não são ordenados e não possuem pares de chave-valor. 

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








