## Herança em Python

A herança permite que uma classe herde atributos e métodos de outra classe. Uma classe base é especificada na definição de uma classe derivada.

```python
class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def identificar(self):
        return f"Estudante: {self.nome}, Matrícula: {self.matricula}"
```

Neste caso, a classe `Estudandte` herda da classe `Pessoa`. O metodo `super()` inicializa o construtur da classe pai para que a classe filha consiga utilizar os atributos

```python
estudante1 = Estudante("Renato", 18, 44443)
print(estudante1.identificar())

print(estudante1.cumprimentar()) #o metodo cumprimentar pertence a classe Pessoa 
```

### Exercícios

4. Sorveteria: Uma sorveteria é um tipo específico de restaurante. 

    - screva uma classe chamada `IceCreamStand` que herde da classe Restaurante escrita no `Exercício 1`.
    - Adicione um atributo chamado `sabores` que armazene uma lista de sabores de sorvete. 
    - Escreva um método para mostrar esses sabores. Crie uma instância de IceCreamStand e chame esse método.

5. Admin: Um administrador é um tipo especial de usuário. 

    - Escreva uma classe chamada `Admin` que herde da classe Usuario escrita no Exercício 3.
    - Adicione um atributo `privilegios` que armazene uma lista de strings como "pode adicionar postagem", "pode excluir postagem" "pode banir usuário", e assim por diante. 
    - Escreva um método chamado `exibir_privilegios()` que liste o conjunto de privilégios de um administrador. 
    - Crie uma instância de Admin e chame seu método.

## Encapsulamento e Métodos Privados

Vamos tentar entender...

Imagine que você tem uma caixa com vários brinquedos. Você decide quais brinquedos podem ser compartilhados com seus amigos e quais são apenas para você. Encapsulamento em programação é parecido com isso. É como criar uma "caixa" (que é a classe) onde você coloca "brinquedos" (que são os dados e métodos) e decide quais são para uso interno e quais podem ser compartilhados com outros.

Agora, pense nos métodos privados como seus brinquedos especiais que você não quer compartilhar com ninguém. Na sua classe, você tem certas funções (métodos) que só devem ser usadas dentro da própria classe. Elas são como segredos ou ferramentas especiais que ajudam a classe a funcionar, mas não são para serem usadas diretamente por outras partes do seu programa.

Agora de uma forma um pouco mais técnica: O encapsulamento se refere à restrição do acesso direto aos componentes de um objeto, promovendo a segurança do código. Em Python, o encapsulamento é realizado principalmente através do uso de métodos e variáveis privadas ou protegidas.

### Convenções de Nomes em Python

- Atributos Protegidos: Em Python, um atributo protegido é representado por um único sublinhado `_` no início do seu nome (ex: _atributo). Isto é uma convenção que indica que o atributo deve ser acessado apenas dentro da classe e suas subclasses.
- Atributos Privados: Para criar um atributo verdadeiramente privado em Python, você deve usar dois sublinhados `__` no início do seu nome (ex: __atributoPrivado). Isso ativa um recurso chamado `name mangling`, onde o nome do atributo é alterado para evitar o acesso direto de fora da classe.

### Exemplo com Métodos Privados

Vamos criar a classe ContaBancaria.

**Método Público - Depositar**: Você pode dizer a todos como depositar dinheiro. Isso é como um método público. Qualquer um pode usar.
**Método Privado - Calcular Juros**: Mas, o cálculo de quanto juros você ganha é um segredo do banco. Isso é como um método privado. Ele faz um trabalho interno importante, mas os clientes da conta não precisam saber como ele funciona. Eles só veem o resultado (o saldo atualizado com os juros).
**Método Público - Atualizar saldo com juros**: Mostra o saldo atualizado com os juros.

```python
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial  # Atributo protegido

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return self._saldo
        else:
            return "Valor inválido para depósito."

    def _calcular_juros(self):
        # Método privado
        taxa_juros = 0.05
        juros = self._saldo * taxa_juros
        return juros

    def atualizar_saldo_com_juros(self):
        juros = self._calcular_juros()
        self._saldo += juros
        return self._saldo

```

Mais alguns detalhes.

### Metodo privado _calcular_juros.

Este método calcula os juros com base no saldo atual da conta. A taxa de juros está fixada em 5% (0.05). 

**Mas Por Que é Privado?**: Este método é considerado uma operação interna da classe ContaBancaria. O cálculo de juros é um detalhe de implementação que não precisa ser exposto para quem utiliza a classe. Assim, ele é definido como privado (usando um único sublinhado _) para indicar que deve ser usado apenas internamente pela classe.

```python
def _calcular_juros(self):
    taxa_juros = 0.05  # Taxa de juros fixa de 5%
    juros = self._saldo * taxa_juros  # Cálculo dos juros com base no saldo
    return juros
```

### Metodo atualizar_saldo_com_juros 

Este método público usa o método privado _calcular_juros para determinar o valor dos juros e atualizar o saldo.

**Encapsulamento**: Ao chamar _calcular_juros, a classe ContaBancaria `encapsula` a lógica de como os juros são calculados. O usuário da classe não precisa saber como os juros são calculados, apenas que ele pode atualizar o saldo com juros.

```python
def atualizar_saldo_com_juros(self):
    juros = self._calcular_juros()  # Chama o método privado para calcular os juros
    self._saldo += juros  # Atualiza o saldo com os juros calculados
    return self._saldo
```

### Benefícios do Encapsulamento com Métodos Privados

- **Segurança**: Evita que partes críticas da lógica interna da classe sejam alteradas ou mal utilizadas externamente.
- **Manutenção**: Facilita a manutenção e as futuras alterações no código, já que as mudanças internas não afetam o código externo.
- **Clareza**: Torna a interface pública da classe mais clara e mais fácil de entender, escondendo detalhes complexos ou irrelevantes para o usuário da classe.


## Exercícios

1. Implementação de Saque: Adicione um método `sacar(valor)` na classe `ContaBancaria` que permita saques, mas não permita que o saldo fique negativo.

2. Método Privado para Validação: Crie um método privado `_validar_valor(valor)` que verifica se um valor é positivo e maior que zero. Utilize este método nos métodos depositar e sacar.

3. Extensão da Classe: Crie uma subclasse de ContaBancaria, como `ContaPoupanca`, que tenha uma taxa de juros diferente. Demonstre como os métodos protegidos e privados da classe pai são acessados na subclasse.

