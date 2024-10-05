## Módulos e blibliotecas em Python

Módulos e bibliotecas são o meio de estender as funcionalidades básicas da linguagem. Permitem que nós programadores utilizem código previamente escrito, evitando a necessidade de reinventar a roda a cada novo projeto.

## Objetivos

- Explorar as bibliotecas padrão do Python e o que elas oferecem.
- Aprender a instalar e usar bibliotecas de terceiros.

## Módulos mais conhecidos

1. Bibliotecas padrão de Python:

`os`: Para interagir com o sistema operacional.
`datetime`: Para manipular datas e horas.
`collections`: Contém alternativas especializadas para containers padrão (como namedtuple, deque, Counter, etc.).
`math`: Funções matemáticas.
`json`: Para ler e escrever arquivos JSON.
`re`: Para trabalhar com expressões regulares.

1. Desenvolvimento web:

`Flask`: Um micro-framework para desenvolvimento web.
`Django`: Um framework de alto nível para desenvolvimento web.
`FastAPI`:  Estrutura web moderna para construção de APIs RESTful

1. Desenvolvimento de GUI:

`tkinter`: Biblioteca padrão para desenvolvimento de GUI.
`PyQt` ou `PySide`: Para criar interfaces de usuário modernas.
`Flet`: Interface cross plataforma
`Kivy`: Desenvolvimento de aplicativos móveis ou desktop.

1. Automatização e scraping:

`selenium`: Para automatização de navegadores web.
`BeautifulSoup`: Para parsing de HTML e XML.

1. Conexão com bancos de dados:

`sqlite3`: Interface para SQLite, um banco de dados relacional embutido.
`SQLAlchemy`: Um toolkit SQL e ORM (Object-Relational Mapping).

E muitoooo maissss.....

!!! progress
    Continuar...

## Importando Módulos

Para usar um módulo padrão do python, primeiro você precisa importá-lo. Isso é feito usando a palavra-chave `import`.

```python
import datetime
import calendar
```
## Instalando bibliotecas externas

Além das bibliotecas padrão, você pode instalar bibliotecas externas. Essas são coleções de módulos escritos por terceiros que fornecem funcionalidades adicionais, desde manipulação de dados, web, interface até aprendizado de máquina. Antes de realizar o `import` dessas bibliotecas é necessário realizar a sua instalação.

O `pip` é o gerenciador de pacotes do Python que facilita a instalação e gerenciamento dessas bibliotecas. Ele vem pré-instalado com o Python.

### Instalar uma biblioteca:

Use o comando `pip install nome_da_biblioteca`. Por exemplo, para instalar a biblioteca de requisições HTTP requests, você usaria `pip install requests`.

### Listar bibliotecas instaladas:

Use `pip list`.

| Package | Version |
|:---:|:---:|
| numpy | 1.20.1 |
| requests | 2.31.0 |

Ou `pip freeze`.

```bash
numpy==1.20.1
requests==2.31.0
```

### Desinstalar uma biblioteca:

Use `pip uninstall nome_da_biblioteca`.

### Instalar bibliotecas de um arquivo de requisitos:

Para projetos maiores, é comum especificar todas as dependências em um arquivo de requisitos, geralmente chamado `requirements.txt`. Para instalar todas as bibliotecas listadas neste arquivo, use `pip install -r requirements.txt`.

!!! progress
    Continuar...

## Módulo `datetime`

O módulo `datetime` é built-in do Python e fornece classes para manipular `datas e horas`.

### Classes Principais

- **date**: Representa uma data (ano, mês e dia).
- **time**: Representa uma hora do dia.
- **datetime**: Combina uma data e uma hora.
- **timedelta**: Representa a diferença entre duas datas ou horas.

### Criando Objetos

Para criar uma data:

```python
import datetime

d = datetime.date(2023, 10, 20)
print(d)  # Saída: 2023-10-20
```

### Diferença entre datas

Você pode subtrair duas datas para obter um objeto `timedelta`:

```python
d1 = datetime.date(2023, 10, 20)
d2 = datetime.date(2023, 11, 20)
delta = d2 - d1
print(delta.days)  # Saída: 31
```

### Adicionando ou subtraindo de uma data

Use `timedelta`:

```python
d = datetime.date(2023, 10, 20)
delta = datetime.timedelta(days=10)
new_date = d + delta
print(new_date)  # Saída: 2023-10-30
```

!!! progress
    Continuar...

## Módulo `calendar`

O módulo `calendar`  built-in do Python e fornece funções e classes para trabalhar com calendários.

### Funções Úteis

- **weekday()**: Retorna o dia da semana de uma data. 0 é segunda-feira e 6 é domingo.

```python
import calendar

print(calendar.weekday(2023, 10, 20))  # Saída: 4 (pois 20 de outubro de 2023 é uma sexta-feira)
```

- **monthrange()**: Retorna o dia da semana do primeiro dia e o número de dias do mês, para o ano e mês especificados.

```python
print(calendar.monthrange(2023, 10))  # Saída: (6, 31) (pois outubro de 2023 começa em um domingo e tem 31 dias)
```

### Dicas e Truques

1. O módulo `datetime` é mais adequado para manipulação de datas e horas, enquanto o módulo `calendar` é mais voltado para operações relacionadas a calendários.
2. Ao lidar com fusos horários, considere usar o módulo `pytz`.
3. Lembre-se de que a indexação dos dias da semana no módulo `calendar` começa em 0 para segunda-feira e vai até 6 para domingo.


