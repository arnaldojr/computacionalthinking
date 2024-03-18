# Projeto 2: Gerenciador de Finanças Pessoais

## Introdução

Desenvolva um programa para ajudar os usuários a gerenciar suas finanças pessoais. Os usuários devem ser capazes de registrar receitas e despesas, visualizar um relatório de suas finanças e obter insights sobre seus hábitos de gastos.

## Siga as instruções das funções a serem Implementadas

### `adicionar_transacao`

- **Descrição:** Adiciona uma nova transação (receita ou despesa) ao sistema.
- **Entrada:** Tipo de transação (receita ou despesa), valor, descrição e data.
- **Saída:** Confirmação da transação adicionada.
- **Dicas:** 

  - Forneça feedback imediato ao usuário após a adição de uma transação, confirmando os detalhes da transação.
  - Certifique-se de validar o tipo de transação e o valor (não deve ser negativo).

### `remover_transacao`

- **Descrição:** Remove uma transação existente.
- **Entrada:** ID ou detalhes da transação.
- **Saída:** Confirmação da transação removida.
- **Dicas:** 

  - Implemente uma busca por transações para facilitar a remoção.
  - Forneça uma confirmação antes de remover uma transação, para evitar remoções acidentais.

### `visualizar_relatorio`

- **Descrição:** Exibe um relatório das transações, mostrando receitas, despesas e saldo total.
- **Entrada:** Nenhuma.
- **Saída:** Relatório financeiro.
- **Dicas:** 

  - Formate a saída para fácil leitura.
  - Considere oferecer opções para visualizar o relatório por período (mensal, anual, etc.).

### `obter_insights`

- **Descrição:** Fornece insights sobre os hábitos de gastos do usuário.
- **Entrada:** Nenhuma.
- **Saída:** Insights financeiros.
- **Dicas:** 

  - Analise as transações para identificar padrões ou sugestões de economia.
  - Utilize técnicas simples de análise de dados para fornecer insights úteis.

### `salvar_dados`

- **Descrição:** Salva todas as transações em um arquivo.
- **Entrada:** Nenhuma.
- **Saída:** Confirmação de que os dados foram salvos.
- **Dicas:** 

  - Use manipulação de arquivos para armazenar os dados.
  - Considere o uso de formatos de arquivo como JSON ou CSV para salvar os dados.

### `carregar_dados`

- **Descrição:** Carrega as transações salvas anteriormente.
- **Entrada:** Nenhuma.
- **Saída:** Confirmação de que os dados foram carregados.
- **Dicas:** 

  - Adicione tratamento de erros para lidar com situações onde o arquivo de dados está corrompido.

## **Função Principal e Modularização**

- Crie a função principal `main` que orquestrará a execução do seu código.
- É permitido criar quantas funções adicionais ou módulos conforme achar necessário para manter cada parte do código focada em uma tarefa específica.