import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import shutil
import os

def selecionar_origem():
    pasta=filedialog.askdirectory(title="Selecione a pasta de entrada")
    if pasta:
        entrada_origem.set(pasta)

def selecionar_saida():
    pasta=filedialog.askdirectory(title="Selecione a pasta de saida")
    if pasta:
        entrada_saida.set(pasta)

def copiar_arquivos():
    origem=entrada_origem.get()
    saida=entrada_saida.get()
    extensao=entrada_tipo.get().strip().lower()

    if not origem or not saida or not extensao:
        messagebox.showwarning("Algo errado","Preencha todos os campos")
        return
    
    if not extensao.startswith("."):
        extensao="." + extensao

    arquivos=[f for f in os.listdir(origem) if f.endswith(extensao)]

    if not arquivos:
        messagebox.showinfo("Resultado", f"Nenhum arquivo '{extensao}' encontrado")
        return
    
    os.makedirs(saida, exist_ok=True)
    copiados=0

    for arquivo in arquivos:
        shutil.copy(os.path.join(origem, arquivo), os.path.join(saida, arquivo))
        listbox.insert(tk.END, f"certo {arquivo}")
        copiados += 1

    messagebox.showinfo("Concluido", f"{copiados} arquivo(s) copiado(s) com sucesso")

janela=tk.Tk()
janela.title("Copiador de arquivos")
janela.geometry("800x600")
janela.resizable(False, False)

entrada_origem=tk.StringVar()
entrada_saida=tk.StringVar()

tk.Label(janela, text="Pasta de entrada:").pack(anchor="w", padx=20, pady=(20, 0))
frame1=tk.Frame(janela)
frame1.pack(fill="x", padx=20)
tk.Entry(frame1, textvariable=entrada_origem, width=45).pack(side="left")
tk.Button(frame1, text="Selecionar", command=selecionar_origem).pack(side="left", padx=5)

tk.Label(janela, text="Tipo de arquivo").pack(anchor="w", padx=20, pady=(15, 0))
entrada_tipo=tk.Entry(janela, width=20)
entrada_tipo.pack(anchor="w", padx=20)

tk.Label(janela, text="Pasta de saida:").pack(anchor="w", padx=20, pady=(15, 0))
frame2=tk.Frame(janela)
frame2.pack(fill="x", padx=20)
tk.Entry(frame2, textvariable=entrada_saida, width=45).pack(side="left")
tk.Button(frame2, text="Selecionar", command=selecionar_saida).pack(side="left", padx=5)

tk.Button(janela, text="Copiar arquivos", command=copiar_arquivos,
            bg="#838b8b", fg="white", font=("Arial", 12, "bold"), pady=5).pack(pady=20)

tk.Label(janela, text="Arquivos copiados").pack(anchor="w", padx=20)
listbox=tk.Listbox(janela, height=8, width=60)
listbox.pack(padx=20)

janela.mainloop()