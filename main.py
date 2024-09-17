import tkinter as tk
from tkinter import messagebox
from database import conectar, inserir_dados


def submit_entrada():
    nome = entry_nome.get()
    email = entry_email.get()

    if not nome or not email:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    conn = conectar()
    
    if conn:
        inserir_dados(conn, nome, email)
        conn.close()

    btn_entrada.pack_forget()
    btn_saida.pack()

def submit_saida():
    nome = entry_nome.get()
    email = entry_email.get()

    conn = conectar()
    if conn:
        inserir_dados(conn, nome, email, 'saida')
        conn.close()

    reset_interface()

def reset_interface():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    
    btn_saida.pack_forget()
    btn_entrada.pack()

root = tk.Tk()
root.title("Registro de Ponto")

tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

btn_entrada = tk.Button(root, text="Entrada", command=submit_entrada)
btn_entrada.pack()

btn_saida = tk.Button(root, text="Saída", command=submit_saida)

root.mainloop()
