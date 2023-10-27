# Projeto 1: Sistema de Reservas para Eventos

## Introdução

Um programa para gerenciar reservas de ingressos para diversos eventos. O sistema permitirá aos usuários adicionar eventos, comprar ingressos, cancelar reservas, visualizar eventos disponíveis e obter informações detalhadas sobre os eventos.

## Descrição do Sistema

O sistema deve ser capaz de gerenciar eventos e reservas, proporcionando uma interface intuitiva para os usuários realizarem suas operações. Abaixo estão as funcionalidades principais e as funções que devem ser implementadas para atingir os objetivos do sistema.

## Siga as instruções das funções a serem Implementadas

### `criar_evento`

- **Descrição:** Permite ao usuário criar um novo evento, fornecendo informações como nome, data, capacidade e localização.
- **Entrada:** Dados do evento.
- **Saída:** Evento criado e armazenado no sistema.
- **Dicas:**

  - Forneça feedback claro ao usuário após a criação do evento, confirmando os detalhes do evento.
  - Valide as entradas para garantir que todas as informações necessárias sejam fornecidas e estejam no formato correto.

### `listar_eventos`

- **Descrição:** Exibe uma lista de todos os eventos disponíveis, mostrando informações básicas de cada um.
- **Entrada:** Nenhuma.
- **Saída:** Lista de eventos.
- **Dicas:**

  - Formate a saída para fácil leitura, mostrando claramente as informações de cada evento.
  - Considere a implementação de paginação caso a lista de eventos seja muito longa.

### `reservar_vaga`

- **Descrição:** Permite ao usuário reservar uma vaga em um evento específico.
- **Entrada:** ID ou nome do evento.
- **Saída:** Confirmação da reserva.
- **Dicas:**

  - Verifique se há vagas disponíveis antes de confirmar a reserva.
  - Atualize a quantidade de vagas disponíveis após a reserva.
  - Forneça feedback claro ao usuário, indicando se a reserva foi bem-sucedida ou não.

### `cancelar_reserva`

- **Descrição:** Permite ao usuário cancelar uma reserva previamente feita.
- **Entrada:** ID ou nome do evento.
- **Saída:** Confirmação do cancelamento.
- **Dicas:**

  - Verifique se o usuário tem uma reserva para o evento antes de tentar cancelar.
  - Atualize a quantidade de vagas disponíveis após o cancelamento.
  - Forneça uma mensagem de confirmação clara ao usuário.

### `visualizar_detalhes_evento`

- **Descrição:** Exibe todos os detalhes de um evento específico.
- **Entrada:** ID ou nome do evento.
- **Saída:** Detalhes do evento.
- **Dicas:**

  - Mostre todas as informações relevantes do evento, incluindo nome, data, localização, capacidade e vagas disponíveis.
  - Formate a saída para garantir que as informações sejam fáceis de ler.

### `salvar_dados`

- **Descrição:** Salva todos os dados do sistema (eventos, reservas, etc.) em um arquivo.
- **Entrada:** Nenhuma.
- **Saída:** Confirmação de que os dados foram salvos.
- **Dicas:**

  - Use manipulação de arquivos para persistir os dados entre as sessões do programa.
  - Considere o uso de formatos de arquivo como JSON ou CSV.

### `carregar_dados`

- **Descrição:** Carrega os dados do sistema a partir de um arquivo.
- **Entrada:** Nenhuma.
- **Saída:** Confirmação de que os dados foram carregados.
- **Dicas:**

  - Implemente tratamento de erros para lidar com situações em que o arquivo de dados não existe ou está corrompido.

## **Função Principal e Modularização**

- Crie a função principal `main` que orquestrará a execução do seu código.
- É permitido criar quantas funções adicionais ou módulos conforme achar necessário para manter cada parte do código focada em uma tarefa específica.