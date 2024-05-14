## Polimorfismo

Se refere à capacidade de uma função ou método de processar objetos de diferentes maneiras, dependendo da classe ou do tipo de objeto que é fornecido a ela.

### Tipos de Polimorfismo

- **Polimorfismo de Sobrecarga**: Refere-se à capacidade de ter várias funções com o mesmo nome, mas com diferentes tipos ou quantidades de parâmetros.
- **Polimorfismo de Substituição**: Quando uma subclasse pode ser usada no lugar de sua classe pai. Isso geralmente é alcançado através da herança e da sobrescrita de métodos.

## Exemplo com Polimorfismo

Criamos uma classe `Animal` com um método `falar`. Duas subclasses, `Cachorro` e `Gato`, que **sobrescrevem** o método falar.

A função `som_do_animal`, repare que ela não pertence a nenhuma classe e pode aceitar qualquer objeto que seja um Animal e chama seu método falar. 

Isso é polimorfismo em ação: a função trata diferentes tipos de objetos (cachorro e gato) de maneira uniforme.


```python
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau"


def som_do_animal(animal):
    print(animal.falar())

# Criando instâncias
cachorro = Cachorro()
gato = Gato()

# Demonstrando polimorfismo
som_do_animal(cachorro)  # Saída: Au Au
som_do_animal(gato)      # Saída: Miau
```

### Benefícios do Polimorfismo

- **Flexibilidade**: O polimorfismo permite escrever código mais flexível e reutilizável.
- **Simplicidade**: Simplifica o código ao permitir o uso de uma interface comum para diferentes tipos de objetos.
- **Extensibilidade**: Facilita a adição de novas classes que se encaixam na mesma interface.

### Exercícios
 
1. Criar uma classe `Animal` com atributos `nome` e `especie`. Adicionar um método `emitir_som()` que imprime um som genérico.
2. Adicionar um método `descrever()` à classe Animal que imprime uma descrição do animal (nome e espécie).
3. Criar uma subclasse `Cachorro` que herda de Animal. Adicionar um atributo adicional `raca` e um método `latir()`.
4. Sobrescrever o método `emitir_som()` na subclasse Cachorro para imprimir um latido específico em vez do som genérico.