!!! progress
    Continuar...


### Desafio

Esse foi uma breve descrição de utilização dos módulos `datetime` e `calendar`. Ambos os módulos têm muitas outras funcionalidades que podem ser exploradas na documentação oficial do Python.
O seu `desafio` é:

**Gestão de Datas**

Crie um programa Python que lida com operações de data e calendário. Este programa será interativo e solicitará ao usuário que insira dados para processamento.

O seu programa Python deverá:
    
    - Solicitar ao usuário que insira uma data no formato DD/MM/YYYY.

Uma vez fornecida a `data`, o programa deverá:

    - Mostrar o dia da semana correspondente à data inserida.
    - Calcular e exibir o número de dias que faltam até o final do ano a partir da data fornecida.
    - Converter a data para o fuso horário GMT+3 e mostrar o resultado.

Em seguida, o programa deverá usar o módulo `calendar` para:

    - Exibir o calendário do mês da data fornecida.
    - Determinar e informar se o ano da data fornecida é bissexto.
    - Listar todas as segundas-feiras do mês da data fornecida.


!!! progress
    Continuar...

## Interação com Sistemas de Arquivos

Python também oferece módulos, como `os`, para interagir com sistemas de arquivos. Ele permite navegar, criar, modificar e deletar arquivos e diretórios, entre outras operações.

Vamos conhecer apenas ver alguns métodos, sugiro se aprofundar lendo a documentação [https://docs.python.org/pt-br/3/library/os.html](https://docs.python.org/pt-br/3/library/os.html).


### Navegando pelo Sistema de Arquivos

- **Obter o diretório atual**:

```python
import os
print(os.getcwd())
```

- **Mudar de diretório**:

```python
os.chdir('/path/to/directory')
```

### Manipulando Diretórios

- **Criar um diretório**:

```python
os.mkdir('nome_do_diretorio')
```

- **Criar múltiplos diretórios**:

```python
os.makedirs('dir1/dir2/dir3')
```

- **Renomear um diretório**:

```python
os.rename('nome_atual', 'novo_nome')
```

- **Remover um diretório**:

```python
os.rmdir('nome_do_diretorio')
```

### Manipulando Arquivos

- **Listar arquivos e diretórios**:

```python
print(os.listdir('.'))
```

- **Verificar a existência de um arquivo ou diretório**:

```python
print(os.path.exists('nome_do_arquivo.txt'))
```

- **Obter informações sobre o arquivo**:

```python
info = os.stat('nome_do_arquivo.txt')
print(info)
```

- **Remover um arquivo**:

```python
os.remove('nome_do_arquivo.txt')
```


!!! progress
    Continuar...


### Exemplos Práticos

1. **Listar todos os arquivos de texto em um diretório**:

```python
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(txt_files)
```

2. **automação de tarefas**

`Cenário`: Imagine que você tenha uma pasta chamada "documentos" que contém vários arquivos de texto. Sua tarefa é criar uma automação que faça o seguinte:

1. Verifique se a pasta "documentos" existe. Se não existir, crie-a.
2. Navegue até a pasta "documentos".
3. Crie três arquivos de texto com conteúdos diferentes.
4. Liste todos os arquivos na pasta.
5. Renomeie um dos arquivos.
6. Verifique o tamanho de cada arquivo.
7. Mova um dos arquivos para uma subpasta chamada "arquivados".
8. Liste novamente todos os arquivos na pasta "documentos".

```python
import os

# Passo 1: Verifique se a pasta "documentos" existe. Se não, crie-a.
if not os.path.exists("documentos"):
    os.mkdir("documentos")

# Passo 2: Navegue até a pasta "documentos".
os.chdir("documentos")

# Passo 3: Crie três arquivos de texto com conteúdos diferentes.
with open("documento1.txt", "w") as file:
    file.write("Conteúdo do Documento 1.")
with open("documento2.txt", "w") as file:
    file.write("Conteúdo do Documento 2.")
with open("documento3.txt", "w") as file:
    file.write("Conteúdo do Documento 3.")

# Passo 4: Liste todos os arquivos na pasta.
lista_arquivos = os.listdir('.')
print(lista_arquivos)

# Passo 5: Renomeie um dos arquivos.
os.rename("documento2.txt", "documento_renomeado.txt")

# Passo 6: Verifique o tamanho de cada arquivo.
tamanho_arquivos = {file: os.stat(file).st_size for file in os.listdir('.') if os.path.isfile(file)}
print(tamanho_arquivos)

# Passo 7: Mova um dos arquivos para uma subpasta chamada "arquivados".
if not os.path.exists("arquivados"):
    os.mkdir("arquivados")
os.rename("documento3.txt", "arquivados/documento3.txt")

# Passo 8: Liste todos os arquivos na pasta "documentos" novamente.
lista_arquivos = os.listdir('.')
print(lista_arquivos)
```

## Desafio

Pratique o uso de modulos alterando o exemplo `automação de tarefas` para que ele organize os arquivos do seu computador. Esse script deve ser capaz de organizar os arquivos por extensão em diretórios diferentes. Por exemplo: imagens .jpg ou .png para a parta `img` arquivos .pdf para a pasta `pdf` e assim por diante. **ATENÇÃO: Muiti cuidado para não excluir seus arquivos pessoais**.