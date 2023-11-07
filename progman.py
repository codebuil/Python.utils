import tkinter as tk
import subprocess

class Aplicativo:
    def __init__(self, root):
        self.root = root
        self.root.title("Executar Comandos do Windows")

        # String com os itens separados por ;
        string_itens = "Bloco de Notas,notepad;Paint,mspaint;Write,write;Prompt de Comando,cmd"

        # Separar os itens e criar a lista
        self.itens = []
        for item in string_itens.split(";"):
            item_info = item.split(",")
            self.itens.append((item_info[0], item_info[1]))

        # Lista de itens na janela
        self.lista = tk.Listbox(root)
        for item in self.itens:
            self.lista.insert(tk.END, item[0])
        self.lista.pack()

        # Botão para executar o comando correspondente ao item selecionado
        self.botao = tk.Button(root, text="Executar Comando", command=self.executar_comando)
        self.botao.pack()

    def executar_comando(self):
        # Obter o item selecionado na lista
        selecionado = self.lista.curselection()
        if selecionado:
            item_selecionado = self.itens[selecionado[0]]
            comando = item_selecionado[1]

            # Executar o comando no shell do Windows
            subprocess.Popen(comando, shell=True)

def main():
    root = tk.Tk()
    app = Aplicativo(root)
    root.configure(bg="brown", width=800, height=600)  # Define a cor de 
    root.mainloop()

main()

