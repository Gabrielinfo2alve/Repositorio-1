import sqlite3

 
conn = sqlite3.connect('DBappAlunos2.db')
cursor = conn.cursor()





def criar_tabela():
    cursor.execute("""

   CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Senha TEXT NOT NULL,
    CPF TEXT NOT NULL
 


   );

  """)
    conn.commit()
def adicionar_cpf():
   try:
     cursor.execute("""
             ALTER TABLE Users ADD COLUMN CPF TEXT
        """)
     conn.commit()
   except sqlite3.OperationalError:
     print("A coluna CPF já existe na tabela.")
criar_tabela()        


print("Conectado ao Banco de Dados Corretamente")



