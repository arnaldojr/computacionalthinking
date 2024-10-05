
## Erros e Exceções em Python

Ao escrever programas em Python, é comum encontrar situações em que o código não se comporta como esperado. Essas situações indesejadas são geralmente resultado de 'erros e exceções'. Entender e lidar adequadamente com esses problemas é crucial para desenvolver programas robustos e confiáveis.

### Por que ocorrem erros?

Erros podem ocorrer por diversos motivos, incluindo:

`Erros de Sintaxe`: Ocorrem quando o código não segue as regras gramaticais da linguagem Python. São os erros mais fáceis de corrigir, pois o interpretador aponta exatamente onde está o problema.

Exemplo:

```python
while True print('Hello world')
```

Neste caso, o interpretador indica exatamente onde o erro foi encontrado com uma seta apontando para o local. O erro é causado pelo fato de que falta um dois-pontos (':') antes do `print`.


`Erros Lógicos`: São erros que ocorrem quando o programa é sintaticamente correto, mas não produz o resultado esperado. Esses erros são mais difíceis de detectar e corrigir, pois exigem uma compreensão profunda da lógica do programa.

Exemplo:

```python
# Função para calcular a média de dois números
def calcular_media(a, b):
    media = (a * b) / 2 # Erro lógico: deveria ser (a + b) / 2
    return media

# Testando a função com valores esperados
resultado = calcular_media(4, 6)
print(f"A média de 4 e 6 é {resultado}")

# Saída esperada: A média de 4 e 6 é 5
# Saída real: A média de 4 e 6 é 12.0
```


`Exceções`: São erros detectados durante a execução do programa. Diferentemente dos erros de sintaxe, as exceções podem ocorrer mesmo quando o código está gramaticalmente correto. Exemplos comuns de exceções incluem tentativas de divisão por zero, acesso a um índice fora dos limites de uma lista e abertura de um arquivo que não existe.

<iframe src="https://trinket.io/embed/python/47891252d0" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
	
Note que neste código temos um problema. Não podemos fazer divisão por zero. Imagine esse código rodando em um servidor, esse erro vai fazer o nosso programa python 'quebrar' e parar de executar. E agora como podemos resolver de forma a evitar que o programa pare de funcionar. 


!!! tip
    Queremos garantir que nosso programa possa lidar com situações inesperadas sem 'quebrar'."

### Como os erros prejudicam a performance do sistema?

Quando ocorrem podem ter várias consequências negativas para um sistema, tais como:

`Interrupção do Programa`: Um erro não tratado pode causar a interrupção abrupta do programa, o que pode ser particularmente problemático em sistemas críticos ou em produção.

`Comportamento Inesperado`: Erros lógicos podem levar a comportamentos inesperados, o que pode resultar em decisões incorretas ou em falhas de segurança.

`Consumo Excessivo de Recursos`: Alguns erros, como vazamentos de memória, podem levar ao consumo excessivo de recursos do sistema, afetando a performance e a estabilidade.

### A importância do tratamento de erros e exceções

Tratar adequadamente os erros e exceções é essencial para garantir a confiabilidade e a robustez do sistema. Ao prever e lidar com situações de erro, é possível:

`Melhorar a Usabilidade`: Programas que tratam erros de forma elegante proporcionam uma experiência de usuário mais amigável, evitando mensagens de erro confusas ou interrupções inesperadas.

`Aumentar a Segurança`: Um tratamento cuidadoso de exceções pode prevenir falhas de segurança, como a exposição de informações sensíveis através de mensagens de erro.

`Facilitar a Manutenção`: Códigos que incluem um tratamento claro e consistente de erros são mais fáceis de entender e manter.

!!! progress
    Continuar...

## Exceções

Mesmo que um comando ou expressão estejam sintaticamente corretos, pode ocorrer um erro durante sua execução. Erros detectados durante a execução são chamados de exceções e não são necessariamente fatais.

Exemplos de exceções:

```python
10 * (1/0)   # ZeroDivisionError
4 + spam*3   # NameError
'2' + 2      # TypeError
```

## Tratamento de Exceções

