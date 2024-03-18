## CHECKPOINT4

### Objetivo

A proposta é focada no `estudo prático de algoritmos de busca e ordenação aplicados a cenários reais`. Para isso, vocês deverão desenvolver uma biblioteca customizada em Python que incorpore as técnicas de `ordenação` e `busca` estudadas, além de seguir as boas práticas de `programação orientada a objetos` (POO).

### Desenvolvimento da infraestrutura:

- Desenvolvimento da Biblioteca:

    - Crie um `pacote` chamado `algoritmos`, que servirá como a biblioteca customizada.
    Dentro do pacote, crie módulos separados para as técnicas de ordenação e busca.
        
        - Crie um módulo `ordenacao.py` que contenha uma `classe Ordenacao` com métodos estáticos para os algoritmos de `ordenação` estudados.

        - Crie um módulo `busca.py` que contenha uma `classe Busca` com métodos estáticos para os algoritmos de `busca` estudados.

    - Crie um `pacote` chamado `testes`, que conterá testes para validar que sua biblioteca está funcionando corretamente. Os testes devem cobrir diferentes tamanhos de entrada e condições (ordenadas e desordenadas).

        - Dentro do pacote testes, crie os `módulos` `test_ordenacao.py` e `test_busca.py` para testar os métodos de ordenação e busca, respectivamente.

    - Vocês devem utilizar a biblioteca customizada como um `módulo` em sua aplicação principal `main.py`.

    - A estrutura de pastas e arquivos para a biblioteca customizada pode ser organizada da seguinte forma:

    ```bash
    projeto/
    │
    ├── algoritmos/
    │   ├── __init__.py
    │   ├── ordenacao.py
    │   └── busca.py
    │
    ├── testes/
    │   ├── __init__.py
    │   ├── test_ordenacao.py
    │   └── test_busca.py
    │
    └── main.py
    ```

### Implementações:

- Para o pacore `algoritmos`, implemente todos os algoritmos de ordenação e de busca estudados em aula.

- Para o pacote `testes` considere realizar os seguinte testes:

    - Testes de Ordenação:

        1. vetor ordenado crescente: [3, 7, 33, 59, 71]
        1. vetor não ordenado: [71, 7, 3, 9, 7]
        1. vetor ordenado descrescente: [71, 59, 33, 7, 3]
        1. Vetor vazio: []
        1. Vetor com um único elemento: [42]
        1. Vetor com elementos repetidos: [3, 7, 3, 9, 7]
        1. Vetor com elementos negativos: [-5, -3, -9, -1]

    - Testes de Busca:

        1. Busca por um elemento que está presente no vetor.
        1. Busca por um elemento que não está presente no vetor.
        1. Busca em um vetor vazio.
        1. Busca em um vetor com um único elemento.

- Para o programa principal `main.py` realize `Análise de Desempenho` e `Relatórios de Teste`:

    - Vamos realizar uma análise impirica para determinar a performance dos algoritmos, essa análise computa o tempo de execução de cada algortimo para executar. Por exemplo:

    ```python
    def medir_tempo_execucao(algoritmo, lista):
    inicio = time.time() ### define o tempo inicial
    algoritmo(lista)     ### algoritmo sendo executado
    fim = time.time()    ### tempo final
    return fim - inicio  ### calcula o tempo total de execução   
    ```
    
    - Para realizar a `análise de desempenho`, vocês podem seguir os seguintes passos:

        1. `Importar Módulos Necessários`: Importe os módulos de ordenação e busca da sua biblioteca e modulos adicionais como `import time`, `import random` e `import matplotlib.pyplot as plt`.
        1. `Gerar Dados de Teste`: - Crie listas de diferentes tamanhos para testar os algoritmos de ordenação e busca. Teste `ao menos` listas com `100`, `1.000` e `10.000` elementos, etc.
        1. `Medir Tempo de Execução`: Para cada lista de teste, meça o tempo de execução de cada algoritmo de ordenação e busca. Crie uma função que realize esse teste automaticamente. Use a função `time.time()` para obter o tempo antes e depois da execução do algoritmo e calcule a diferença de tempo.

    - Para realizar o `relatório`, vocês podem seguir os seguintes passos:

        1. `Armazenar Resultados`: Armazene os resultados dos tempos de execução em um dicionário, onde as chaves são os nomes dos algoritmos e os valores são listas dos tempos de execução correspondentes a cada tamanho de lista de teste.
        1. `Gerar Gráfico`: Use o `matplotlib.pyplot` para gerar um gráfico que compare o tempo de execução dos algoritmos em função do tamanho da lista de teste.
        1. `Salvar o Gráfico`: Salve o gráfico como uma imagem (plt.savefig("relatorio_grafico.png")).
        1. `Identificar o Algoritmo Campeão`: Analise o gráfico para determinar qual algoritmo teve o melhor desempenho em termos de tempo de execução para os diferentes tamanhos de lista.


## Datas e Formatos:

A solução será apresentada em aula remota, e cada grupo terá até `8 min` para demonstrar o funcionamento do projeto, explicar o código e responder a quaisquer perguntas. É importante estar bem preparado para esta apresentação, assegurando que todos os membros do grupo conheçam bem o projeto e estejam aptos a participar da discussão.

| Data | CheckPoint |
|:---:|:---:|
| 26/03 | CheckPoint 4 - Apresentação do CP4. |



## Critérios de Avaliação

- `Implementação dos Algoritmos (20%)`: Criação correta do pacote Algoritmos com as implementações dos algoritmos de ordenação e busca estudados (10%). Estrutura e Organização do Código (10%).

- `Implementaçao dos Testes (30%)`: Criação correta do pacote testes incluindo herança e diferentes casos e condições (10%). Casos de testes implementados corretamente (20%).

- `Análise de Desempenho (30%)`: Implementação correta dos testes de desempenho para diferentes tamanhos de listas.

- `Relatórios de Teste (20%)`: Análise completa dos resultados, incluindo a apresentação de gráficos e a identificação do algoritmo campeão (20%).

- `Documentação e apresentação (Bônus até 10%)`: Documentação do código completa e organizada no repositório, incluindo docstrings e comentários explicativos. Apresentação coerente, de forma técnica.

## **Contato e Suporte**

Não existem perguntas ruins, caso tenham dúvidas sobre o projeto, não hesitem em perguntar tanto em aula como fora de aula. O objetivo é que que vocês tenham uma experiência de aprendizado positiva, produtiva e divertida!

## **Checklist de Submissão**

O projeto deve ser submetido em um repositório github que o grupo irá criar. Aguns pontos relevantes para garantir que todos os requisitos foram atendidos:

- [ ] **Código Fonte**: Todo o código fonte está bem comentado e formatado de acordo com as boas práticas de programação?
- [ ] **Funcionalidades**: Todas as funcionalidades requisitadas foram implementadas e estão funcionando corretamente?
- [ ] **Estruturas de Dados**: As estruturas de dados escolhidas são adequadas para as tarefas propostas?
- [ ] **Testes**: O código foi testado e é funcional?
- [ ] **Apresentação**: O grupo está preparado para a apresentação, com todos os membros conhecendo bem o projeto e aptos a responder perguntas?
- [ ] **Documentação**: A documentação do projeto está completa?