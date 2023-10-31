import bcrypt
from dataBase import Database
#Função responsavel pelo cadastro administrativo 
def cadastro1(new_User,new_Pass,new_Pass2,senha_Mae2):
    #verifica se a senha mãe é igual a senha e verifica de a senha de confirmação está igual
    if senha_Mae2 == "1234" and new_Pass == new_Pass2: 

        db = Database()
        db.iniciar()
        #encripta a senha antes de enviar pro bd
        senhaCrip = bcrypt.hashpw(new_Pass.encode("utf-8"), bcrypt.gensalt())
        
        db.inserir_usuario(new_User,senhaCrip)
        db.Desconect()
        return True
    else:
        return False
    
    
   