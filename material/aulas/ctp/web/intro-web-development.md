
## Introdução ao Desenvolvimento Web

A web está presente em nosso dia-a-dia e o seu desenvolvimento está relacionado ao processo de criação de sites e aplicações para a internet. Ele envolve uma variedade de disciplinas e tecnologias que permitem a construção de conteúdo interativo e dinâmico que pode ser acessado por usuários através de navegadores web (chrome, safari, firefox...). 

### Componentes do Desenvolvimento Web

Vamos definir alguns personagens que estão presentes no desenvolvimento web, geralmente dividimos em duas áreas principais:

![https://www.alura.com.br/artigos/o-que-e-front-end-e-back-end](https://www.alura.com.br/artigos/assets/o-que-e-front-end-e-back-end/back-end-sincronizacao-banco-dados-navegadores.jpg)

- `Front-end`: Também conhecido como "lado do cliente", refere-se à parte da aplicação web que os usuários veem e interagem. Ele é construído usando 3 principais tecnologias que são executadas no navegador do usuário:
    
    - `HTML` (HyperText Markup Language): É a espinha dorsal de qualquer página web, responsável pela estrutura e pelo conteúdo. HTML define a estrutura básica de uma página, como cabeçalhos, parágrafos, listas e links.
    - `CSS` (Cascading Style Sheets): É usado para controlar a apresentação, o layout e o design da página HTML. CSS permite estilizar elementos HTML, definindo cores, fontes, espaçamentos, alinhamentos e muito mais.
    - `JavaScript`: É uma linguagem de programação que permite adicionar interatividade e dinamismo às páginas web. Com JavaScript, é possível criar efeitos de animação, validar formulários, realizar operações assíncronas com AJAX e manipular o DOM (Document Object Model).

- `Back-end`: Conhecido como "lado do servidor", é responsável pela lógica de negócios, gerenciamento de banco de dados e servidor da aplicação.As tecnologias comuns usadas no back-end incluem:
    - `Linguagens de Programação`: Como Python, Ruby, PHP, Node.js e Java. Essas linguagens são usadas para desenvolver a lógica do servidor, manipular dados e interagir com o banco de dados.
    - `Frameworks`: Como Flask e Django para Python, Ruby on Rails para Ruby, Express para Node.js e Spring para Java. Os frameworks fornecem uma estrutura e um conjunto de ferramentas para facilitar o desenvolvimento do back-end, incluindo roteamento de URL, manipulação de requisições e respostas, e integração com bancos de dados.
    - `Servidores Web`: Como Apache, Nginx e IIS, que são responsáveis por receber as requisições HTTP dos clientes, passá-las para a aplicação back-end e enviar as respostas de volta ao cliente.

- `Banco de dados`: É o componente que armazena e gerencia os dados da aplicação. Ele é fundamental para qualquer aplicação web que precisa persistir informações, como dados de usuários, conteúdo de páginas ou registros de transações. Os tipos comuns de bancos de dados incluem:

    - `Bancos de Dados Relacionais`: Como MySQL, PostgreSQL e SQLite, que organizam os dados em tabelas e usam SQL (Structured Query Language) para consulta e manipulação de dados.
    - `Bancos de Dados Não Relacionais (NoSQL)`: Como MongoDB, Cassandra e Redis, que são mais flexíveis em termos de estrutura de dados e são frequentemente usados em aplicações que requerem escalabilidade horizontal e manipulação de grandes volumes de dados.
 

### Dinâmica Cliente-Servidor

No coração do desenvolvimento web está o modelo cliente-servidor, uma arquitetura de rede que separa clientes (navegadores) e servidores (onde os sites são armazenados e executados). Quando um usuário acessa um site, o navegador (cliente) envia uma solicitação HTTP ao servidor, que então processa a solicitação e envia de volta os dados necessários (geralmente em forma de HTML, CSS e JavaScript) para o navegador exibir a página web.

### Protocolo HTTP

O protocolo HTTP (Hypertext Transfer Protocol) é o fundamento da comunicação de dados na web. Ele define um conjunto de regras para a transferência de arquivos (textos, imagens, som, vídeo e outros dados) na internet.

 O HTTP é um protocolo baseado em solicitação-resposta, onde o cliente envia uma solicitação ao servidor e espera uma resposta.

refs:
- https://www.alura.com.br/artigos/o-que-e-front-end-e-back-end
- https://realpython.com/python-sockets/ 


!!! progress
    Continuar...


## Prática, um pouco sobre sockets

Sockets são uma abstração de endpoints de comunicação que permitem a `troca de dados` entre `processos em uma rede` ou entre processos na mesma máquina. Eles são a base para a construção de aplicações de rede, como servidores web, clientes de email, jogos online, entre outros.

### Como Utilizar Sockets em Python

Python oferece uma biblioteca chamada `socket` que fornece uma interface de alto nível para trabalhar com sockets. 

Vamos dar uma olhada em algums pontos básicos de como criar um socket em Python:

1. Importar e Criar um Objeto Socket:

    - Antes de usar sockets, você deve importar a biblioteca socket e para criar, utilizamos o método `socket.socket()`, especificando o `tipo de endereço` e o `protocolo de comunicação`:

    ```python
    import socket

    # Cria um socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ```
    
    - `socket.AF_INET`: Especifica o domínio do endereço do socket. `AF_INET` indica que o socket usará endereços IPv4.
    - `socket.SOCK_STREAM`: Especifica o tipo do socket. `SOCK_STREAM` indica que o socket será do tipo TCP (Transmission Control Protocol), que é orientado a conexão e fornece um fluxo de bytes confiável.

2. Vincular o Socket a um Endereço e Porta (Servidor)

    - Para um servidor, você precisa vincular o socket a um `endereço IP` e uma `porta` para escutar por conexões de entrada:

    ```python
    server_address = ('localhost', 10000)  # Endereço e porta do servidor
    sock.bind(server_address)
    ```

    - `bind()`: para associar o socket a um endereço IP e uma porta específico.

3. Escutar por Conexões de Entrada (Servidor)

    - Após vincular o socket, o servidor deve escutar por conexões de entrada:

    ```python
    sock.listen()
    ```

    - `listen()`: para colocaro socket em modo de escuta, permiti que o socket aceite conexões.

4. Aceitar Conexões (Servidor)

    - O servidor pode aceitar uma conexão de um cliente usando o método accept(), que bloqueia a execução até que uma conexão seja estabelecida:

    ```python
    connection, client_address = sock.accept()
    ```
    
    - `accept()`:para aceitar uma conexão de um cliente


5. Estabelecer Conexão (Cliente)

    - Para um cliente, você deve estabelecer uma conexão com o servidor especificando o endereço IP e a porta do servidor:

    ```python
    server_address = ('localhost', 10000)  # Endereço e porta do servidor
    sock.connect(server_address)
    ```

    - `connect()`: para estabelecer uma conexão com o servidor

6. Enviar e Receber Dados

    - Tanto o cliente quanto o servidor podem enviar e receber `bytes` usando os métodos send() e recv():
    - **`A comunicação sempre é em bytes, não existe comunicação de string ou int, float... é tudo byte!`**
    - os metodos encode() e decode(): codificá em bytes uma string e decodifica de bytes para string.

    ```python
    # Enviar dados
    message = 'Olá, mundo!'
    sock.sendall(message.encode())

    # Receber dados
    data = sock.recv(1024)
    print(f"Recebido: {data.decode()}")
    ```

    - `sendall()`: para enviar dados 
    - `recv()`: para receber dados. O argumento especifica o número máximo de bytes a serem lidos. Retorna os dados recebidos como um objeto de bytes.

7. Fechar o Socket

    - Após a comunicação ser concluída, é importante fechar o socket para liberar os recursos:

    ```python
    sock.close()
    ```

    - `close()`: fecha a conexão.


Agora que já temos uma idéia das principais funções, definir uma estrutura de comunicação client-server da seguinte forma:

![](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg)


!!! progress
    Continuar...


!!! exercise "Question"
    Antes de continuar na aula, pense e responda:

    - Considerando dois processos que precisam se comunicar usando TCP/IP ou UDP/IP, qual deve ser o primeiro passo para iniciar a comunicação?

    !!! answer
        Para iniciar a comunicação, um dos processos deve estar em execução no modo de "escuta" (listening), aguardando uma solicitação de conexão do outro processo. Esse processo em modo de escuta é geralmente chamado de servidor. O outro processo, conhecido como cliente, pode iniciar a comunicação a qualquer momento, estabelecendo uma conexão com o servidor.


!!! progress
    Continuar...


## Projeto loop-back

Vamos criar um projeto de `loopback` cliente-servidor, onde a comunicação entre o cliente e o servidor ocorrerá no mesmo computador, utilizando o endereço de loopback `127.0.0.1`.

![](https://files.realpython.com/media/sockets-loopback-interface.44fa30c53c70.jpg)


Basicamente vai funcionar da seguinte forma: 

- Iniciar o Servidor:

    - O servidor será iniciado primeiro e ficará escutando em um endereço IP de loopback (127.0.0.1) em uma porta específica (por exemplo, 65432).
    - O servidor criará um socket, vinculará esse socket ao endereço e porta especificados e começará a escutar por conexões de entrada.

- Conectar o Cliente:

    - O cliente será iniciado em seguida e tentará se conectar ao servidor usando `o mesmo endereço de loopback e porta` em que o servidor está escutando.
    - O cliente criará um socket e usará o método `connect()` para estabelecer uma conexão com o servidor.

- Comunicação:

    - Após a conexão ser estabelecida, o cliente poderá enviar dados ao servidor usando o método `send()` ou `sendall()` do socket.
    - O servidor receberá os dados enviados pelo cliente usando o método `recv()` do socket.
    - O servidor vai responder ao cliente enviando dados recebidos de volta, e o cliente vai receber esses dados.

- Encerramento da Conexão:

    - O código é encerrado quando a comunicação for concluída. 
    - O cliente e o servidor fecham seus respectivos sockets para encerrar a conexão. 


### Criando um Servidor Simples

Para criar um **`servidor`** simples usando sockets, você precisa seguir os seguintes passos:

- `Criar um Socket`: Use o método socket() para criar um objeto de socket.
- `Vincular o Socket a um Endereço e Porta`: Use o método bind() para associar o socket a um endereço IP e uma porta específicos.
- `Colocar o Socket em Modo de Escuta`: Use o método listen() para permitir que o socket aceite conexões.
- `Aceitar uma Conexão`: Use o método accept() para aceitar uma conexão de um cliente.
- `Enviar e Receber Dados`: Use os métodos send() e recv() para enviar e receber dados.

O servidor simples:

```python
import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta que o servidor está ouvindo

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor escutando...")
    conn, addr = s.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recebido: {data.decode('utf-8')}")
            conn.sendall(data) 
```

### Criando um Cliente Simples

Para criar um **`cliente`** simples que se conecta a um servidor usando sockets, você precisa seguir os seguintes passos:

- `Criar um Socket`: Use o método socket() para criar um objeto de socket.
- `Conectar o Socket ao Servidor`: Use o método connect() para estabelecer uma conexão com o servidor.
- `Enviar e Receber Dados`: Use os métodos send() e recv() para enviar e receber dados.
- `Fechar o Socket`: Use o método close() para fechar a conexão.

O cliente simples:

```python
import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta que o servidor está ouvindo

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Codifique a string 'Olá, servidor!' usando UTF-8 antes de enviá-la
    mensagem = 'Olá, servidor!'.encode('utf-8')
    s.sendall(mensagem)
    data = s.recv(1024)

print(f"Recebido: {data.decode('utf-8')}")

```

!!! exercise choice "Question"
    Teste e valide o funcionamento do client-server simples. Para isso, siga os seguintes passos:
    
    - Crie uma nova pasta de projeto;
    - Crie um arquivo python chamado servidor.py e adicione o código fornecido para o servidor;
    - Crie um arquivo python chamado cliente.py e adicione o código fornecido para o cliente;
    - Em um terminal, execute o código servidor.py;
    - Em um **novo** terminal, execute o código cliente.py;
    - obseve o que aconteceu  


Responda as pergutas a seguir para validar seus conhecimentos sobre sockets

!!! exercise choice "Question"
    Qual dos seguintes métodos é utilizado para vincular um endereço e uma porta a um socket em Python?

    - [ ] `connect()`
    - [x] `bind()`
    - [ ] `listen()`
    - [ ] `accept()`
    
    !!! answer
        O método `bind()` é utilizado para vincular um endereço e uma porta a um socket em Python.


!!! exercise choice "Question"
    Em uma comunicação cliente-servidor, qual dos seguintes métodos é utilizado pelo servidor para escutar por conexões de entrada?

    - [ ] `connect()`
    - [ ] `bind()`
    - [x] `listen()`
    - [ ] `accept()`
    
    !!! answer
        O método `listen()` é utilizado pelo servidor para escutar por conexões de entrada.


!!! exercise choice "Question"
    Qual das seguintes alternativas é verdadeira sobre o método `accept()` em um servidor de socket?

    - [ ] Ele é usado para enviar dados para um cliente.
    - [ ] Ele é usado para receber dados de um cliente.
    - [x] Ele é usado para aceitar uma conexão de um cliente.
    - [ ] Ele é usado para escutar por conexões de entrada.
    
    !!! answer
        O método `accept()` é usado por um servidor de socket para aceitar uma conexão de um cliente.


!!! exercise choice "Question"
    Em uma comunicação de rede usando sockets, qual das seguintes afirmações é verdadeira sobre o endereço IP `127.0.0.1`?

    - [ ] É usado para se referir a um dispositivo remoto na rede.
    - [x] É o endereço de loopback que se refere ao próprio dispositivo.
    - [ ] É o endereço IP padrão para todos os roteadores.
    - [ ] É um endereço IP reservado para uso futuro.
    
    !!! answer
        O endereço IP `127.0.0.1` é conhecido como endereço de loopback e é usado para se referir ao próprio dispositivo na rede.


!!! progress
    Continuar...


## Projeto WebChat via socket

Legal, agora que já conhecemos e sabemos criar uma conexão socket, vamos avançar criando uma aplicação Client-Server por meio de um chat usando sockets. Basicamente, esse novo sistema consiste de um servidor que gerencia as mensagens de multiplos clientes conectados.

![](https://files.realpython.com/media/sockets-ethernet-interface.aac312541af5.jpg)


!!! exercise "Question"
    1. Clone o repositório.

    ```bash
    git clone https://github.com/arnaldojr/client-server.git
    cd client-server
    ```

    2. Inicie `primeiramente` o servidor, nesse caso será o pc do professor será o HOST:

    ```bash
    python server.py
    ```

    3. Em outro terminal, inicie um ou mais clientes. Neste caso é importante ajustar o IP do Host:

    ```bash
    python client.py
    ```

    4. Digite seu nome de usuário e comece a enviar mensagens 😁. Para sair do programa, digite "sair".

