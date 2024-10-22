## Estruturas de Repetição com Laço `while`

Em Python, as estruturas de repetição são cruciais para executar um bloco de código várias vezes até que uma condição seja atendida (ou deixe de ser atendida). O laço `while` é uma dessas estruturas, permitindo repetições baseadas em condições.


##  Casos de Uso Comuns

O laço while é frequentemente usado em situações em que a quantidade de iterações não é conhecida antecipadamente. Alguns cenários comuns incluem:

- **Leitura de arquivos até o final**: Pode-se usar um laço while para ler linhas de um arquivo até que não haja mais linhas a serem lidas.
- **Menus interativos**: Em aplicativos com interface de linha de comando, um menu pode ser continuamente apresentado ao usuário até que ele escolha sair.
- **Jogos**: Em jogos, um loop while pode ser usado para manter o jogo em execução até que uma condição de término seja atendida, como o jogador perder todas as vidas.


### Entendendo o Laço `while`

O laço `while` repete um bloco de código enquanto uma condição é avaliada como verdadeira (`True`). Assim que a condição torna-se falsa (`False`), o laço é interrompido e o programa prossegue para as próximas linhas de código, após o laço.


A estrutura básica do loop `while` é:

```python
while condição:
    # código a ser executado enquanto a condição for verdadeira
```

!!! tip
    É crucial garantir que a condição do loop `while` se torne falsa em algum momento, caso contrário, o loop continuará infinitamente.


### Exemplo Básico


```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Neste exemplo, o código imprimirá os números de 0 a 4. Quando `contador` atingir o valor 5, a condição `contador < 5` se tornará falsa e o laço será interrompido.


### Exercícios de Verificação

Qual será a saída do seguinte código?

```python
i = 3
while i > 0:
    print(i)
    i -= 1
```

Após a execução do código, qual será o valor de `x`?

```python
x = 10
while x > 0:
    x -= 2

print x
```

No seguinte código, quantas vezes o print será executado?

```python
y = 5
while y < 8:
    print("Executando...")
    y += 1
```


### E se não existem os laços de repetição, como seria? 

Apenas por curiosidade... Se não existem os laços de repetição poderiamos utilizar uma técnica de recursão para conseguir fazer nossos códigos realizar loops. Apenas como exemplo avalie o código abaixo e entenda como ele funciona. Mais adiante em nosso curso vamos explorar a fundo as recussões. 

```python
def cont(contador):
    if contador == 5:
        return
    print(contador)
    contador += 1
    cont(contador)

cont(0)
```
Neste exemplo, o código imprimirá os números de 0 a 4. Quando `contador` atingir o valor 5, a condição `contador == 5` se tornará verdadeira e será interrompido.


### Combinação de `while` com Estruturas de Decisão

Frequentemente na programação, precisamos de lógicas de repetição que também incluam tomadas de decisão. Combinando o laço `while` com estruturas de decisão como `if-else`, podemos criar fluxos mais dinâmicos e adaptáveis às condições que são verificadas durante a execução.

Ao integrar essas estruturas, é possível, por exemplo, adaptar ações dentro do loop com base em determinadas condições, tornando o código mais flexível e versátil.

```python
numero = 0
while numero <= 10:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
    numero += 1
```

No código acima, usamos o operador módulo (`%`) para verificar o resto da divisão do `numero` por 2. Se o resto é 0, o número é par; caso contrário, é ímpar. A cada iteração, o valor de `numero` é incrementado, e essa lógica é repetida até que `numero` seja maior que 10.


### Interação com o Usuário e Laço `while`

Muitas vezes, em programas interativos, queremos que o código execute enquanto aguardamos uma entrada do usuário ou até que o usuário decida encerrar. O laço `while` é ideal para esses cenários.

#### Exemplo com `input` do Usuário

Suponha que queremos que o usuário insira números e o programa os multiplique por 10, até que o usuário decida parar:

```python
resposta = "sim"
while resposta.lower() == "sim":
    numero = float(input("Digite um número: "))
    print(f"{numero} multiplicado por 10 é {numero * 10}")
    resposta = input("Deseja continuar? (sim/não) ")
```




#### Exemplo com Loop Contínuo até Digitar "sair"

Podemos criar um loop que executa continuamente até que o usuário digite uma palavra-chave, como "sair":

```python
mensagem = ""
while mensagem != "sair" or "SAIR":
    mensagem = input("Digite uma mensagem ou 'sair' para encerrar: ")
    if mensagem.lower() != "sair":
        print(f"Você digitou: {mensagem}")
```




Aqui, o programa imprimirá as mensagens do usuário até que ele digite "sair".


### Exercícios de Verificação

Quantas vezes a mensagem "é meu número favorito!" será impressa?

```python
numero = 0
while numero < 5:
    if numero == 3:
        print(f"{numero} é meu número favorito!")
    else:
        print(f"{numero} é um número comum.")
    numero += 1
```

### Uso do `break` e `continue` com `while`

Dentro dos laços de repetição em Python, temos duas instruções poderosas que nos permitem controlar o fluxo da execução: `break` e `continue`.

- **`break`**: Esta instrução interrompe completamente o laço. Quando o interpretador encontra um `break`, ele sai do laço atual e continua a execução do código após esse laço.
  
- **`continue`**: Ao contrário do `break`, o `continue` não interrompe o laço completamente. Ele apenas interrompe a iteração atual e faz o laço retornar ao seu início, avaliando a condição novamente.

#### Uso do `break` com `while`

Imagine que você esteja buscando um elemento em uma lista e queira parar a busca assim que encontrá-lo. O `break` é perfeito para este cenário.


```python
contador = 0
while contador < 10:
    if contador == 5:
        break
    print(contador)
    contador += 1
print(f"continua fora do while com contador = {contador}")
```

No código acima, a execução do laço `while` é interrompida assim que o `contador` alcança o valor 5. Como resultado, o programa imprime os números de 0 a 4.

#### Uso do `continue` com `while`

O `continue` é útil quando queremos pular uma iteração específica do laço mas continuar com as próximas iterações.

```python
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue
        print("estou no if") # note que esse print nunca será executado
    print(contador)
print(f"fora do while com contador = {contador}")
```

Neste exemplo, quando `contador` é igual a 3, a instrução `continue` faz com que o código retorne ao início do laço, pulando o `print(contador)` para esse valor específico. Assim, o programa imprime os números 1, 2, 4 e 5.


### Exercícios de Verificação

Qual será a saída do seguinte código?

```python
i = 1
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
```

Qual será a saída do seguinte código?

```python
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
```
No seguinte código, até que valor a variável `y` será incrementada?

```python
y = 5
while y < 10:
    if y == 8:
        break
    y += 1
```




### Cuidados com Laços Infinitos

É importante ter cuidado ao escrever loops `while` para evitar loops infinitos. Se a condição nunca se tornar falsa, o loop continuará executando indefinidamente. Isso pode causar travamento do programa ou consumo excessivo de recursos. Existem sitações especificas, como programação de sistemas embarcados, onde é necessário um laço de repetição infinito.  

!!! tip
    Para interromper um loop infinito em um ambiente de desenvolvimento, geralmente você pode usar a combinação de teclas `Ctrl + C`.


### Exercícios Práticos

Práticar é o segredo do sucesso para pragramação. 

- **Calculadora Simples**: Dado um número inteiro n >= 0, calcular n!.
