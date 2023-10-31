from databaseCad import Database_cad

def cadastrar_Visit(nome, cpf, contato):
        db = Database_cad()
        try:
            db.iniciar()
            db.cursor.execute('''
                INSERT INTO visitas (nome, CPF, contato)
                VALUES (?, ?, ?)
            ''', (nome, cpf, contato))
            db.connection.commit()
        
            db.connection.commit()
            print("Visitas cadastrado com sucesso!")

            db.Desconect()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar visitas: {str(e)}")
            db.Desconect()
            return False
