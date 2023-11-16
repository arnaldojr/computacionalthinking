## Trabalhando com Arquivos em Python

Em Python, fa manipulação de arquivos é muito simples, além de ser uma habilidade essencial, pois permite que os programas interajam com dados persistentes, realizem análises, modifiquem e armazenem resultados para uso futuro. 

Note que, neste conteúdo, estamos focando na manipulação de arquivos locais, e não abordaremos banco de dados.

## Introdução ao Trabalho com Arquivos

Em Python, os arquivos são objetos que oferecem uma interface para interagir com conteúdo armazenado no sistema de arquivos do computador. A manipulação de arquivos é fundamental para muitas operações, desde a simples leitura de dados até operações mais complexas de processamento de dados.

### Objeto de Arquivo

Quando abrimos um arquivo em Python usando a função `open()`, obtemos um objeto de arquivo. Este objeto fornece métodos e atributos que nos permitem realizar operações como ler, escrever e fechar o arquivo.

```python
# Abre um arquivo chamado "exemplo.txt" para leitura
arquivo = open("exemplo.txt", "r")

# Lê o conteúdo do arquivo
conteudo = arquivo.read()

# Fecha o arquivo após a leitura
arquivo.close()

# Agora você pode usar o conteúdo do arquivo
print(conteudo)
```
A partir do Python 3.3, é recomendado usar a sintaxe `with open` para abrir arquivos, pois ele garante que o arquivo seja fechado automaticamente após a conclusão das operações.

```python
# Abre um arquivo chamado "exemplo.txt" para leitura usando o bloco with
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()

# O arquivo é automaticamente fechado quando o bloco with é concluído
print(conteudo)
```


!!! progress
    Continuar...


### Modos de Abertura

Existem vários modos em que um arquivo pode ser aberto:

- **'r'**: Modo de leitura. (padrão)
- **'w'**: Modo de escrita. Cria um novo arquivo ou sobrescreve um existente.
- **'a'**: Modo de anexação. Escreve no final do arquivo sem sobrescrever o conteúdo existente. 

Podemos especificar se o arquivo deve ser tratado como modo binário ou texto.

- **'b'**: Modo binário. Usado para arquivos não-textuais como imagens ou arquivos binários.
- **'t'**: Modo de texto. (padrão) Usado para arquivos de texto.

### Exemplos Simples e Práticos

1. **Ler um arquivo e imprimir seu conteúdo**:

```python
with open("exemplo.txt", "r") as file:
    conteudo = file.read()
    print(conteudo)
```

2. **Ler uma imagem e imprimir seu conteúdo**:

```python
with open("exemplo.jpg", "rb") as file:
    conteudo = file.read()
    print(conteudo)
```

3. **Escrever uma strings em um arquivo**:

```python
# Abre o arquivo para escrita
with open("exemplo.txt", "w") as file:
    file.write("Conteúdo de exemplo.")
```

4. **Escrever uma lista de strings em um arquivo**:

```python
lines = ["Linha 1", "Linha 2", "Linha 3"]
with open("exemplo.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
```


!!! progress
    Continuar...


## Lendo e Escrevendo Arquivos de Texto (`.txt`)


### Leitura:

Para entender como utilizar os métodos de leitura vamos assumir que já exite o arquivo `exemplo.txt`, com o seguinte conteúdo.

```python
Olá universo!
Pensamento computacional
Com Python é facil.

```

Usamos `read()` para ler todo o arquivo, por padrão o arquivo é lido como string (texto).  

```python
with open("exemplo.txt", "r") as file:
    conteudo = file.read()
print(conteudo)
```

!!! Tip
    O erro `FileNotFoundError: [Errno 2] No such file or directory: 'exemplo.txt'` significa que ou o arquivo não existe ou está em um diretório diferente do script python.


Abrindo um arquivo de um diretório diferente: Caso o script python e o arquivo não estejam no mesmo diretório é necessário passar o caminho `path` relativo ou completo na hora da leitura.

```python
with open("c:\\<caminho_ate_o_arquivo>\exemplo.txt", "r") as file:
    conteudo = file.read()
print(conteudo)
```

Podemos ler apenas uma parte do arquivo:

- Definindo a quantidade de caracteres: `read(10)` retorna os 10 primeiros caracteres do arquivo `Olá unive`.

```python
with open("exemplo.txt", "r") as file:
    conteudo = file.read(10)
print(conteudo)
```
O resultado é: `Olá unive`.

- Lendo uma linha inteira: `readline()` retorna o conteudo da linha toda `\n`.  

```python
with open("exemplo.txt", "r") as file:
    conteudo = file.readline()
print(conteudo)
```

Se tudo deu certo, o resultado será: `Olá universo!`. 

Para para ler mais uma linha do arquivo temos que realizar mais um `readline()`, para facilitar pode ser iterado em um laço for.

```python
with open("exemplo.txt", "r") as file:
    conteudo = []
    for linha in file:
        conteudo.append(linha.strip())
print(conteudo)
```

O resultado será: `['Olá universo!', 'Pensamento computacional', 'Com Python é facil.']`

