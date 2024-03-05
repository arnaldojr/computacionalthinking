
"Mas afinal, de que serve ter uma coleção de itens se não conseguimos encontrar o que precisamos quando precisamos? Assim como o problema da busca, a 'ordenação' é uma questão fundamental que enfrentamos constantemente, seja organizando livros em uma estante, as cartas em um jogo de baralho, arquivos em um computador ou até mesmo as fotos no nosso celular."

## A Importância da Ordenação

Ordenar dados é uma operação fundamental em Ciência da Computação, nada mais é do que arrumar a casa, com implicações significativas em diversas áreas de aplicação. Vamos explorar em mais detalhes por que a ordenação é tão importante:

- Facilitar a busca e o acesso a informações.

    Quando os dados estão ordenados, a busca por informações específicas se torna muito mais rápida e eficiente. Por exemplo, se você tem uma lista telefônica ordenada alfabeticamente, encontrar o número de uma pessoa específica é muito mais fácil do que se os nomes estivessem em ordem aleatória. Da mesma forma, em um banco de dados, registros ordenados permitem consultas mais rápidas e precisas.

- Melhorar a eficiência de algoritmos

    Muitos algoritmos de busca, como a busca binária, exigem que os dados estejam ordenados para funcionar corretamente. A busca binária, por exemplo, pode localizar um elemento em uma lista ordenada em tempo logarítmico (O(log n)), enquanto a busca sequencial em uma lista não ordenada requer tempo linear (O(n)). Portanto, ordenar os dados pode ser um passo crucial para garantir a eficiência de algoritmos subsequentes.


- Organizar e apresentar dados de maneira compreensível

    Além dos benefícios técnicos, a ordenação ajuda a apresentar dados de maneira mais compreensível e acessível. Em relatórios, tabelas ou gráficos, dados ordenados facilitam a identificação de padrões, tendências e anomalias. Isso é essencial não apenas para análise de dados, mas também para a tomada de decisões baseada em informações claras e organizadas.

- Otimização de Recursos

    A ordenação eficiente também pode contribuir para a otimização de recursos computacionais, como memória e processamento. Algoritmos de ordenação otimizados minimizam o número de operações necessárias, reduzindo o consumo de recursos e melhorando o desempenho geral do sistema.

- Aplicações em Diversos Campos
    
    A ordenação tem aplicações em diversos campos, desde sistemas de gerenciamento de banco de dados, engenharia de software e inteligência artificial até áreas como bioinformática, onde a ordenação de sequências genéticas é fundamental para análises comparativas e descobertas científicas.



Em Python ou JavaScript tem um método de classificação nativo. Ele funciona em arrays de números ou até mesmo em arrays de strings:

Em Python:

```python 
animals = ["gnu", "zebra", "antelope", "aardvark", "yak", "iguana"]
animals.sort()
print(animals)
```
ou em JavaScript:

```javascript
var animals = ["gnu", "zebra", "antelope", "aardvark", "yak", "iguana"];
animals.sort();
print(animals);
```

Mesmo que o JavaScript tenha um método de classificação nativo, classificar é um ótimo exemplo de como pode haver muitas maneiras de pensar um mesmo problema, algumas talvez melhores que outras. Compreender a classificação é um tradicional primeiro passo para o domínio de algoritmos.


Existem  diversos  tipos  de  algoritmos  para  a  tarefa  de  ordenação.  Suas complexidades  vãode  O(nlogn)  até  O(n2). Assista o video com 15 formas de ordenação diferentes.


![https://youtu.be/kPRA0W1kECg?si=QGFoBM55yaHOB9HL](https://youtu.be/kPRA0W1kECg?si=QGFoBM55yaHOB9HL)



!!! exercise choice "Questão 1"
    Qual é a alternativa que descreve o conceito de ordenação na computação?


    - [ ] Os resultados, assim, poderão ser consolidados e analisados pelas instâncias de planejamento estratégico das instituições que implementam as tais políticas públicas.

    - [x] É a operação de rearranjar os dados disponíveis em uma determinada ordem.

    - [ ] Todas as empresas têm a necessidade de classificar seus dados, muitas vezes em volumes maciços.

    - [ ] A eficiência no manuseio desses dados pode ser aumentada.

    - [ ] Em diversas situações cotidianas é conveniente colocar uma lista em ordem para facilitar a busca de informações nela contidas.

    !!! answer
        Ordenar é rearranjar os dados em uma ordem determinada


!!! exercise
    Discuta com o seu colega uma forma de ordenar cartas de baralho que estão em sua mão. Por exemplo [5,13,47,17,53,2,7,29,41,11,23] A dupla deve escrever a forma que pensou em um pseudocódigo. Agora Compare com os outros grupo se realizaram essa tarefa da mesma forma ou não. Quantos passos foram necessários? Qual a forma mais eficiênte de realizar essa tarefa?


### Que tal pensar nesse problema de forma visual?

Você pode trocar qualquer par de cartas ao clicar em uma carta e depois na outra. Troque as cartas até que elas estejam ordenadas com a menor carta à esquerda.

<iframe sandbox="allow-popups allow-same-origin allow-scripts allow-top-navigation" src="https://pt.khanacademy.org/computer-programming/program/4869717459730432/embedded?embed=yes&amp;author=no&amp;editor=no&amp;width=688&amp;buttons=no&amp;settings=%7B%7D" class="perseus-scratchpad" allowfullscreen="" style="height: 200px; width: 100%;"></iframe>




!!! progress
    continuar...

"Depois de explorarmos o problema da ordenação, vamos agora pensar em um contexto mais computacional.

!!! exercise
    Definição do Problema

    Dada uma coleção de elementos, com uma relação de ordem entre eles, ordenar os elementos da coleção de forma crescente.

    !!! answer
        Para entender melhor, imagine uma lista de números, onde cada número é único, e queremos que essa liste fique em ordem crescente, ou seja, do menor para o maior.




