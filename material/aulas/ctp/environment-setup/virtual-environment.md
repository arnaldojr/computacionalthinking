## Configurando seu Ambiente de desenvolvimento

### O que é um ambiente virtual e por que é importante?

Um ambiente virtual em Python é um ambiente isolado que permite instalar e gerenciar pacotes de forma independente para diferentes projetos. Isso é importante porque ajuda a evitar conflitos entre as versões dos pacotes e garante que cada projeto tenha suas próprias dependências, sem afetar outros projetos ou o sistema operacional como um todo.

### Como criar um ambiente virtual usando venv

Neste exemplo vamos imaginar a seguinte estrutura de pastas do nosso projeto:

```kotlin
meu_projeto/
│   app.py
│   requirements.txt
└───data/
└───templates/
```
Nessa estrutura, `app.py` é o arquivo principal do projeto, `requirements.txt` lista todas as dependências do projeto, `data/` pode conter arquivos de dados, e `templates/` pode armazenar templates HTML para um projeto web...


`Para criar um ambiente virtual`, você pode usar o módulo `venv` que vem integrado com Python 3. 


Aqui estão os passos para criar e ativar um ambiente virtual:

!!!warning
    - Se estiver utilizando o `Windowns` da faculdade, execute o `Windowns PowerShell` e digite o comando a seguir para ajustar as permissões de acesso:

    ```PowerShell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

- Abra um terminal ou prompt de comando.

    - Certifique-se que está dentro da pasta do projeto, neste caso `meu_projeto`. Caso contrario, navegue até o diretório do projeto para criar o ambiente virtual.

- Execute o seguinte comando para criar um ambiente virtual chamado `meu_ambiente` (você pode escolher o nome que preferir):

    ```bash
    python -m venv meu_ambiente
    ```

!!! tip
    Geralmente usamos python -m venv venv para facilitar.

Isso criará um diretório chamado `meu_ambiente` contendo os arquivos necessários para o ambiente virtual.

A estrutura de pastas será parecida com essa:

```kotlin
meu_projeto/
│   app.py
│   requirements.txt
└───meu_ambiente/       # Ambiente virtual
│   │   └───bin/
│   │   └───include/
│   │   └───lib/
│   │   └───Scripts/    # Scripts de ativação do ambiente (Windows)
│   └───data/
└───templates/
```

### Como ativar o ambiente virtual

Dependendo do seu sistema operacional, o comando para ativar o ambiente virtual varia:

- Windows:

    ```bash
    .\meu_ambiente\Scripts\activate
    ```

- macOS e Linux:

    ```bash
    source meu_ambiente/bin/activate
    ```

Quando o ambiente virtual estiver `ativado`, você verá o nome do ambiente entre parênteses no início da linha de comando, indicando que qualquer pacote Python que você instalar será instalado nesse ambiente isolado.


```bash
(meu_ambiente) ➜ 
```

### Como desativar o ambiente virtual

Para sair do ambiente virtual e voltar ao ambiente global, basta digitar o comando `deactivate` no terminal:

```bash
deactivate
```

Isso retornará ao ambiente padrão do sistema.

## Instalação de pacotes no ambiente virtual

Com o ambiente virtual ativado, você pode instalar pacotes usando o `pip`, que é o gerenciador de pacotes do Python. Por exemplo, para instalar o pacote `requests`, você usaria o seguinte comando:

```bash
pip install requests
``` 

Os pacotes instalados no ambiente virtual estarão disponíveis apenas quando o ambiente estiver ativado.

### O arquivo `requirements.txt`

O `requirements.txt` é um arquivo que lista todas as dependências externas necessárias para o seu projeto. Cada linha neste arquivo especifica um pacote e, opcionalmente, uma versão específica. 

Por exemplo:

```makefile
matplotlib
numpy
opencv-python
flask==2.0.1
requests==2.25.1
beautifulsoup4==4.9.3
```

Quando alguém clona seu repositório ou deseja configurar o ambiente de desenvolvimento, pode instalar todas as dependências listadas no requirements.txt executando o seguinte comando:

```bash
pip install -r requirements.txt
```

Isso `garante` que todos tenham as mesmas versões dos pacotes instalados, tornando o desenvolvimento e a implantação mais consistentes.

Quando você usa um ambiente virtual `(meu_ambiente)`, o `requirements.txt` ainda desempenha o mesmo papel. No entanto, ao instalar as dependências listadas no arquivo, você deve garantir que o `ambiente virtual esteja ativado`. Isso garantirá que os pacotes sejam `instalados no ambiente isolado`, em vez de no ambiente global do sistema.

### Criando o arquivo requirements.txt para o seu projeto

Você deve seguir os seguintes passos para criar o arquivo de requirements.txt do seu projeto. 

1. **`Ative o ambiente virtual`**

    Veja como na seção anterior. Não faça os próximos passos sem ativar seu ambiente virtual

2. Instale as dependências do projeto:

    Use o pip para instalar qualquer biblioteca que seu projeto necessite. Por exemplo:

    ```bash
    pip install flask
    pip install requests
    pip install beautifulsoup4
    ```

3. Gere o arquivo requirements.txt:

    Após instalar todas as dependências necessárias, você pode gerar o requirements.txt usando o seguinte comando:
    
    ```bash
    pip freeze > requirements.txt
    ```

    Esse comando lista todas as bibliotecas instaladas no ambiente (virtual ou global) e suas versões, e redireciona a saída para criar ou sobrescrever o arquivo requirements.txt.

4. Verifique o conteúdo do arquivo:

    Você pode abrir o requirements.txt em um editor de texto para verificar se todas as dependências e suas versões estão listadas corretamente. O arquivo pode ter uma aparência semelhante a esta:
    
    ```makefile
    Flask==2.0.1
    requests==2.25.1
    beautifulsoup4==4.9.3
    ```
Pronto! arquivo criado e atualizado com sucesso!

## Usando o arquivo `.gitignore` em seu projeto

O arquivo `.gitignore` é usado em projetos que utilizam o sistema de controle de versão Git. Ele especifica quais arquivos ou diretórios devem ser ignorados pelo Git, ou seja, não devem ser rastreados ou incluídos no repositório. 

**É uma boa prática incluir um arquivo .gitignore em todos os seus projetos Git para evitar o commit acidental de arquivos desnecessários ou sensíveis.**

### Como criar e configurar um arquivo .gitignore

1. Crie o arquivo .gitignore:

    Na raiz do seu projeto, crie um arquivo chamado `.gitignore`. Você pode fazer isso usando um editor de texto ou pelo terminal:

    ```bash
    touch .gitignore
    ```

    Deve ficar parecico com o exemplo a seguir:

    ```kotlin
    meu_projeto/
    │   app.py
    │   requirements.txt    # requirements 
    │   .gitignore          # gitignore
    └───meu_ambiente/       # Ambiente virtual
    └───data/
    └───templates/
    ```


2. Adicione regras ao arquivo:

    Abra o arquivo .gitignore em um editor de texto e adicione regras para especificar quais arquivos ou diretórios devem ser ignorados. Por exemplo:

    ```bash
    # Ignorar todos os arquivos .log
    *.log

    # Ignorar o diretório de ambiente virtual
    meu_ambiente/
    venv/

    # Ignorar arquivos de configuração sensíveis
    config.yaml

    # Ignorar arquivos temporários
    temp/
    ```

    Cada linha do arquivo .gitignore representa uma regra. Os caracteres # são usados para comentários.

3. Salve e feche o arquivo:

    Após adicionar todas as regras necessárias, salve e feche o arquivo .gitignore.

4. Verifique o status do Git:

    No terminal, use o comando `git status` para verificar se os arquivos especificados estão sendo devidamente ignorados pelo Git.

## Pronto agora já está tudo configurado para o seu projeto. 