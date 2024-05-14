## E agora, por onde começar?

- Perfil do estudante
- Instalação e configuração do Python 3.x
- Criação da conta no github
- Instalação da IDE de programação
- Validação e testes de instalação da infraestrutura


## Conhecendo o perfil de estudante

Para começar, eu quero conhecer um pouco o perfil da nossa turma. 


!!! exercise
    Responda o questionário:
 
    > - [https://forms.gle/UYZBeFRXjN81NxsK9](https://forms.gle/UYZBeFRXjN81NxsK9)


!!! progress
    Continuar...

## Instalação e configuração do Python 3.x


!!! exercise
    1. Acesse o site oficial do Python em [https://www.python.org/](https://www.python.org/).
    2. Clique em "Downloads" e escolha a versão mais recente do Python 3.x para o seu sistema operacional.
    3. Siga as instruções de instalação. Durante a instalação, certifique-se de marcar a opção ``"Add Python 3.x to PATH"`` para facilitar a execução do Python no terminal.
    

!!! exercise choice "Question"
    Após a instalação, abra o terminal ou prompt de comando (cmd) e digite `python --version` para confirmar que o Python foi instalado corretamente e escolha a alternativa que mais se aproxima da corerta.

    - [X] Python 3.11.4
    - [ ] Python 2.8
    - [ ] Python 


    !!! answer
        Versão 3 do Python instalada.

!!! progress
    Continuar...


## Introdução ao Git e GitHub

### **O que é Git?**  
   Git é um sistema de controle de versão distribuído que permite que os desenvolvedores colaborem em projetos de qualquer escala. Ele rastreia as mudanças no código, facilitando a colaboração e a resolução de conflitos.

### **Primeiros passos com Git:**  

!!! exercise
   - Instale o Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)

!!! exercise
   - Após a instalação, abra o terminal ou prompt de comando (cmd) e digite os comandos abaixo para configurar sua identidade:  

     ```bash
     git config --global user.name "Seu Nome"
     git config --global user.email "seuemail@email.com"
     ```

### **O que é GitHub?**  
   GitHub é uma plataforma de hospedagem de código que utiliza o Git para controle de versão. Ele permite que os desenvolvedores colaborem em projetos e compartilhem seu trabalho com o mundo.

### Criação da conta no GitHub

!!! exercise
    1. Acesse [https://github.com/](https://github.com/).
    2. Clique em "Sign up" no canto superior direito.
    3. Preencha seus dados e siga as instruções para criar sua conta.
    4. Após a criação da conta, verifique seu e-mail para confirmar o registro.
    
### **Primeiros passos no GitHub:**  

Com o git/github podemos trabalhar de forma colaborativa e organizada. Cada projeto está organizado em um ``repositório`` isso inclui o site da nossa disciplina. 

Basicamente, podemos criar novos repositório publicos ou privados para os nossos projetos, clonar respositórios para trabalhar em nossa maquina local ou realizar fork de outros projetos. 

A idéia do fork é que ele faz o clone para o seu repositório do Github e mantem uma "conexão" entre o que você fez e o original. Isso vai permitir você manter atualizado o seu repositório com o da disciplina.  

!!! exercise

    1. **Faça o fork do repositório da disciplina:**  
       - Acesse [https://github.com/](https://github.com/) e faça login na sua conta.
       - Acesse [https://github.com/arnaldojr/computacionalthinking](https://github.com/arnaldojr/computacionalthinking) e clique em ``fork``.
    
    2. **Clone o repositório para sua máquina local:**  
       - Na página principal do seu novo repositório no GitHub, clique no botão 'Code' e copie a URL fornecida.
       - Abra o terminal ou prompt de comando e navegue até o diretório onde deseja clonar o repositório.
       - Digite `git clone [URL_DO_REPOSITÓRIO]`. Por exemplo:  
         ```bash
         git clone https://github.com/seu_usuario/nome_do_repositorio.git
         ```
    
    3. **Trabalhe com o Git localmente: (opcional por enquanto)**
       - 
       - Navegue até o diretório do repositório clonado: `cd nome_do_repositorio`.
       - Faça as alterações desejadas nos arquivos ou adicione novos arquivos.
       - Adicione as alterações ao Git usando:  
         ```bash
         git add .
         ```
       - Faça um commit das alterações com uma mensagem descritiva:  
         ```bash
         git commit -m "Descrição das alterações feitas"
         ```
       - Envie as alterações para o GitHub (push):  
         ```bash
         git push origin master
         ```

!!! Warning
    Lembre-se de que a prática leva à perfeição. Quanto mais você trabalhar com Git e GitHub, mais confortável se sentirá com essas ferramentas!

## Instalação da IDE de programação

Ambientes de Desenvolvimento Integrado (IDEs) são ferramentas que fornecem um conjunto de funcionalidades para facilitar o processo de desenvolvimento de software. Eles geralmente incluem um editor de código, ferramentas de depuração e, muitas vezes, recursos para design de interface, controle de versão, entre outros.

1. **Visual Studio Code (VS Code): (vamos usar durante o curso)**  
   - Uma IDE leve e extensível, popular não apenas para Python, mas para uma variedade de linguagens.
   - Com a extensão Python, o VS Code oferece linting, debugging, IntelliSense, e suporte para Jupyter Notebooks.
   - [Site oficial do VS Code](https://code.visualstudio.com/)

2. **PyCharm:**  
   - Desenvolvido pela JetBrains, é uma das IDEs mais completas para Python.
   - Oferece recursos avançados como análise de código, um debugger visual e integração com muitos frameworks e ferramentas populares de Python.
   - Existe em duas versões: Community (gratuita) e Professional (paga).
   - [Site oficial do PyCharm](https://www.jetbrains.com/pycharm/)

3. **Jupyter Notebook:(vamos usar durante o curso)**  
   - Mais do que uma IDE tradicional, é uma aplicação web que permite criar e compartilhar documentos que contêm código, equações, visualizações e texto narrativo.
   - Popular para análise de dados, ciência de dados e aprendizado de máquina.
   - [Site oficial do Jupyter](https://jupyter.org/)

4. **Thonny:**  
   - Uma IDE para ensino e aprendizado de programação Python. Ideal para iniciantes.
   - Vem com Python incluído e um debugger simples de usar.
   - [Site oficial do Thonny](https://thonny.org/)

5. **Spyder:**  
   - Uma IDE voltada para cientistas, engenheiros e analistas de dados.
   - Integra-se bem com bibliotecas populares de Python como SciPy, NumPy e Matplotlib.
   - [Site oficial do Spyder](https://www.spyder-ide.org/)

!!! Warning
    No entanto, é válido ressaltar que, para simplesmente escrever código Python, até mesmo editores de texto básicos como o ``Bloco de Notas`` podem ser utilizados. No entanto, uma IDE especializada oferece ferramentas e recursos que facilitam e enriquecem o processo de desenvolvimento.

!!! note
    Para os propósitos da nosso disciplina, eu optei por utilizar o ``VS Code``, mas você pode escolher a IDE que melhor se adapte às suas necessidades e ao conteúdo que deseja abordar. Seja qual for sua escolha, o mais importante é a prática e a familiaridade com as ferramentas.


### Instalação da IDE de programação: Visual Studio Code (VS Code)

O Visual Studio Code é uma IDE leve, mas poderosa, que suporta uma variedade de linguagens de programação. É altamente extensível e tem uma grande comunidade que contribui com extensões úteis.

### Passos para instalação:

!!! exercise

    -  **Download:**  
        - Acesse o site oficial do VS Code em [https://code.visualstudio.com/](https://code.visualstudio.com/).
        - Clique em "Download" e escolha a versão adequada para o seu sistema operacional (Windows, macOS ou Linux).
    
    -  **Instalação:**  
        - Execute o arquivo baixado e siga as instruções do assistente de instalação.
        - Durante a instalação, recomendo marcar as opções "Add 'Open with Code' action to Windows Explorer file context menu" e "Add 'Open with Code' action to Windows Explorer directory context menu" (para usuários Windows) para facilitar a abertura de arquivos e diretórios com o VS Code.
    
    -  **Configuração inicial:**  
        - Ao abrir o VS Code pela primeira vez, você será apresentado a uma interface com uma barra lateral à esquerda. Esta barra contém ícones para explorador de arquivos, pesquisa, controle de versão, extensões, entre outros.
        - Recomendo instalar a extensão "Python" para obter suporte à linguagem Python. Para isso, clique no ícone de extensões (quarto ícone da barra lateral) e pesquise por "Python". Selecione a extensão oficial oferecida pela Microsoft e clique em "Install".
        - Recomendo também instalar a extensão "Jupyter" para rodar notebooks diretamente pelo VSCode. Siga o mesmo processo de pesquisa e instalação que você fez para a extensão Python.

### Instalação do Jupyter Notebook

O Jupyter Notebook é uma aplicação web que permite criar e compartilhar documentos que contêm código, equações, visualizações e texto explicativo. É amplamente utilizado para análise de dados, ciência de dados e aprendizado de máquina.

!!! exercise

    -  **Instalação via pip:**  
        - Abra o terminal ou prompt de comando.
        - Digite o seguinte comando: `pip install jupyter`
    
    -  **Execução:**  
        - No terminal ou prompt de comando, digite `jupyter notebook`. Isso iniciará o servidor do Jupyter e abrirá uma nova janela ou aba no seu navegador padrão com a interface do Jupyter Notebook.
        - Você pode criar um novo notebook selecionando "New" e depois "Python 3" ou pode abrir notebooks existentes navegando pelos diretórios.

    -  **Integração com VS Code:**  
        - Com a extensão "Jupyter" instalada no VS Code, você pode criar e editar notebooks diretamente na IDE. Basta criar um novo arquivo com a extensão `.ipynb` ou abrir um existente.

Pronto! Se tudo deu certo até aqui, estamos com a nossa infraestrutura pronta para começar a desenvolver sistemas utilizando Python e Jupyter Notebook.
