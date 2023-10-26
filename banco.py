with open("testes.txt", "r") as arquivo:
  linhas = arquivo.readlines()
with open("tiposEmpresas.txt", "r") as arquivo2:
  naturezas = arquivo2.readlines()

linhas = [elemento.replace(",", ".") for elemento in linhas]
linhas = [elemento.replace(";", ",") for elemento in linhas]
linhas = [elemento.replace('"', "") for elemento in linhas]
naturezas = [elemento.replace('"', "") for elemento in naturezas]


lista_atualizada = []
dicionario = {}
for natureza in naturezas:
  parte = natureza.strip().split(";")
  chave = parte[0]
  valor = parte[1]
  dicionario[chave] = valor

for linha in linhas:
    partes = linha.split(',')

    for key, value in dicionario.items():
      if key == partes[2]:
        texto = value

    match partes[5]:
      case '00':
        texto2 = 'Não informado'
      case '01':
        texto2 = 'Micro empresa'
      case '03':
        texto2 = 'Empresa de pequeno porte'
      case '05':
        texto2 = 'Demais'

    partes.insert(3, texto)
    partes.insert(7, texto2)
    nova_linha = ','.join(partes)
    lista_atualizada.append(nova_linha)

for linha in lista_atualizada:

    print(linha)

lista_de_listas = []
for linha in lista_atualizada:

    lista_de_strings = linha.strip().split(',')
    lista_de_listas.append(lista_de_strings)



import sqlite3 as conector
try:
  conexao = conector.connect("meu_banco.db")

  cursor = conexao.cursor()

#  cursor.execute('''
#    CREATE TABLE pessoas(
#      cnpj INTEGER PRIMARY KEY UNIQUE,
#      nome TEXT,
#      natureza INTEGER,
#      descricao TEXT,
#      qualificacao INTEGER,
#      capital INTEGER,
#      codigo_porte INTEGER,
#      porte TEXT,
#      ente INTEGER
#
#    )

#''')

#  cursor.execute("INSERT INTO pessoas (cnpj, nome, natureza, descricao, qualificacao, capital, codigo_porte, porte, ente) VALUES (?,?,?,?,?,?,?,?,?)", lista_atualizada)
#  cursor.execute("INSERT INTO pessoas (cnpj, nome, natureza, descricao, qualificacao, capital, codigo_porte, porte, ente) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", lista_de_listas)

  for i in lista_de_listas:
    cursor.execute("INSERT INTO pessoas (cnpj, nome, natureza, descricao, qualificacao, capital, codigo_porte, porte, ente) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", i)
  conexao.commit()

except IndexError as erro:
  print("Informações ja contidas no banco")

finally:
  cursor.close()
  conexao.close()


