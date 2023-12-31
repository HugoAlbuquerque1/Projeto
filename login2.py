import bcrypt
from dataBase import Database


def login(username, password):
    db = Database()  # Crie uma instância da classe Database
    db.iniciar()
    result = db.fazer_Login(username)  # Busque o resultado da consulta

    if result is not None:
        stored_username = result[0]
        stored_password = result[1]  # Obtenha a senha encriptada armazenada no banco de dados
        
        # Compare a senha fornecida durante o login com a senha encriptada armazenada
        if bcrypt.checkpw(password.encode("utf-8"), stored_password):
            db.Desconect()
            print("login realizado com sucesso")
            return True  # Senha válida
    db.Desconect()
    print("login n foi realizado")
    return False  # Senha inválida ou usuário não encontrado



