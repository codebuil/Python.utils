class Text:
    def __init__(self):
        self.linhas_numero = []  # Armazena os índices das linhas
        self.linhas = []  # Armazena o conteúdo das linhas

    def insertline(self, linha):
        self.linhas_numero.append(len(self.linhas) + 1)
        self.linhas.append(linha)

    def referencit(self, linha, index):
        self.linhas_numero.insert(index, len(self.linhas) + 1)
        self.linhas.insert(index, linha)

    def report(self):
        for idx in self.linhas_numero:
            print(self.linhas[idx - 1])

def main():
    texto = Text()
    linhas = "x86;8086;80186;80286;80386;80486;arm6;arm7;arm8"
    linhas_separadas = linhas.split(';')

    for linha in linhas_separadas:
        texto.insertline(linha)

    

    texto.report()  # Imprime todas as linhas do texto

print("\x1bc\x1b[43;30m")
if __name__ == "__main__":
    main()

