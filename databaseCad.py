
import sqlite3

class Database_cad:
    def iniciar(self):
        self.connection = sqlite3.connect("cadastro.db")
        self.cursor =self.connection.cursor()
        print("Banco de dados  'cadastro' inciado")
        self.create_Cadastro_Table()
    
    def create_Cadastro_Table(self):
        Tab_cadastro = ("""

            CREATE TABLE IF NOT EXISTS instituição(
                Nome TEXT,
                id_Aluno INTEGER,
                id_Visitas INTEGER,
                id_Funcionario INTEGER,
                FOREING KEY (id_Aluno) REFERECES aluno(matricula),
                FOREING KEY (id_Visitas)  REFERENCES visitas(id),
                FOREING KEY (id_Funcionario)  REFERENCES funcionario(id)
                                          
                )
                        
            CREATE TABLE IF NOT EXISTS aluno(
                matricula INTEGER PRIMARY KEY,
                nome TEXT,
                code TEXT,
                id_responsavel INTEGER,
                turno TEXT,
                curso TEXT,
                idade DATE,
                foto TEXT
                FOREING KEY (id_responsavel) REFERENCES responsavel(id)      
                        )

            CREATE TABLE IF NOT EXISTS responsavel(
                id INTERGER AUTO_INCREMENT PRIMARY KEY ,
                nome TEXT,
                email TEXT,
                telefone int

            )

            CREATE TABLE IF NOT EXISTS funcionario(
                id INTEGER AUTO_INCREMENT PRIMARY KEY,
                nome TEXT,
                cargo TEXT,
                code TEXT

            )

            CREATE TABLE IF NOT EXISTS visitas (
                id INTEGER AUTO_INCREMENT PRIMARY KEY,
                nome TEXT,
                CPF INT,
                contato INT
            )

            )""")
        self.cursor.execute(Tab_cadastro)
        print("Tabela Criada Com sucesso")
        self.connection.commit
        

        

def cadastrar_Aluno1(self, nome, idade, matricula, curso, turno, code, nomeresp, emailresp, telefoneresp, foto):
    db =Database_cad
    try:
        # Primeiro, insira os dados na tabela 'responsavel'
        self.cursor.execute('''
            INSERT INTO responsavel (nome, email, telefone)
            VALUES (?, ?, ?)
        ''', (nomeresp, emailresp, telefoneresp))
        
        # Em seguida, obtenha o ID do responsável inserido
        id_responsavel = self.cursor.lastrowid
        
        # Agora, insira os dados na tabela 'aluno' usando o ID do responsável
        self.cursor.execute('''
            INSERT INTO aluno (nome, idade, matricula, curso, turno, code, id_responsavel, foto)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, idade, matricula, curso, turno, code, id_responsavel, foto))
        
        self.connection.commit()
        print("Aluno cadastrado com sucesso!")
        self.Desconect()
    except Exception as e:
        print(f"Erro ao cadastrar aluno: {str(e)}")
        self.Desconect()
        
        
    def Desconect(self):
        print("Desconectando ao banco de dados")
        self.connection.close()