
## Recursão

Na aula de hoje, vamos dar uma pausa nos algoritmos de busca e ordenação que estamos estudando para falar de `Recursão` que é um conceito fundamental em Ciência da Computação. A intuição é de que uma função chama a si própria diretamente ou indiretamente, permitindo que problemas sejam resolvidos de forma elegante e muitas vezes eficiente. Em outras palavras, a ideia central da recursão é `dividir um problema grande e complexo em problemas menores e mais gerenciáveis`, que são mais fáceis de resolver, o famoso `dividir para conquistar`.


![](https://media.geeksforgeeks.org/wp-content/uploads/20200707093844/WhatsApp-Image-2020-07-07-at-9.37.31-AM.jpeg)

!!! tip
    `To understand recursion, you must first understand recursion.` A chave entender recursão é identificar o "caso base" (ou condição de parada), que é uma condição sob a qual a recursão termina, evitando assim um loop infinito, e o "caso recursivo", que é onde a função faz uma chamada a si mesma com um conjunto de parâmetros que se aproxima do caso base. Calma,vamos entender direitinho...


!!! progress
    continuar...


## Estrutura Básica de uma Função Recursiva

Vamos estudar um exemplo simples. Queremos escrever um algoritmo que exiba um contador que reproduz a seguinte saída:

```python
5
4
3
2
1
fim!
```

Facil!! Podemos utilizar uma estrutura de repetição `while` ou `for` para fazer essa tarefa, por exemplo:

```python
def contador_for(numero):
    for i in range(numero,0,-1):
        print(i)
    print('fim!')

# para testar
contador_for(5)
```

ou 

```python
def contador_while(numero):
    while numero > 0:
        print(numero)
        numero -= 1
    print('fim!')

# para testar    
contador_while(5)
```

E se quisermos usar apenas 'if'? É possível implementar um algoritmo com essa saída usando apenas if? A resposta é 'sim', e é aqui que a 'recursão' entra em jogo.

Vamos utilizar uma função recursiva para resolver esse problema:

```python 
def contador_if(numero):
    if numero == 0:
        return print('fim!')
    else:
        print(numero)
        return contador_if(numero -1)

# para testar
contador_if(5)
```


Neste exemplo, a função 'contador_if' chama a si mesma com um parâmetro que é decrementado a cada chamada, até que o caso base (numero == 0) seja atingido. Quando isso acontece, a função imprime 'fim!' e a recursão termina.

Uma função recursiva típica em Python tem a seguinte estrutura:

```python
def funcao_recursiva(parametros):
    if caso_base:
        # bloco de código ...
        return valor_base
    else:
        # bloco de código ...
        return funcao_recursiva(parametros_modificados)

```


!!! exercise
    Com base no exemplo 'contador_if', altere a função para dar prints extras que nos ajude a entender como o programa funciona. Nesta versão é exibido 'Entrando em contador_if ( n )' para indicar que entrou na função com o valor 'n' da chamada. e 'Saindo de contador_if(n)' para indicar o retorno da recursão.

    ```python 
    Entrando em contador_if( 5 )
    5
    Entrando em contador_if( 4 )
    4
    Entrando em contador_if( 3 )
    3
    Entrando em contador_if( 2 )
    2
    Entrando em contador_if( 1 )
    1
    Entrando em contador_if( 0 )
    fim!
    Saindo de contador_if( 0 )
    Saindo de contador_if( 1 )
    Saindo de contador_if( 2 )
    Saindo de contador_if( 3 )
    Saindo de contador_if( 4 )
    Saindo de contador_if( 5 )

    ```


!!! exercice
    O GCD (Greatest Common Divisor), ou MDC (Maior Divisor Comum) em português, é o maior número que divide dois ou mais números inteiros sem deixar resto. Em outras palavras, é o maior número pelo qual dois ou mais números inteiros podem ser divididos igualmente.

    Por exemplo, o GCD de 12 e 18 é 6, pois 6 é o maior número que divide ambos 12 e 18 sem deixar resto. Outro exemplo é o GCD de 48, 72 e 120, que é 24.

    O GCD é uma ferramenta importante em matemática, especialmente em teoria dos números, e é frequentemente usado para simplificar frações, resolver equações diofantinas e em muitos outros contextos. Existem vários métodos para calcular o GCD, sendo o algoritmo de Euclides um dos mais eficientes.

    ref: [https://www.freecodecamp.org/news/euclidian-gcd-algorithm-greatest-common-divisor/](https://www.freecodecamp.org/news/euclidian-gcd-algorithm-greatest-common-divisor/)

    ```python

    def gcd(a, b):
        if b == 0: return a
        return gcd(b, a % b)
    
    print(gcd(20, 12))
    ```

    Qual a saida esperada deste código?


    !!! answer
        Neste caso, a saída esperada é '4', pois esse é o valor do máximo divisor comum entre 20 e 12.


!!! progress
    continuar...


### O problema da recursão infinita


Um dos riscos ao utilizar a recursão é a possibilidade de cair em uma recursão infinita. Isso ocorre quando as chamadas recursivas nunca atingem o caso base, fazendo com que a função chame a si mesma indefinidamente. Esse problema pode levar a um 'estouro da pilha' de chamadas (stack overflow), resultando em um erro de execução.

!!! Warning
    Todo problema recursivo deve ter pelo menos um caso base, que é a condição sob a qual a recursão termina, e um ou mais casos recursivos, que são as chamadas à própria função.


É crucial que cada chamada recursiva aproxime o problema do caso base, evitando assim uma recursão infinita. A estrutura lógica deve garantir que o problema seja reduzido a cada chamada.

Vamos ver o exemplo a seguir: 

```python 
def contador(n):
  if n == 0:
    print('fim')
  else:
    print(n)
    contador(n - 2)

contador(4)
```

Neste exemplo, a função contador realiza uma chamada recursiva a si mesma com 'n - 2'. Se n for um número par, a função se aproxima do caso base (n == 0) e termina corretamente. No entanto, se n for ímpar, a função nunca alcança o caso base, resultando em uma recursão infinita.


!!! exercise
    Execute a função contador com n = 5 e observe o comportamento. Proponha uma forma de corrigir o problema do loop infinito ajustando o caso base.



### Como Identificar e Evitar a Recursão Infinita

- Caso Base Claro: Certifique-se de que sua função recursiva tenha um caso base bem definido e que seja possível alcançá-lo. O caso base é a condição sob a qual a recursão termina, e deve ser verificado no início da função.

- Progressão em Direção ao Caso Base: Em cada chamada recursiva, os argumentos devem se aproximar do caso base. Isso significa que, para problemas numéricos, os valores devem aumentar ou diminuir em direção ao valor do caso base. Para problemas estruturais, como na travessia de uma árvore, deve haver uma progressão em direção a uma estrutura menor ou a um elemento terminal.

- Teste e Depuração: Teste sua função com vários casos de entrada para garantir que ela se comporta conforme esperado e alcança o caso base. Ferramentas de depuração podem ajudar a rastrear o fluxo de execução e identificar onde a função pode estar entrando em um loop infinito.


!!! progress
    continuar...


Vamos conhecer alguns exemplos clássicos de recursão que podem aparecer em uma entrevista técnica. 

## Exemplo Fatorial

Um exemplo clássico de aplicação da recursão é o cálculo do fatorial de um número 'n!', que é o produto de todos os números inteiros positivos de 1 até n.

```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

```

A função fatorial segue esta lógica:

- 'Caso base': Se n for 0 ou 1, o fatorial é 1. Esse é o caso base que impede que a função chame a si mesma infinitamente.
- Passo recursivo: Se n for maior que 1, a função retorna 'n' multiplicado pelo fatorial de 'n-1'. Isso quebra o problema em um problema menor até que ele atinja o caso base.

Aulas passadas realizamos a implementação do fatorial sem recursão, era alguma coisa parecida com:

```python
def fatorialIterativo(n):
    fatorial = 1
    for i in range(1, n + 1):
      fatorial *= i
    return fatorial

```


Neste caso definimos uma varialvel 'fatorial' para acumular o valor do fatorial além de definir um range de 1 até 'n+1' para o loop for.


## Benefícios e Desvantagens da Recursão

- Benefícios:

    - Simplicidade: A recursão pode tornar o código mais limpo e mais fácil de entender, especialmente para problemas que têm uma definição naturalmente recursiva, como travessia de árvores.
    - Redução de código: Muitas vezes, a recursão permite reduzir a quantidade de código necessário para resolver um problema.

- Desvantagens:

    - Desempenho: Funções recursivas podem ser menos eficientes em termos de tempo de execução e uso de memória devido às múltiplas chamadas de função e ao aumento da pilha de chamadas.
    - 'Risco de estouro de pilha': Chamadas recursivas profundas podem levar a um "stack overflow" se o caso base não for atingido ou se o número de chamadas recursivas for muito grande.

- Técnicas de Otimização da Recursão

    - Memoização: Armazenar os resultados de chamadas de função em uma estrutura de dados (por exemplo, um dicionário) para evitar cálculos repetidos. Isso é especialmente útil em problemas de otimização e programação dinâmica.


### Exemplo Fibonacci

Outro exemplo clássico é a 'Sequência de Fibonacci' que é a sequência numérica proposta pelo matemático Leonardo Pisa, mais conhecido como Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.....

Para entender o que é assista o video do [Pato Donald ](https://youtu.be/XVLHX0ddtqo?si=PTR3W-NQCFTuI3v7)


!!! video
    ![Pato Donald e Fibonacci ](https://youtu.be/XVLHX0ddtqo?si=PTR3W-NQCFTuI3v7)


A função 'fibonacciSimples' calcula o n-ésimo termo da sequência de Fibonacci. Para 'n' igual a 0 ou 1, a função retorna 'n' diretamente. Para outros valores de n, a função chama a si mesma 'duas vezes', uma vez para 'n-2' e outra vez para 'n-1', e soma os resultados.

```python 
def fibonacciSimples(n):
    if n == 0 or n == 1: return n
    return fibonacciSimples(n - 2) + fibonacciSimples(n - 1)

# para testar
fibonacciSimples(5)    
```

Essa abordagem tem uma eficiência ruim para valores grandes de 'n' devido ao grande número de chamadas recursivas repetidas. Para valores maiores, é recomendável usar técnicas de otimização como a memoização ou abordagens iterativas.


```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# para testar
print(fibonacci(10))
```

Neste exemplo, a função fibonacci utiliza um dicionário memo para armazenar os resultados das chamadas anteriores, evitando assim cálculos redundantes.

!!! progress
    continuar...


## Exercicios

Para aprender recursão, primeiro você tem aprender recursão. Então vamos praticar...


!!! exercise
    Projetar uma função recursiva requer que você escolha cuidadosamente um caso base e certifique-se de que cada sequência de chamadas de função eventualmente atinja um caso base. Neste exercicio, o caso base foi programado para você, mas você escreverá o restante da função recursiva.

    Escreva uma função recursiva somaDigital(n) que recebe um número inteiro positivo n e retorna a soma de seus dígitos. Por exemplo, somaDigital(2024) deve retornar 8 porque 2+0+2+4=8.

    ```python
    def somaDigital(n):
        if n < 10:
            return n
        else:
        # caso recursivo
        # seu código
    ```

!!! exercise
    Escreva uma função recursiva raizDigital(n) que retorna a raiz digital de n. Ou seja, A raiz digital de um número inteiro não negativo n é calculada da seguinte forma. Comece somando os dígitos de n. Os dígitos do número resultante são então somados e esse processo continua até que um número de um único dígito seja obtido. Por exemplo, a raiz digital de 2019 é 3 porque 2+0+1+9=12 e 1+2=3. Utilize a função somaDigital para resolver o problema.




!!! exercise
    A sequência de hailstone começando em um número inteiro positivo n é gerada seguindo duas regras simples. Se n for par, o próximo número na sequência será n/2. Se n for ímpar, o próximo número na sequência será 3*n+1. Repetindo esse processo, geramos a sequência do hailstone. Escreva uma função recursiva hailstone(n) que imprime a sequência de granizo começando em n. Pare quando a sequência atingir o número 1 (caso contrário, faríamos um loop eterno de 1, 4, 2, 1, 4, 2, ...)
    Por exemplo, quando n=5, seu programa deverá gerar a seguinte sequência:

    ```python
    5
    16
    8
    4
    2
    1

    ```



## E agora o que vem pela frente? 


Agora que entendemos o que é recursão, podemos aplicar essa técnca em alguns problemas que já conhecemos tais como a 'busca binária' que é um algoritmo eficiente para encontrar um elemento em uma lista ordenada e algoritmos de oedenação rápida.


```python 
def busca_binaria_recursiva(lista, elemento, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio > fim:
        return -1  # Elemento não encontrado
    meio = (inicio + fim) // 2
    if lista[meio] == elemento:
        return meio
    elif lista[meio] > elemento:
        return busca_binaria_recursiva(lista, elemento, inicio, meio - 1)
    else:
        return busca_binaria_recursiva(lista, elemento, meio + 1, fim)

# para testar
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(busca_binaria_recursiva(lista_ordenada, 5))  # Saída: 4
```


### Recursão vs. Iteração

Embora muitos problemas possam ser resolvidos tanto com recursão quanto com iteração, há situações em que um método pode ser mais adequado que o outro. A recursão é frequentemente mais intuitiva e direta para problemas que têm uma natureza recursiva, como a travessia de estruturas de dados hierárquicas (árvores, por exemplo). No entanto, a iteração pode ser mais eficiente em termos de uso de memória e tempo de execução, especialmente para problemas que não exigem a divisão em subproblemas menores.


!!! progress
    continuar...


Algumas referências: 

    - https://acervolima.com/recursao-em-python/

    - https://cscircles.cemc.uwaterloo.ca/16-recursion/

    - https://panda.ime.usp.br/algoritmos/static/algoritmos/20-divisao-e-conquista.html