Em python, é possível escrever programas que tratam exceções específicas usando os blocos `try` e `except`:

```python
try:
    # bloco de código que pode gerar um erro
except:
    # bloco de código que será executado em caso de erro

```

- O bloco `try` contém o código que pode gerar um erro. Se ocorrer um erro durante a execução desse bloco, o bloco except será executado.
- O bloco `except` é utilizado para tratar o erro de uma forma adequada, seja exibindo uma mensagem de erro para o usuário ou realizando alguma outra ação para corrigir o problema.


## Tipos de Erros (Except) Exceções

Tratar qualquer tipo de exceção da mesma maneira não é considerado uma boa prática de programação. É recomendável especificar o tipo de erro exato que a cláusula `except` irá capturar. Por isso, o comando try pode ter `mais de um except associado ao tipo de errro`, caso o programador queira associar um tratamento diferente para cada um deles.

O formato geral do comando é:

```python
try:
    # bloco de código que pode gerar um erro
except tipo_de_erro1:
    # bloco de código que será executado em caso de erro do tipo 1
except tipo_de_erro2:
    # bloco de código que será executado em caso de erro do tipo 1
except tipo_de_erro3:
    # bloco de código que será executado em caso de erro do tipo 1
```

Alguns tipos de exceção mais comuns:

`NameError`: exceção gerada quando o programa não consegue encontrar um nome de variável local ou global.
`TypeError`: exceção gerada quando é passado um objeto de um tipo diferente do tipo que a função espera como argumento.
`ValueError`: essa exceção ocorre quando um argumento de uma função tem o tipo certo, mas um valor inadequado.
`ZeroDivisionError`: exceção gerada quando você fornece um zero como segundo argumento para uma divisão ou módulo.
`FileNotFoundError`: essa exceção é gerada quando o arquivo ou diretório que o programa solicitou não existe.


### Exercícios sobre tipos de erros


!!! exercise choice "Question"
    Qual linha de código abaixo causará um erro `ZeroDivisionError` em Python?

    - [ ] `print(10 / 2)`
    - [ ] `print(5 * 0)`
    - [x] `print(1 / 0)`
    - [ ] `print(0 + 10)`

    !!! answer
        `print(1 / 0)` causará um erro `ZeroDivisionError`, pois não é possível dividir um número por zero.

!!! exercise choice "Question"
    Qual linha de código abaixo causará um erro `NameError` em Python?

    - [ ] `x = 5`
    - [x] `print(y)`
    - [ ] `print("Hello, world!")`
    - [ ] `x = "Python"`

    !!! answer
        `print(y)` causará um erro `NameError`, pois a variável `y` não foi definida antes de ser usada.

!!! exercise choice "Question"
    Qual linha de código abaixo causará um erro `TypeError` em Python?

    - [ ] `print(10 + 5)`
    - [ ] `print("Python" * 3)`
    - [x] `print("Python" + 3)`
    - [ ] `print(len("Python"))`

    !!! answer
        `print("Python" + 3)` causará um erro `TypeError`, pois não é possível concatenar uma string com um número inteiro.

!!! exercise choice "Question"
    Qual linha de código abaixo causará um erro `IndexError` em Python?

    - [ ] `lista = [1, 2, 3]`
    - [ ] `print(lista[1])`
    - [ ] `lista.append(4)`
    - [x] `print(lista[3])`

    !!! answer
        `print(lista[3])` causará um erro `IndexError`, pois o índice 3 está fora do alcance da lista `lista` que tem apenas 3 elementos.

!!! exercise choice "Question"
    Qual linha de código abaixo causará um erro `KeyError` em Python?

    - [ ] `dicionario = {"nome": "João", "idade": 30}`
    - [ ] `print(dicionario["nome"])`
    - [x] `print(dicionario["altura"])`
    - [ ] `dicionario["cidade"] = "São Paulo"`

    !!! answer
        `print(dicionario["altura"])` causará um erro `KeyError`, pois a chave `altura` não existe no dicionário `dicionario`.

