def forms(perguntas):
    respostas = []
    lista_perguntas = perguntas.split(',')  # Separando as perguntas

    for pergunta in lista_perguntas:
        resposta = input(f"{pergunta.strip()}? ")  # Pergunta ao usuário
        respostas.append(resposta)  # Armazena a resposta na lista

    return respostas

def main():
    lista_de_perguntas = "Qual é o seu nome,Qual é a sua idade,Qual é a sua profissão"

    # Chama a função forms com a lista de perguntas
    respostas = forms(lista_de_perguntas)

    # Imprime as respostas
    print("Respostas:")
    for i, resposta in enumerate(respostas):
        print(f"Pergunta {i + 1}: {resposta}")

print("\x1bc\x1b[43;30m")

main()

