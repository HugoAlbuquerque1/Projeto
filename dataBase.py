
import sqlite3


class Database:
    
    def iniciar(self):
        self.connection = sqlite3.connect("users.db")
        self.cursor = self.connection.cursor()
        print("DataBase Iniciado com sucesso ")

        self.create_table()
    

    def create_table(self):
        criar_tabela = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user TEXT,
            senha TEXT
        )
        """
        # Verifique se a tabela já existe no banco de dados
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        tabela_existe = self.cursor.fetchone()

        if tabela_existe:
            print("Tabela já existe no banco de dados")
        else:
            self.cursor.execute(criar_tabela)
            print("Tabela Criada com Sucesso")
            self.connection.commit()



    def fazer_Login(self, username):
        self.cursor.execute("SELECT user, senha FROM users WHERE user = ? ", (username, ))
        result = self.cursor.fetchone()
        if result:
            print("Acesso à tabela bem-sucedido")
        return result
        



    def inserir_usuario(self, new_User, senhaCrip ):
        self.cursor.execute("INSERT INTO users (user, senha) VALUES (?, ?)", (new_User, senhaCrip))
        self.connection.commit()

   
    def Desconect(self):
        print("Desconectando ao banco de dados")
        self.connection.close()