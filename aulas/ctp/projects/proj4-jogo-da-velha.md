# Projeto 4: Jogo da Velha

## Introdução

Desenvolva uma versão simples do jogo da velha, onde dois jogadores podem jogar um contra o outro.

## Siga as instruções das funções a serem Implementadas

### `inicializar_tabuleiro()`

- **Descrição:** Inicializa o tabuleiro de jogo.
- **Entrada:** Nenhuma.
- **Saída:** Tabuleiro inicializado.
- **Dicas:** 

  - Considere usar uma lista de listas para representar o tabuleiro.
  - Considere a criação de uma função separada para limpar o console, mantendo a interface do usuário limpa.

### `exibir_tabuleiro`

- **Descrição:** Exibe o estado atual do tabuleiro.
- **Entrada:** Tabuleiro.
- **Saída:** Nenhuma (apenas exibe o tabuleiro).
- **Dicas:** 

  - Formate a saída para fácil leitura.
  - Adicione coordenadas ao tabuleiro para ajudar os jogadores a identificar facilmente onde fazer sua jogada.

### `fazer_jogada`

- **Descrição:** Realiza a jogada de um jogador.
- **Entrada:** Tabuleiro, jogador ('X' ou 'O') e posição da jogada.
- **Saída:** Tabuleiro atualizado.
- **Dicas:** 

  - Valide a jogada para garantir que a posição está livre.
  - Implemente uma checagem para garantir que a posição escolhida está dentro dos limites do tabuleiro.

### `verificar_vencedor`

- **Descrição:** Verifica se há um vencedor.
- **Entrada:** Tabuleiro.
- **Saída:** Vencedor ('X', 'O' ou 'Empate') ou `None` se o jogo ainda não terminou.
- **Dicas:** 

  - Implemente a lógica para verificar linhas, colunas e diagonais.
  - Forneça uma mensagem clara indicando qual jogador venceu ou se o jogo terminou em empate.

### `jogar_novamente`

- **Descrição:** Pergunta aos jogadores se eles querem jogar novamente.
- **Entrada:** Nenhuma.
- **Saída:** Resposta dos jogadores (sim ou não).
- **Dicas:** 

  - Valide a entrada dos jogadores.
  - Considere adicionar uma contagem de vitórias para cada jogador, incentivando a competição amigável.

## **Função Principal e Modularização**

- Crie a função principal `main` que orquestrará a execução do seu código.
- É permitido criar quantas funções adicionais ou módulos conforme achar necessário para manter cada parte do código focada em uma tarefa específica.