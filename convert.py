def convert_structure(exercise_choice):
    # Dividir o texto original em linhas e remover linhas em branco
    lines = [line.strip() for line in exercise_choice.split("\n") if line.strip()]

    # Encontrar a linha que contém a pergunta
    question_line = ""
    for i, line in enumerate(lines):
        if line.startswith("!!! exercise choice"):
            # A pergunta está na linha seguinte
            question_line = lines[i + 1].strip()
            break

    # Iniciar o novo formato com a tag de abertura e a pergunta
    new_structure = "<?quiz?>\n\n"
    new_structure += f"question: {question_line}\n"

    # Extrair e reorganizar as respostas
    for line in lines:
        if line.startswith("- [x]"):
            # Resposta correta
            answer_correct = line.split("[x] ")[1].strip()
            new_structure += f"answer-correct: {answer_correct}\n"
        elif line.startswith("- [ ]"):
            # Respostas incorretas
            answer = line.split("[ ] ")[1].strip()
            new_structure += f"answer: {answer}\n"

    # Adicionar o conteúdo da resposta
    for i, line in enumerate(lines):
        if line.startswith("!!! answer"):
            answer_content = lines[i + 1].strip()
            new_structure += f"content:\n{answer_content}\n"
            break
    
    # Fechar a tag do quiz
    new_structure += "<?/quiz?>"

    return new_structure

# Testar o script com a estrutura original
original_structure = '''!!! exercise choice "Questão"
    Qual é a principal diferença entre as instruções `break` e `continue` em um laço `while`?

    - [x] `break` interrompe o laço, enquanto `continue` interrompe a iteração atual e retorna ao início do laço.
    - [ ] `break` e `continue` ambos interrompem o laço imediatamente.
    - [ ] `break` retorna ao início do laço, enquanto `continue` interrompe o laço.
    - [ ] Ambos têm o mesmo comportamento.
'''

# Gerar o novo formato
new_structure = convert_structure(original_structure)
print(new_structure)
