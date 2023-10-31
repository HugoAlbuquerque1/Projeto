
from databaseCad import Database_cad

def cadastrar_Aluno1(nome, matricula, datanasc, turma, turno, curso, nomeresp, email, telefone, code):
        db = Database_cad()
        try:
            db.iniciar()
            # Primeiro, insira os dados na tabela 'responsavel'
            db.cursor.execute('''
                INSERT INTO responsavel (nome, email, telefone)
                VALUES (?, ?, ?)
            ''', (nomeresp, email, telefone))
            db.connection.commit()
            
            # Em seguida, obtenha o ID do responsável inserido
            
            id_responsavel = db.cursor.lastrowid
            
            # Agora, insira os dados na tabela 'aluno' usando o ID do responsável
            db.cursor.execute('''
                INSERT INTO aluno (matricula, nome,  code,id_responsavel,  turno, curso,   turma, datanasc)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matricula,nome,  code, id_responsavel, turno,curso,  turma, datanasc ))
            
            db.connection.commit()
            print("Aluno cadastrado com sucesso!")

            db.Desconect()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar aluno: {str(e)}")
            db.Desconect()
            return False