!!! Tip
    Para ler o arquivo e remover o caractere de nova linha `\n` de cada linha, você pode usar o método `strip()`. Esse método retorna uma cópia da string original, removendo os espaços em branco no início e no final da string. No contexto de leitura de arquivos, ele efetivamente remove os caracteres de nova linha `\n` do final das linhas.


### Escrita:

Ao escrever em um arquivo, temos que saber que:

- Se tentarmos abrir um arquivo que não existe, um novo arquivo será criado;
- Se um arquivo já existir, seu conteúdo será apagado e um novo conteúdo será adicionado ao arquivo.
- Pode ser utilizado `\n` para dar quebra de linha ao escrever no arquivo.
- Para escrever em um arquivo em Python, precisamos abri-lo no modo de gravação passando `w` dentro de `open()` como segundo argumento.

Se o arquivo `exemplo2.txt` não existe. Vamos ver o que acontece se escrevermos conteúdo nele.

```python
with open("exemplo2.txt", "w") as file:
    file.write("Olá, Mundo!\n")
    file.write("Pensamento Computacional")
```

!!! progress
    Continuar...

## Trabalhando com CSVs

O módulo `csv` do Python facilita a leitura e a escrita de arquivos CSV.

### Leitura:
```python
import csv
with open('exemplo.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### Escrita:
```python
import csv
with open('exemplo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["nome", "idade", "profissão"])
    writer.writerow(["João", 30, "Engenheiro"])
```


!!! progress
    Continuar...


## Trabalhando com Arquivos JSON

JSON (JavaScript Object Notation) é um formato leve de troca de dados que é fácil de ler e escrever para humanos e fácil de analisar e gerar para máquinas. Em Python, o módulo `json` facilita a leitura e escrita de arquivos JSON.

Ao trabalhar com JSON em Python, os objetos JSON são convertidos em tipos de dados Python, como dicionários, listas, strings, números, booleanos (`true`/`false` em JSON se tornam `True`/`False` em Python) e `null` (em JSON) se torna `None` em Python.


### Lendo de um Arquivo JSON

Para ler dados de um arquivo JSON, você pode usar o método `load()` do módulo `json`.

```python
import json

with open("dados.json", "r") as file:
    data = json.load(file)
print(data)
```

### Escrevendo em um Arquivo JSON

Para escrever dados em um arquivo JSON, você pode usar o método `dump()` do módulo `json`.

```python
import json

pizza = {
    "marguerita": {
        "tamanho": "médio",
        "preço": 22.99,
        "ingredientes": ["tomate", "muçarela", "manjericão"],
        "queijo_extra": False
    },
    "pepperoni": {
        "tamanho": "grande",
        "preço": 55.67,
        "ingredientes": ["pepperoni", "muçarela"],
        "queijo_extra": True
    },
    "vegetariana": {
        "tamanho": "pequena",
        "preço": 10.5,
        "ingredientes": ["cogumelos", "pimentão verde", "cebolas"],
        "queijo_extra": False
    },
    "cliente": {
        "nome": "Janaina Faminta",
        "telefone": None,
        "email": "jana@email.com"
    }
}


with open("dados_pizza.json", "w") as file:
    json.dump(pizza, file)
```

### Trabalhando com Strings JSON

- Para converter uma string JSON em um objeto Python:

```python
import json

data_string = '{"nome": "Renato", "idade": 30, "cidade": "São Paulo"}'
data_object = json.loads(data_string)
print(data_object)
```

- Para converter um objeto Python em uma string JSON:

```python
data_object = {"nome": "Arnaldo", "idade": 25, "cidade": "Rio de Janeiro"}
data_string = json.dumps(data_object, indent=4)
print(data_string)
```

!!! Tip
    O argumento `indent` em `dumps()` é usado para formatar a saída JSON, tornando-a mais legível.


#### Diferença entre `load()` e `loads()`

- `json.load()`: Este método é usado para ler dados JSON de um arquivo. Ele lê o arquivo e converte o conteúdo JSON em um objeto Python.
  
- `json.loads()`: Este método é usado para analisar uma string JSON e convertê-la em um objeto Python.

### Diferença entre `dump()` e `dumps()`

- `json.dump()`: Este método é usado para escrever dados JSON em um arquivo.
  
- `json.dumps()`: Este método converte um objeto Python em uma string JSON.


!!! progress
    Continuar...


### Arquivos Binários

Ao trabalhar com arquivos não-textuais, como imagens ou executáveis, utilizamos o modo binário. 

```python
# Lendo um arquivo binário
with open("imagem.jpg", "rb") as file:
    data = file.read()
```

### Tratamento de Exceções

É importante tratar exceções ao trabalhar com arquivos para evitar falhas no programa. O erro mais comum é o `FileNotFoundError`.

```python
try:
    with open("arquivo_inexistente.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
```

## Boas Práticas ao Trabalhar com Arquivos

- Sempre use o gerenciador de contexto `with` ao abrir arquivos para garantir que eles sejam fechados corretamente.
- Manipule exceções ao trabalhar com arquivos para lidar com possíveis erros.
- Evite a leitura de arquivos inteiros na memória se eles forem muito grandes. Existem tecnicas e bibliotecas mais apropriadas para isso, como `Pandas`


