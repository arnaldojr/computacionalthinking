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

<?quiz?>

question: Qual alternativa indica um dicionário?
answer: ['nome': 'arnaldo', 'idade': 10, 'sexo': 'masculino']
answer-correct: {'nome': 'arnaldo', 'idade': 10, 'sexo': 'masculino'}
answer: ('nome': 'arnaldo'), ('idade': 10), ('sexo': 'masculino')
answer: [['nome': 'arnaldo'], ['idade': 10], ['sexo': 'masculino']]
content:
A saída é {'nome': 'arnaldo', 'idade': 10, 'sexo': 'masculino'}.
<?/quiz?>


### Acesso a Elementos

Para acessar o valor associado a uma chave, use a chave como índice.

```python
pessoa = {"nome": "Alice", "idade": 30, "profissão": "Engenheira"}

print(pessoa["idade"])  # Saída: 30
```

Se tentarmos acessar uma chave que não existe, obteremos um `KeyError`.

```quiz
{
    "questao": "Qual é a saída do código a seguir?",
	"opcoes": {
		"a": 1,
		"b": 2,
		"c": 3,
        "d": "KeyError",
	},
	"correta": "b",
	"code" : """
```python
    d = {"a": 1, "b": 2, "c": 3}
    print(d["b"])
```"""
}
```

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

```quiz
{
    "questao": "Qual é a saída do código a seguir?",
	"opcoes": {
		"a": "Engenharia",
		"b": "Matemática",
		"c": 20,
        "d": "Dra. Fernanda",
	},
	"correta": "b",
	"code" : """
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
print(dados["alunos"]["Pedro"]["curso"])
```"""
}
```
```quiz
{
    "questao": "Qual é a saída do código a seguir?",
	"opcoes": {
		"a": 1,
		"b": 3,
		"c": 4,
        "d": 5,
	},
	"correta": "b",
	"code" : """
```python
d1 = {"a": 1, "b": 2, "c": 3} 
d2 = {"b": 3, "c": 4, "d": 5}

d1.update(d2) 
```"""
}
```


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


```quiz
{
    "questao": "Dado o dicionário:\n\n```python\nprodutos = {\n    \"maçã\": {\"preço\": 0.5, \"estoque\": 100},\n    \"banana\": {\"preço\": 0.3, \"estoque\": 50},\n    \"cereja\": {\"preço\": 2.0, \"estoque\": 20}\n}\n```\n\nQual será a saída do código a seguir?",
    "opcoes": {
        "a": "0.5",
        "b": "0.3",
        "c": "2.0",
        "d": "Produto não encontrado"
    },
    "correta": "d",
    "code": """
```python
print(produtos.get("pêssego", {}).get("preço", "Produto não encontrado"))
```"""
}
```

```quiz
{
    "questao": "Considerando o seguinte dicionário:\n\n```python\nalunos = {\n    \"Ana\": [8.5, 9.0, 7.5],\n    \"Pedro\": [6.0, 7.0, 8.0],\n    \"Mariana\": [9.5, 8.5, 9.0]\n}\n```\n\nApós executar o código abaixo, qual será a saída?",
    "opcoes": {
        "a": "8.33",
        "b": "7.0",
        "c": "8.5",
        "d": "9.0"
    },
    "correta": "a",
    "code": """
```python
notas = alunos.get("Ana") 
media = sum(notas) / len(notas)
print(media)
```"""
}
```     

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

```quiz
{
    "questao": "Considerando a seguinte lista de dicionários:\n\n```python\nbiblioteca = [\n    {\n        \"título\": \"Orgulho e Preconceito\",\n        \"autor\": \"Jane Austen\",\n        \"ano\": 1813,\n        \"categoria\": \"Romance\"\n    },\n    {\n        \"título\": \"1984\",\n        \"autor\": \"George Orwell\",\n        \"ano\": 1949,\n        \"categoria\": \"Ficção distópica\"\n    },\n    {\n        \"título\": \"Moby Dick\",\n        \"autor\": \"Herman Melville\",\n        \"ano\": 1851,\n        \"categoria\": \"Aventura\"\n    }\n]\n```\n\nApós executar o código abaixo, qual será a saída?",
    "opcoes": {
        "a": "[\"Orgulho e Preconceito\"]",
        "b": "[\"Orgulho e Preconceito\", \"1984\"]",
        "c": "[\"Moby Dick\", \"1984\"]",
        "d": "[\"Moby Dick\"]"
    },
    "correta": "a",
    "code": """
    ```python
    resultado = [livro["título"] for livro in biblioteca if livro["categoria"] == "Romance"]
    print(resultado)
    ```
    """
}
```


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

```quiz
{
    "questao": "Considere os conjuntos `a` e `b` definidos abaixo. Qual é a saída do código?",
    "opcoes": {
        "a": "{1, 2}",
        "b": "{5, 6}",
        "c": "{3, 4}",
        "d": "{1, 2, 3, 4, 5, 6}"
    },
    "correta": "c",
    "code": """
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)
```"""
}
```








