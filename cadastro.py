import bcrypt
from dataBase import Database

def cadastro(new_User,new_Pass,new_Pass2,senha_Mae2):
    if senha_Mae2 == "1234" and new_Pass == new_Pass2: 

        db = Database()
        senhaCrip = bcrypt.hashpw(new_Pass.encode("utf-8"), bcrypt.gensalt())
        db.inserir_usuario(new_User,senhaCrip)
        return True
    else:
        return False
    
    
   