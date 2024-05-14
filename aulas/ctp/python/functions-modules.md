## Funções em Python

Funções são blocos de código que são projetados para fazer uma coisa específica. Se você precisar executar essa tarefa várias vezes durante o seu programa, você não precisa digitar todo o código para aquela tarefa novamente. Basta chamar a função dedicada a ela.

## Objetivos

Se familiarizar com os conceitos básicos das funções em Python:

-   Como **definir** e **chamar** funções.
-   Usando **parâmetros** e **valores de retorno**.
-   Definindo **valores padrão** para parâmetros.

## Por que usar funções?

- **Modularidade**: Permite segmentar um programa longo em funções menores e gerenciáveis.
- **Reusabilidade**: Permite reutilizar uma função em diferentes programas.
- **Economia de tempo**: Você não precisa escrever o mesmo código repetidamente.
- **Manutenção de programas**: Se uma lógica precisa ser alterada, você pode fazer a mudança na função específica, em vez de alterar o código repetido em vários lugares.

## 1. Criando uma Função

Uma função é definida usando a palavra-chave `def`, seguida pelo nome da
função, parênteses `()` e dois pontos `:`. O código dentro da função é
indentado.

``` python
def nome_da_funcao():
    print("Olá, sou uma função!")
```

## 2. Chamando uma Função 

Depois de definir uma função, você pode \"chamá-la\" ou \"invocá-la\"
usando seu nome seguido de parênteses.

``` python
nome_da_funcao()  # Isso imprimirá: Olá, sou uma função!
```

## 3. Passando Parâmetros 

Informações podem ser passadas para as funções por meio de parâmetros.
Parâmetros são especificados após o nome da função, entre os parênteses.

``` python
def saudacao(nome):
    print(f"Olá, {nome}!")
```

Ao chamar essa função, você pode passar um valor (argumento) para o
parâmetro `nome`:

``` python
saudacao("Alice")  # Isso imprimirá: Olá, Alice!
```

## 4. Retorno de Função

Uma função pode retornar um valor usando a instrução `return`.

``` python
def somar(a, b):
    return a + b
```

Você pode armazenar o valor retornado em uma variável:

``` python
resultado = somar(5, 3)  # resultado será 8
```

## 5. Valores Padrão para Parâmetros

Você pode definir um valor padrão para um parâmetro para que, se um
argumento não for fornecido ao chamar a função, ela use o valor padrão:

``` python
def saudacao_avancada(nome="Visitante"):
    return f"Olá, {nome}!"
```

Chamando essa função sem fornecer um argumento:

``` python
saudacao_avancada()  # Isso retornará: Olá, Visitante!
```

## 6. Funções com Número Arbitrário de Argumentos 

Às vezes, em programação, nos deparamos com situações em que o número exato de argumentos que uma função deve receber não é conhecido antecipadamente. Python oferece uma maneira flexível de lidar com isso através do uso de `*args `e` **kwargs`.

### Utilizando *args

Quando você deseja que sua função aceite um número indefinido de argumentos posicionais, utiliza-se `*args`. O termo args é apenas uma convenção, e você pode nomeá-lo como desejar, desde que esteja precedido por um asterisco `*`.

``` python
def lista_nomes(*nomes):
    return f"Lista de nomes: {', '.join(nomes)}"
```

Chamando essa função:

``` python
lista_nomes("Alice", "Bob", "Charlie")  # Isso retornará: Lista de nomes: Alice, Bob, Charlie
```

!!! Tip 
    Nota: Embora a convenção mais comum seja usar `*args`, você pode substituir "`args`" por qualquer nome que achar adequado.

### Utilizando  **kwargs

Para situações em que você deseja aceitar um número indefinido de argumentos de palavra-chave, Python oferece  `**kwargs`. Novamente, "`kwargs`" é apenas uma convenção e pode ser substituído por qualquer nome, desde que esteja precedido por dois asteriscos `**`.

Os argumentos passados são armazenados em um dicionário, facilitando seu acesso e manipulação.

Se você não souber quantos argumentos de palavra-chave serão passados para sua função, pode adicionar um `**` antes do nome do parâmetro. Isso permitirá que você passe múltiplos argumentos de palavra-chave para a função e os receba como um dicionário.

``` python
def apresentacao(**pessoa):
    return f"{pessoa['nome']} tem {pessoa['idade']} anos e mora em {pessoa['cidade']}."
```

```python
apresentacao(nome="João", idade=30, cidade="Rio de Janeiro") # Isso retornará: João tem 30 anos e mora em Rio de Janeiro.
```

!!! Tip 
    Nota: Semelhante ao `*args`, `**kwargs` é apenas uma convenção. Você é livre para usar qualquer nome que desejar, mas é recomendado seguir essa convenção para manter a legibilidade e compreensibilidade do código.

## 7. Funções Lambda 

Uma função lambda é uma pequena função anônima. Uma função lambda pode ter qualquer número de argumentos, mas só pode ter uma expressão. A expressão é avaliada e retornada. As funções lambda podem ser usadas onde objetos de função são necessários.

Exemplo:

``` python
f = lambda x, y: x + y
f(5, 3)  # Isso retornará 8
```

### E o que mais??

Esse assunto não se esgota aqui... mas já é um bom inicio para o nosso aprendizado.
