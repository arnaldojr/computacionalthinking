
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


### Acesso a Elementos

Cada item em uma lista tem um índice, começando do zero. Você pode acessar itens individuais usando esse índice.

```python
print(frutas[1])  # Saída: banana
print(nomes[0])  # Saída: Alice
print(misturada[2][1])  # ATENCÃO nesta Saída: 3
```
!!! tip
    Em python assim como em outras linguagens de programação, começamos a contar o indice a partir de zero, isso significa que o valor da primeira posição da lista possui indice `0` (zero).


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

#### Remoção

Método para remoção de item da lista:

    - remove(): Remove o primeiro item com o valor especificado.
    - pop(): Remove o item em um índice específico (ou o último item se o índice não for especificado).
    - clear(): Limpa todos os itens da lista.

!!! Tip 
    Cuidado com o método `remove()`,  quando o item não existe na lista vai gerar o erro `ValueError`


```python
frutas.remove("banana")
frutas.pop()
frutas.clear()
```

#### Alteração

Você pode alterar um item referenciando seu índice.

```python
frutas[0] = "manga"
```

### Métodos mais utilizados de Listas

Alguns dos métodos mais utilizados são:
 
    - len(): Retorna o número de itens em uma lista.
    - extend(): Adiciona elementos de outra lista (ou qualquer iterável) ao final da lista atual.
    - index(): Retorna o índice do primeiro item com o valor especificado.
    - count(): Retorna o número de vezes que um valor aparece na lista.
    - sort(): Ordena a lista.
    - reverse(): Inverte a ordem da lista.

!!! Tip 
    É importante mencionar que o método `sort()` altera a lista original, enquanto a função incorporada `sorted()` retorna uma nova lista ordenada.



Teste o código a seguir:

```python
# definimos uma lista de listas (com nome e senha)
usuarios = [
    ['alberto', '1234'],
    ['mario', '6282'],
    ['maria', '5274'],
    ['joana', '9943']
]

nome = input('Nome do usuário: ')
senha = input('Senha: ')

# Verificando se a combinação nome e senha está na lista de usuários
usuario_encontrado = [nome, senha] in usuarios

if usuario_encontrado:
    msg = 'Acesso liberado'
else:
    msg = 'Acesso negado'

print(msg)
```
Neste código estamos usando a expressão `[nome, senha] in usuarios` para verificar se a combinação de nome e senha existe na lista usuarios. Esta expressão retornará True se a combinação for encontrada e False caso contrário.


### Fatiamento (slices)

Além de acessar elementos da lista por meio de índices, podemos realizar o fatiamento de listas. O fatiamento é uma operação que permite extrair uma sublista de uma lista. A sintaxe de fatiamento é representada por colchetes `[]` e dois pontos `:`.

A notação básica do fatiamento é: `lista[início:fim]`, onde:

- início: é o índice inicial do fatiamento (inclusivo).
- fim: é o índice final do fatiamento (exclusivo).

Por exemplo, `lista[1:4]` retorna uma sublista que começa no índice 1 e vai até (mas não inclui) o índice 4.

A notação `[ : ]` pode ser expandida para incluir um terceiro parâmetro, `o passo`, usando a sintaxe `lista[início:fim:passo]`:

- passo: especifica a "distância" entre os índices. Por exemplo, um passo de 2 pula um índice entre cada item incluído na sublista.

A notação `[ : ]` por si só cria uma cópia superficial da lista original. Isso significa que você obtém uma nova lista com os mesmos elementos, mas é uma lista diferente em termos de identidade (ou seja, está armazenada em um local diferente da memória).

Alguns exemplos comuns incluem:

lista[::2]: retorna todos os elementos em índices pares.
lista[::-1]: inverte a lista.
lista[1:5:2]: retorna os elementos nos índices 1 e 3 (começa no índice 1, termina antes do índice 5, com um passo de 2).

```python
números = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_lista = números[2:7]  # [2, 3, 4, 5, 6]
```


juntando as coisas, varrendo uma lista com while. Exemplo de como usar um loop while para iterar através de uma lista

```python 
primos = [2, 3, 5, 7, 11]
i = 0
while i < len(primos):
    print( "elemento de indice %d = %d"%(i, primos[i]) )
    i = i + 1
```

Esse é um exemplo básico de como usar um loop while para iterar através de uma lista em Python. No entanto, em muitos casos, um `loop for` seria uma escolha mais razoável para essa tarefa.


## Tuplas

