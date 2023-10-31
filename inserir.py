import tkinter as tk
import sqlite3
from tkinter import messagebox

# Função para criar a tabela no banco de dados
def create_table():
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            cnpj INTEGER PRIMARY KEY UNIQUE,
            nome TEXT,
            natureza INTEGER,
            descricao TEXT,
            qualificacao INTEGER,
            capital INTEGER,
            codigo_porte INTEGER,
            porte TEXT,
            ente INTEGER

        )

    ''')
    conn.commit()

# Função para criar um novo contato
def create_contact():
    nome = entry_nome.get()
    cnpj = entry_cnpj.get()
    natureza = entry_natureza.get()
    descricao = entry_descricao.get()
    qualificacao = entry_qualificacao.get()
    capital = entry_capital.get()
    codigo_porte = entry_codigo_porte.get()
    porte = entry_porte.get()
    ente = entry_ente.get()

    
    if nome and cnpj and natureza and descricao and qualificacao and capital and codigo_porte and porte and ente:
        cursor.execute("INSERT INTO pessoas (cnpj, nome, natureza, descricao, qualificacao, capital, codigo_porte, porte, ente) VALUES (?,?,?,?,?,?,?,?,?)", (cnpj, nome, natureza, descricao, qualificacao, capital, capital, codigo_porte, porte, ente))
        conn.commit()
        entry_cnpj.delete(0, tk.END)
        entry_nome.delete(0, tk.END)
        entry_natureza.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
        entry_qualificacao.delete(0, tk.END)
        entry_capital.delete(0, tk.END)
        entry_codigo_porte.delete(0, tk.END)
        entry_porte.delete(0, tk.END)
        entry_ente.delete(0, tk.END)
        read_contacts()
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

# Função para ler todos os contatos
def read_contacts():
    cursor.execute("SELECT * FROM pessoas")
    rows = cursor.fetchall()
    text.delete(1.0, tk.END)
    for row in rows:
        text.insert(tk.END, f"{row[0]}. {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[6]} -{row[7]}\n")

# Função para atualizar um contato
def update_contact():
    nome = entry_nome.get()
    cnpj = entry_cnpj.get()
    natureza = entry_natureza.get()
    descricao = entry_descricao.get()
    qualificacao = entry_qualificacao.get()
    capital = entry_capital.get()
    codigo_porte = entry_codigo_porte.get()
    porte = entry_porte.get()
    ente = entry_ente.get()
    if id and nome and cnpj and natureza and descricao and qualificacao and capital and codigo_porte and porte and ente:
        cursor.execute("UPDATE pessoas SET nome = ?, telefone = ? WHERE id = ?", (cnpj, nome, natureza, descricao, qualificacao, capital, capital, codigo_porte, porte, ente))
        conn.commit()
        entry_cnpj.delete(0, tk.END)
        entry_nome.delete(0, tk.END)
        entry_natureza.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
        entry_qualificacao.delete(0, tk.END)
        entry_capital.delete(0, tk.END)
        entry_codigo_porte.delete(0, tk.END)
        entry_porte.delete(0, tk.END)
        entry_ente.delete(0, tk.END)
        read_contacts()
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

# Função para excluir um contato
def delete_contact():
    cnpj = entry_cnpj.get()
    if id:
        cursor.execute("DELETE FROM pessoas WHERE id = ?", (cnpj,))
        conn.commit()
        entry_cnpj.delete(0, tk.END)
        read_contacts()
    else:
        messagebox.showwarning("Erro", "Por favor, insira o ID do contato a ser excluído.")

# Configuração inicial
root = tk.Tk()
root.title("CRUD com SQLite")

# Conexão com o banco de dados
conn = sqlite3.connect("meu_banco.db")
cursor = conn.cursor()

# Criação da tabela (se não existir)
create_table()

# Widgets
label_cnpj = tk.Label(root, text="CNPJ:")
label_nome = tk.Label(root, text="CNPJ:")
label_natureza = tk.Label(root, text="Natureza:")
label_descricao = tk.Label(root, text="Descrição:")
label_qualificacao = tk.Label(root, text="Qualificação:")
label_capital = tk.Label(root, text="Capital:")
label_codigo_porte = tk.Label(root, text="Código Porte:")
label_porte = tk.Label(root, text="Porte:")
label_ente = tk.Label(root, text="Ente:")
entry_cnpj = tk.Entry(root)
entry_nome = tk.Entry(root)
entry_natureza = tk.Entry(root)
entry_descricao = tk.Entry(root)
entry_qualificacao = tk.Entry(root)
entry_capital = tk.Entry(root)
entry_codigo_porte = tk.Entry(root)
entry_porte = tk.Entry(root)
entry_ente = tk.Entry(root)
entry_telefone = tk.Entry(root)
entry_id = tk.Entry(root)
text = tk.Text(root, height=10, width=120, pady=4)
create_button = tk.Button(root, text="Criar Contato", command=create_contact)
read_button = tk.Button(root, text="Listar Contatos", command=read_contacts)
update_button = tk.Button(root, text="Atualizar Contato", command=update_contact)
delete_button = tk.Button(root, text="Excluir Contato", command=delete_contact)

# Posicionamento dos widgets
label_cnpj.grid(row=0, column=0)
label_nome.grid(row=0, column=2)
label_natureza.grid(row=0, column=4)
label_descricao.grid(row=0, column=6)
label_qualificacao.grid(row=0, column=8)
label_capital.grid(row=0, column=10)
label_codigo_porte.grid(row=0, column=12)
label_porte.grid(row=0, column=14)
label_ente.grid(row=0, column=16)

entry_cnpj.grid(row=0, column=1)
entry_nome.grid(row=0, column=3)
entry_natureza.grid(row=0, column=5)
entry_descricao.grid(row=0, column=7)
entry_qualificacao.grid(row=0, column=9)
entry_capital.grid(row=0, column=11)
entry_codigo_porte.grid(row=0, column=13)
entry_porte.grid(row=0, column=15)
entry_ente.grid(row=0, column=17, padx=10)


text.grid(row=4, column=0, columnspan=20)
create_button.grid(row=1, column=0, pady=10)
read_button.grid(row=1, column=1)
update_button.grid(row=1, column=2)
delete_button.grid(row=1, column=3)

root.mainloop()

# Fechando a conexão com o banco de dados
conn.close()