!!! exercise choice "Question"
    Qual linha de código abaixo causará um erro `AttributeError` em Python?

    - [ ] `import math`
    - [ ] `print(math.sqrt(16))`
    - [x] `print(math.PI)`
    - [ ] `print(math.pow(2, 3))`

    !!! answer
        `print(math.PI)` causará um erro `AttributeError`, pois o módulo `math` não possui um atributo chamado `PI`.

!!! progress
    Continuar...


Além disso, é possível utilizar a cláusula `else` para executar um bloco de código caso não ocorra nenhum erro no bloco try. 


```python
try:
    # bloco de código que pode gerar um erro
except tipo_de_erro1:
    # bloco de código que será executado em caso de erro do tipo 1
except tipo_de_erro2:
    # bloco de código que será executado em caso de erro do tipo 1
else:
    # bloco de código que será executado se nenhum erro ocorrer no bloco try
```

E também é possível utilizar a cláusula `finally` para executar um bloco de código que sempre será executado, independentemente de ter ocorrido um erro ou não. Por exemplo:


```python
try:
    # bloco de código que pode gerar um erro
except tipo_de_erro1:
    # bloco de código que será executado em caso de erro do tipo 1
except tipo_de_erro2:
    # bloco de código que será executado em caso de erro do tipo 1
else:
    # bloco de código que será executado se nenhum erro ocorrer no bloco try
finally:
    # bloco de código que sempre será executado, independentemente de ter ocorrido um erro ou não
```

!!! exercise choice "Question"
    Qual é a saída do seguinte código?

    ```python
    try:
        print("Iniciando...")
        x = 1 / "texto"
    except TypeError:
        print("Erro de tipo.")
    ```

    - [ ] `Iniciando...`
    - [x] `Iniciando...\nErro de tipo.`
    - [ ] `Erro de tipo.`
    - [ ] `Iniciando...\nErro de tipo.\nFinalizando...`

    !!! answer
        A saída será `Iniciando...\nErro de tipo.` pois ocorre um erro de tipo e o bloco `except` é executado.

!!! exercise choice "Question"
    Qual é a saída do seguinte código?

    ```python
    try:
        print("Tentando...")
        x = 10 / 2
    except ZeroDivisionError:
        print("Erro de divisão por zero.")
    else:
        print("Nenhum erro ocorreu.")
    ```

    - [ ] `Tentando...\nErro de divisão por zero.`
    - [x] `Tentando...\nNenhum erro ocorreu.`
    - [ ] `Nenhum erro ocorreu.`
    - [ ] `Tentando...`

    !!! answer
        A saída será `Tentando...\nNenhum erro ocorreu.` pois não ocorre nenhum erro e o bloco `else` é executado.

!!! exercise choice "Question"
    Qual é a saída do seguinte código?

    ```python
    try:
        print("Iniciando...")
        x = int("texto")
    except ValueError:
        print("Erro de valor.")
    else:
        print("Conversão bem-sucedida.")
    ```

    - [ ] `Iniciando...\nConversão bem-sucedida.`
    - [ ] `Erro de valor.`
    - [x] `Iniciando...\nErro de valor.`
    - [ ] `Iniciando...`

    !!! answer
        A saída será `Iniciando...\nErro de valor.` pois ocorre um erro de valor e o bloco `except` é executado.


!!! exercise choice "Question"
    Qual é a saída do seguinte código?

    ```python
    try:
        print("Iniciando...")
        x = 1 / 0
    except ZeroDivisionError:
        print("Erro de divisão por zero.")
    else:
        print("Nenhum erro ocorreu.")
    finally:
        print("Finalizando...")
    ```

    - [ ] `Iniciando...\nNenhum erro ocorreu.\nFinalizando...`
    - [x] `Iniciando...\nErro de divisão por zero.\nFinalizando...`
    - [ ] `Erro de divisão por zero.\nFinalizando...`
    - [ ] `Iniciando...\nFinalizando...`

    !!! answer
        A saída será `Iniciando...\nErro de divisão por zero.\nFinalizando...` pois ocorre um erro de divisão por zero, o bloco `except` é executado, e o bloco `finally` é executado independentemente do que acontece antes.

