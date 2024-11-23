from cachorro import Cachorro
from gato import Gato
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

lista = []

def cadastrar_animal():
    nome = entry_nome.get()
    idade = entry_idade.get()
    descricao = entry_descricao.get()
    tipo = var_tipo.get()

    erro = 0

    if nome == "":
        messagebox.showinfo("Erro", "Nome não preenchido")
        erro = 1

    if idade == "":
        messagebox.showinfo("Erro", "Idade do animal não foi preenchida")
        erro = 1

    if descricao == "":
        if tipo == "Cachorro":
            messagebox.showinfo("Erro", "Porte do animal não foi preenchido")
        else:
            messagebox.showinfo("Erro", "Raça do animal não foi preenchida")
        erro = 1

    if erro == 0:
        if tipo == "Cachorro":
            animal = Cachorro(nome, idade, descricao)
        else:
            animal = Gato(nome, idade, descricao)

        salvar(animal)
        messagebox.showinfo("Cadastro", f"O cadastro do seu {tipo} foi concluído com sucesso")

def salvar(obj):
    lista.append(obj)
    atualizar_listbox()

def atualizar_listbox():
    listbox.delete(0, tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())

def atualizar_descricao(*args):
    tipo = var_tipo.get()
    if tipo == "Cachorro":
        label_descricao.config(text="Porte:")
    else:
        label_descricao.config(text="Raça:")

janela = tk.Tk()
janela.title("Cadastro de Animais")
janela.geometry("500x300")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)
for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1, text="Cadastro")
janelinha.add(tab2, text="Lista")

label_nome = tk.Label(tab1, text="Nome:", font=("", 13))
label_nome.grid(row=0, column=0, sticky="w", padx=10)

entry_nome = tk.Entry(tab1, font=("", 13))
entry_nome.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

label_idade = tk.Label(tab1, text="Idade:", font=("", 13))
label_idade.grid(row=1, column=0, sticky="w", padx=10)

entry_idade = tk.Entry(tab1, font=("", 13))
entry_idade.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

label_descricao = tk.Label(tab1, text="Porte:", font=("", 13))
label_descricao.grid(row=2, column=0, sticky="w", padx=10)

entry_descricao = tk.Entry(tab1, font=("", 13))
entry_descricao.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Tipo:", font=("", 13)).grid(row=3, column=0, sticky="w", padx=10)
var_tipo = tk.StringVar(value="Cachorro")

tk.Radiobutton(tab1, text="Cachorro", font=("", 13), variable=var_tipo, value="Cachorro").grid(row=3, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Gato", font=("", 13), variable=var_tipo, value="Gato").grid(row=4, column=1, sticky="w", padx=10)

var_tipo.trace("w", atualizar_descricao)

tk.Button(tab1, text="Cadastrar", font=("", 13), command=cadastrar_animal).grid(row=5, columnspan=2, pady=10)

listbox = tk.Listbox(tab2, font=("", 13))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

tk.Button(tab2, text="Atualizar", font=("", 13), command=atualizar_listbox).grid(row=1, column=0, pady=10)

janela.mainloop()