Tuplas são uma estrutura de dados em Python semelhante às listas. No entanto, enquanto as listas são mutáveis (ou seja, podem ser alteradas após a criação), as tuplas são **`imutáveis`**. Isso significa que, uma vez que uma tupla é criada, seus elementos não podem ser modificados, adicionados ou removidos.

!!! tip
    A principal diferença entre listas e tuplas é que listas são mutáveis, enquanto tuplas são imutáveis.


### Definindo Tuplas

Uma tupla é definida colocando-se uma sequência de valores separados por vírgulas entre parênteses `()`:

```python
variavel = [2,2,2,2]
a = tuple(variavel)

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

### Acessando Elementos de Tuplas

Assim como as listas, as tuplas são ordenadas e indexadas. Você pode acessar elementos de uma tupla usando índices:

```python
tupla = (10, 20, 30, 40, 50)
print(tupla[1])  # Saída: 20

```

### Imutabilidade das Tuplas

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


### Fatiamento em Tuplas

Assim como as listas, as tuplas também suportam operações de fatiamento:


```python
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
fatiado = tupla[2:6]
print(fatiado)  # Saída: (2, 3, 4, 5)

```

### Funções com Tuplas

Várias funções que funcionam com listas também são aplicáveis às tuplas:

- len(tupla): Retorna o número de itens na tupla.
- min(tupla): Retorna o menor item da tupla.
- max(tupla): Retorna o maior item da tupla.


## E agora qual eu escolho?? Por que usar Listas ou Tuplas?

Estudamos duas estruturas de dados muito utlizadas em programação, mas... Você pode se perguntar: `"Por que usar tuplas se as listas são mais flexíveis?"`. 

A escolha entre lista e tupla dependerá do contexto e das necessidades específicas do seu programa. Vamos tentar listar algumas caracteristicas de cada uma delas.

| Característica               | Lista                                                                                   | Tupla                                                              |
|------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Mutabilidade                 | Mutável (itens podem ser adicionados, removidos ou alterados).                          | Imutável (não pode ser alterada após a criação).                    |
| Sintaxe                      | Usa colchetes `[]`: `[1, 2, 3]`                                                         | Usa parênteses `()`: `(1, 2, 3)`                                    |
| Performance                  | Geralmente mais lenta para algumas operações devido à mutabilidade.                     | Geralmente mais rápida por ser imutável.                            |
| Utilização em dicionários    | Não pode ser usada como chave devido à mutabilidade.                                    | Pode ser usada como chave por ser imutável.                         |
| Métodos integrados           | Vários, como `append()`, `remove()`, `pop()`, `reverse()`, `extend()`.                  | Limitados, como `count()` e `index()`.                              |
| Tamanho (uso de memória)     | Geralmente ocupa mais memória devido à sobrecarga associada à mutabilidade.             | Ocupa menos memória devido à sua estrutura fixa e imutável.         |
| Casos de uso comuns          | Dados dinâmicos, armazenamento temporário, onde a mutabilidade é necessária.            | Representações imutáveis, como pontos em geometria, chaves de dicionários. |

Se você precisa de mutabilidade, vá de lista. Se você quer imutabilidade (por razões de segurança, performance ou semântica), escolha tupla.

Em geral, as tuplas são usadas em situações onde a imutabilidade é necessária ou benéfica. Por exemplo, tuplas podem ser usadas como chaves em dicionários (veremos isso em breve no curso ), enquanto listas não podem. Além disso, as tuplas, por serem imutáveis, podem ser mais seguras para certos tipos de operações onde não queremos que os dados sejam alterados acidentalmente. Vamos tentar ver algumas aplicações.


| Aplicação                                              | Escolha | Justificativa                                                                                               |
|--------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------|
| Mantendo uma lista de tarefas pendentes                | Lista   | As tarefas podem ser adicionadas, removidas ou reordenadas dinamicamente.                                   |
| Representando um ponto no espaço 3D                    | Tupla   | Um ponto no espaço é imutável.                                                                              |
| Chaves para coordenadas geográficas em dicionários     | Tupla   | Dicionários requerem que as chaves sejam imutáveis.                                                         |
| Coletar e processar dados em tempo real                | Lista   | Dados podem precisar ser constantemente atualizados, adicionados ou removidos.                               |
| Retorno de múltiplos valores de função                 | Tupla   | Retorna um grupo fixo de valores que representam diferentes coisas.                                         |
| Edição de Strings por Caractere                        | Lista   | Strings são imutáveis em Python, então para edição eficiente é convertido para lista e depois de volta para string. |
