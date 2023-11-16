## Jogo "Adivinhe o Número"

## Introdução

Neste projeto, você será desafiado a criar um simples jogo de adivinhação chamado "Adivinhe o Número". O objetivo do jogo é que o jogador adivinhe um número secreto gerado aleatoriamente pelo programa. O jogo oferece feedback ao usuário após cada palpite, informando se o número secreto é maior ou menor do que o palpite fornecido.

## Descrição do Jogo

1. O jogador escolhe um intervalo: [0, 100) ou [0, 1000) sendo 1 ou 2.
2. Com base no intervalo escolhido, o programa determina o número de palpites que o jogador tem.
3. O programa gera um número secreto aleatório dentro do intervalo escolhido.
4. O jogador tenta adivinhar o número. Após cada palpite, o programa informa ao jogador se o número secreto é maior, menor ou igual ao palpite fornecido.
5. O jogo termina quando o jogador adivinha corretamente ou esgota todos os seus palpites.

## Funções a serem Implementadas

### 1. `escolher_intervalo()`

- **Descrição:** Permite que o usuário escolha um intervalo para o número a ser adivinhado.
- **Entrada:** Nenhuma.
- **Saída:** O intervalo numérico escolhido (100 ou 1000).

### 2. `definir_palpites(intervalo_num)`

- **Descrição:** Define o número de palpites com base no intervalo escolhido.
- **Entrada:** Intervalo numérico (100 ou 1000).
- **Saída:** Número de palpites permitidos.

### 3. `gerar_numero_secreto(intervalo_num)`

- **Descrição:** Gera um número aleatório dentro do intervalo escolhido.
- **Entrada:** Intervalo numérico (100 ou 1000).
- **Saída:** Número aleatório gerado.

### 4. `obter_palpite()`

- **Descrição:** Permite que o usuário insira um palpite.
- **Entrada:** Nenhuma.
- **Saída:** Palpite numérico inserido pelo usuário.

### 5. `avaliar_palpite(palpite, numero_secreto)`

- **Descrição:** Avalia o palpite do usuário em relação ao número secreto.
- **Entrada:** Palpite do usuário e número secreto.
- **Saída:** Uma das três strings: "Maior", "Menor" ou "Correto".

## Dicas e Sugestões

1. **Modularização:** Mantenha seu código organizado, separando diferentes lógicas em funções distintas.
2. **Tratamento de Erros:** Certifique-se de tratar possíveis erros de entrada, como quando o usuário insere texto em vez de um número.
3. **Feedback:** Forneça feedback claro e útil ao usuário após cada ação.
4. **Teste:** Depois de implementar cada função, teste-a individualmente para garantir que ela funcione como esperado.
