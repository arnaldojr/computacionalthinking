

Vamos brincar do jogo de adivinhação. Nesse jogo, o objetivo é descobrir qual número foi sorteado pelo computador dentro de um intervalo bem definido. O computador vai selecionar aleatoriamente um número inteiro de 1 a 15. Você vai tentar adivinhar o número até encontrar aquele que foi selecionado pelo computador, e o computador lhe dirá a cada vez se seu palpite foi muito alto ou muito baixo:

<iframe sandbox="allow-popups allow-same-origin allow-scripts allow-top-navigation" src="https://pt.khanacademy.org/computer-programming/program/4863148342902784/embedded?embed=yes&amp;author=no&amp;editor=no&amp;width=688&amp;buttons=no&amp;settings=%7B%7D" class="perseus-scratchpad" allowfullscreen="" style="height: 200px; width: 100%;"></iframe>


Agora, reflita sobre como você encontrou o número sorteado. Foi um chute aleatório ou você seguiu algum método? 

Chutar números aleatoriamente não é a melhor estratégia. Em vez disso, você pode ter usado uma abordagem mais sistemática. 

Podemos utilizar o algoritmo de busca sequencial, para isso basta passar em sequencia por todos os valores da lista, 1,2,3..... Neste caso v

Foi facil né, afinal, a lista é pequena. Vamos complicar um pouco aumentando a lista para 300 posições.


<iframe sandbox="allow-popups allow-same-origin allow-scripts allow-top-navigation" src="https://pt.khanacademy.org/computer-programming/program/6095780544249856/embedded?embed=yes&amp;author=no&amp;editor=no&amp;width=688&amp;buttons=no&amp;settings=%7B%7D" class="perseus-scratchpad" allowfullscreen="" style="height: 400px; width: 100%;"></iframe>

Utilizando uma busca linear vamos ter no pior caso que fazer 300 chutes até encontrar o valor correto. Neste caso uma forma eficiênte é escolher o numero no meio do intervalo de opções. 

Por exemplo, se o intervalo é de 1 a 300, você começa adivinhando o número 150 (que é o meio do intervalo). Se o computador disser que seu palpite é muito alto, você sabe que o número sorteado está entre 1 e 149. Se o computador disser que seu palpite é muito baixo, você sabe que o número sorteado está entre 151 e 300.

Agora, você repete esse processo, escolhendo sempre o número no meio do novo intervalo, até encontrar o número sorteado. Esse método é conhecido como busca binária, porque em cada etapa você divide o intervalo de possibilidades pela metade (ou seja, em duas partes).

A busca binária é muito mais eficiente do que adivinhar números aleatoriamente ou verificar cada número um por um (o que seria uma busca sequencial). Ela nos permite encontrar rapidamente o número sorteado, mesmo em intervalos muito grandes.


### Desafio

Implemente o algoritmo de busca binária.

<iframe src="https://trinket.io/embed/python/9d59fb109f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Referência: https://pt.khanacademy.org/computing/computer-science/algorithms/intro-to-algorithms/a/a-guessing-game 

