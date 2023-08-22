from singleton import Singleton
import sqlite3

class Database(Singleton):
    def iniciar(self):
        self.connection = sqlite3.connect("users.db")
        self.cursor = self.connection.cursor()
        print("DataBase Iniciado com sucesso ")

        self.create_table()

    def create_table(self):
        criar_tabela=("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user TEXT,
            senha TEXT
        )
        """)
        self.cursor.execute(criar_tabela)
        print("Tabela Criada Com sucesso")
        self.connection.commit

    def inserir_usuario(self, new_User, new_Pass ):
        self.cursor.execute("INSERT INTO users (user, senha) VALUES (?, ?)", (new_User, new_Pass))
        self.connection.commit()
     
    def Desconect(self):
        print("Desconectando ao banco de dados")
        self.connection.close()
    