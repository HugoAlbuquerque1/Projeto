from databaseCad import Database_cad

def cadastrar_Func(nomefunc, matriculaFunc, cpf, telefoneFunc,codef):
        db = Database_cad()
        try:
            db.iniciar()

            db.cursor.execute('''
                INSERT INTO funcionario (nomefunc, matriculaFunc, cpf, telefoneFunc,codef)
                VALUES (?, ?, ?,?,?)
            ''', (nomefunc, matriculaFunc, cpf, telefoneFunc, codef))
            db.connection.commit()
            
            
            db.connection.commit()
            print("Funcionario cadastrado com sucesso!")

            db.Desconect()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar Funcionario: {str(e)}")
            db.Desconect()
            return False
