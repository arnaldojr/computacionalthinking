# Introdução: Orientação a Objetos em Python

Python é uma linguagem de programação que suporta várias abordagens de programação, incluindo a `programação orientada a objetos (OOP)`. A OOP é um paradigma de programação baseado no conceito de `objetos`, que podem conter dados na forma de campos, frequentemente conhecidos como `atributos`; e códigos, na forma de procedimentos, frequentemente conhecidos como `métodos`.

## Conceitos Básicos de OOP

### Classes e Instâncias

- **Classes**: Um modelo para criar objetos que definem um conjunto de atributos e métodos correspondentes a um tipo de objeto.
- **Instâncias**: Um objeto individual construído a partir de uma classe.

### Atributos e Métodos

- **Atributos**: Variáveis pertencentes a uma classe ou instância.
- **Métodos**: Funções pertencentes a uma classe ou instância.

### Herança

- **Herança**: A capacidade de uma classe herdar atributos e métodos de outra classe.

### Encapsulamento

- **Encapsulamento**: A prática de ocultar detalhes internos ou dados de uma classe, expondo apenas interfaces seguras.

### Polimorfismo

- **Polimorfismo**: A capacidade de apresentar a mesma interface para diferentes tipos fundamentais.


!!! progress
    Continuar...



## Definindo uma Classe

Uma classe é definida usando a palavra-chave `class`, seguida pelo nome da classe e um bloco de código com métodos e atributos.

### Estrutura de uma Classe

Uma classe é composta por atributos (variáveis) e métodos (funções). Aqui está a estrutura básica de uma classe em Python:

```python
class NomeDaClasse:
    # Atributos de classe
    atributo_de_classe = valor

    def metodo1(self):
        # Código do método1
        pass
```

!!! Tip
    É uma boa pratica iniciar o nome de uma classe com a letra maiuscula e os metodos com letra minuscula

### Atributos e Métodos de Instância

Atributos de instância são variáveis associadas a uma instância da classe. Métodos de instância são funções associadas a uma instância da classe e podem acessar atributos de instância através do `self`. 

```python
class NomeDaClasse:
    # Atributos de classe
    atributo_de_classe = valor

    def metodo1(self):
        # Código do método1
        pass

    def metodo2(self):
        # Código do método2
        pass

```

### O Método `__init__`

O método `__init__` é um construtor em Python. É chamado automaticamente quando um novo objeto da classe é criado. Ele inicializa os atributos da nova instância da classe.

```python
class NomeDaClasse:
    # Atributos de classe
    atributo_de_classe = valor

    def __init__(self, parametro1, parametro2):
        # Atributos de instância
        self.atributo1 = parametro1
        self.atributo2 = parametro2

    def metodo1(self):
        # Código do método1
        pass

    def metodo2self):
        # Código do método2
        pass
```

Agora vamos ver em um outro exemplo:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
```

## Criando uma Instância de uma Classe

Para criar uma instância de uma classe, você chama a classe usando o nome da classe seguido por parênteses, passando os argumentos que o método `__init__` requer.

```python
pessoa1 = Pessoa("Junior", 18)
print(pessoa1.cumprimentar())
```

### Exercicios 

1. Restaurante: Crie uma classe chamada `Restaurante`. O método `__init__()` de Restaurante deve armazenar dois atributos: `restaurante_nome` e `tipo_cozinha` . 
    
    - Crie um método chamado `descreve_restaurante()` que mostre essas duas informações, e um método de nome `restaurante_aberto()` que exiba uma mensagem informando que o restaurante está aberto.

    - Crie uma instância chamada `restaurante` a partir de sua classe. Mostre os dois atributos individualmente e, em seguida, chame os dois métodos.

2. Três restaurantes: Comece com a classe do Exercício 1. Crie três instâncias diferentes da classe e chame descreve_restaurante() para cada instância.

3. Usuários: Crie uma classe chamada `Usuario`. Crie dois atributos de nomes `primeiro_nome` e `ultimo_nome` e, então, crie vários outros atributos normalmente armazenados em um perfil de usuário. 
    
    - Escreva um método de nome `descreve_usuario()` que apresente um resumo das informações do usuário. 
    
    - Escreva outro método chamado `saudacao_usuario()` que mostre uma saudação personalizada ao usuário.

    - Crie várias instâncias que representem diferentes usuários e chame os dois métodos para cada usuário.

