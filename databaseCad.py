import sqlite3

class Database_cad:
    def iniciar(self):
        self.connection = sqlite3.connect("cadastro.db")
        self.cursor = self.connection.cursor()
        print("Banco de dados 'cadastro' iniciado")
        self.create_Cadastro_Table()

    def create_Cadastro_Table(self):
        Tab_cadastro = """
            CREATE TABLE IF NOT EXISTS aluno (
                matricula INTEGER PRIMARY KEY,
                nome TEXT,
                code TEXT,
                id_responsavel INTEGER,
                turno TEXT,
                curso TEXT,
                turma TEXT,
                datanasc DATE,
                FOREIGN KEY (id_responsavel) REFERENCES responsavel(id)
            );

            CREATE TABLE IF NOT EXISTS responsavel (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT,
                telefone INT
            );

            CREATE TABLE IF NOT EXISTS funcionario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nomefunc TEXT,
                matriculaFunc INT, 
                cpf INT,
                telefoneFunc INT,
                codef TEXT
            );

            CREATE TABLE IF NOT EXISTS visitas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                CPF INT,
                contato INT
            );
        """
        self.cursor.executescript(Tab_cadastro)
        print("Tabela Criada Com sucesso")
        self.connection.commit()

    def Desconect(self):
        print("Desconectando ao banco de dados")
        self.connection.close()