!!! exercise choice "Question"
    Qual é a saída do seguinte código?

    ```python
    try:
        print("Tentando...")
        x = 1 / 1
    except ZeroDivisionError:
        print("Erro de divisão por zero.")
    else:
        print("Nenhum erro ocorreu.")
    finally:
        print("Finalizando...")
    ```

    - [ ] `Tentando...\nErro de divisão por zero.\nFinalizando...`
    - [ ] `Tentando...\nFinalizando...`
    - [ ] `Nenhum erro ocorreu.\nFinalizando...`
    - [x] `Tentando...\nNenhum erro ocorreu.\nFinalizando...`

    !!! answer
        A saída será `Tentando...\nNenhum erro ocorreu.\nFinalizando...` pois não ocorre nenhum erro, o bloco `else` é executado, e o bloco `finally` é executado independentemente do que acontece antes.

!!! exercise choice "Question"
    Qual é a saída do seguinte código?

    ```python
    try:
        print("Iniciando...")
        x = "texto" + 5
    except TypeError:
        print("Erro de tipo.")
    finally:
        print("Finalizando...")
    ```

    - [ ] `Iniciando...\nFinalizando...`
    - [ ] `Erro de tipo.\nFinalizando...`
    - [x] `Iniciando...\nErro de tipo.\nFinalizando...`
    - [ ] `Iniciando...\nErro de tipo.`

    !!! answer
        A saída será `Iniciando...\nErro de tipo.\nFinalizando...` pois ocorre um erro de tipo, o bloco `except` é executado, e o bloco `finally` é executado independentemente do que acontece antes.

!!! progress
    Continuar...



### Desafios



1. Refaça o desafios do inicio da aula para encontrar o angulo da reta entre os pontos utilizando as tratativas de erros e exceções.


2. Responda: 

!!! exercise choice "Question"
    Considere a seguinte função que realiza uma operação de divisão e trata possíveis erros:

    ```python
    def safe_division(numerator, denominator):
        try:
            result = numerator / denominator
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
            return None
        except TypeError:
            print("Erro: Os tipos dos argumentos devem ser numéricos.")
            return None
        else:
            return result
        finally:
            print("Operação concluída.")
    ```

    Qual será a saída ao executar a seguinte linha de código:

    ```python
    print(safe_division(10, "5"))
    ```

    - [ ] `2.0\nOperação concluída.`
    - [ ] `Erro: Divisão por zero não é permitida.\nOperação concluída.`
    - [x] `Erro: Os tipos dos argumentos devem ser numéricos.\nOperação concluída.\nNone`
    - [ ] `Operação concluída.\nNone`

    !!! answer
        A saída será `Erro: Os tipos dos argumentos devem ser numéricos.\nOperação concluída.\nNone` porque o denominador não é um número, causando um `TypeError`, e a função retorna `None` após imprimir a mensagem de erro. O bloco `finally` é executado independentemente, imprimindo "Operação concluída."


3. Para o código a seguir, responda onde e porque é necessário adicionar ao código algum controle de erro exceção:


    ```python

    def adicionar_tarefa(tarefas, tarefa):
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    def remover_tarefa(tarefas, tarefa):
        tarefas.remove(tarefa)
        print("Tarefa removida com sucesso!")

    def visualizar_tarefas(tarefas):
        if len(tarefas) == 0:
            print("Nenhuma tarefa na lista.")
        else:
            print("Tarefas na lista:")
            for tarefa in tarefas:
                print(tarefa)

    def main():
        tarefas = []

        while True:
            print("\n1 - Adicionar tarefa")
            print("2 - Remover tarefa")
            print("3 - Visualizar tarefas")
            print("4 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                tarefa = input("Digite a tarefa: ")
                adicionar_tarefa(tarefas, tarefa)
            elif opcao == "2":
                tarefa = input("Digite a tarefa a ser removida: ")
                remover_tarefa(tarefas, tarefa)
            elif opcao == "3":
                visualizar_tarefas(tarefas)
            elif opcao == "4":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida.")

    if __name__ == "__main__":
        main()
    ```