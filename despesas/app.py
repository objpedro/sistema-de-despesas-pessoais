import tkinter as tk
import sqlite3
from tkinter import messagebox

class SistemaDespesas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Administração de Despesas Pessoais")
        self.conn = sqlite3.connect("despesas.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS despesas 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            nome TEXT, 
                            data TEXT, 
                            valor REAL, 
                            metodo_pagamento TEXT, 
                            descricao TEXT, 
                            status TEXT)''')
        self.conn.commit()

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_data = tk.Label(root, text="Data da Despesa:")
        self.label_data.pack()
        self.entry_data = tk.Entry(root)
        self.entry_data.pack()

        self.label_valor = tk.Label(root, text="Valor:")
        self.label_valor.pack()
        self.entry_valor = tk.Entry(root)
        self.entry_valor.pack()

        self.label_metodo_pagamento = tk.Label(root, text="Método de Pagamento:")
        self.label_metodo_pagamento.pack()
        self.entry_metodo_pagamento = tk.Entry(root)
        self.entry_metodo_pagamento.pack()

        self.label_descricao = tk.Label(root, text="Descrição:")
        self.label_descricao.pack()
        self.entry_descricao = tk.Entry(root)
        self.entry_descricao.pack()

        self.label_status = tk.Label(root, text="Status da Despesa:")
        self.label_status.pack()
        self.entry_status = tk.Entry(root)
        self.entry_status.pack()

        self.button_adicionar = tk.Button(root, text="Adicionar Despesa", command=self.adicionar_despesa)
        self.button_adicionar.pack()

        self.button_atualizar = tk.Button(root, text="Atualizar Despesa", command=self.atualizar_despesa)
        self.button_atualizar.pack()

        self.button_deletar = tk.Button(root, text="Deletar Despesa", command=self.deletar_despesa)
        self.button_deletar.pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack()
        self.carregar_despesas()

    def adicionar_despesa(self):
        nome = self.entry_nome.get()
        data = self.entry_data.get()
        valor = self.entry_valor.get()
        metodo_pagamento = self.entry_metodo_pagamento.get()
        descricao = self.entry_descricao.get()
        status = self.entry_status.get()

        if nome and data and valor and metodo_pagamento and descricao and status:
            self.c.execute("INSERT INTO despesas (nome, data, valor, metodo_pagamento, descricao, status) VALUES (?, ?, ?, ?, ?, ?)",
                           (nome, data, valor, metodo_pagamento, descricao, status))
            self.conn.commit()
            self.carregar_despesas()
            self.limpar_campos()
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    def atualizar_despesa(self):
        selected_item = self.listbox.curselection()
        if selected_item:
            id = self.listbox.get(selected_item)[0]
            nome = self.entry_nome.get()
            data = self.entry_data.get()
            valor = self.entry_valor.get()
            metodo_pagamento = self.entry_metodo_pagamento.get()
            descricao = self.entry_descricao.get()
            status = self.entry_status.get()

            if nome and data and valor and metodo_pagamento and descricao and status:
                self.c.execute("UPDATE despesas SET nome=?, data=?, valor=?, metodo_pagamento=?, descricao=?, status=? WHERE id=?",
                               (nome, data, valor, metodo_pagamento, descricao, status, id))
                self.conn.commit()
                self.carregar_despesas()
                self.limpar_campos()
            else:
                messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        else:
            messagebox.showwarning("Aviso", "Por favor, selecione uma despesa para atualizar.")

    def deletar_despesa(self):
        selected_item = self.listbox.curselection()
        if selected_item:
            id = self.listbox.get(selected_item)[0]
            self.c.execute("DELETE FROM despesas WHERE id=?", (id,))
            self.conn.commit()
            self.carregar_despesas()
            self.limpar_campos()
        else:
            messagebox.showwarning("Aviso", "Por favor, selecione uma despesa para deletar.")

    def carregar_despesas(self):
        self.listbox.delete(0, tk.END)
        self.c.execute("SELECT * FROM despesas")
        despesas = self.c.fetchall()
        for despesa in despesas:
            self.listbox.insert(tk.END, despesa)

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_data.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_metodo_pagamento.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.entry_status.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaDespesas(root)
    root.mainloop()