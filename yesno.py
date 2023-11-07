def inputs(questions):
    responses = []
    question_list = questions.split(',')  # Separando as perguntas

    for question in question_list:
        while True:
            answer = input(f"{question.strip()} (responda 'y' para sim, 'n' para não): ").lower()
            if answer in ['y', 'n']:
                responses.append(answer == 'y')  # Armazena True para 'y' e False para 'n'
                break
            else:
                print("Por favor, responda com 'y' para sim ou 'n' para não.")

    return responses

def main():
    questions = "Você gosta de Python?,Você já programou em Python antes?,Você está gostando deste programa?"

    # Chama a função inputs com as perguntas
    answers = inputs(questions)

    # Imprime as respostas no formato booleano
    print("Respostas:")
    for i, answer in enumerate(answers):
        print(f"Pergunta {i + 1}: {answer}")

print("\x1bc\x1b[43;30m")
main()

