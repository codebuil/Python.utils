
def menu(string_itens):
  itens = string_itens.split(',')  # Separa a string nos itens

  for i, item in enumerate(itens):
      print(f"{i}: {item.strip()}")  # Imprime um número de 0 a 9 e o item

  escolha = input("Escolha um número de 0 a 9: ")
  escolha = int(escolha) if escolha.isdigit() else None  # Valida a entrada como um número

  if escolha is not None and 0 <= escolha <= 9:
      return itens[escolha]
  else:
      return "Escolha inválida"

def main():
  lista_itens = "Maçã, Banana, Laranja, Morango, Abacaxi, Melancia, Pêra, Uva, Mamão, Melão"

  escolha_usuario = menu(lista_itens)

  print(f"Você escolheu: {escolha_usuario}")

print("\x1bc\x1b[43;30m")

main()
