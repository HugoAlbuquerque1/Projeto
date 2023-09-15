import tkinter as tk
from tkinter import PhotoImage
import login  # Importando as funções do arquivo functions.py
import cadastro
from PIL import Image, ImageTk
from dataBase import Database
import atexit
import shutil
from tkinter import filedialog
import os 


# Função para fechar a conexão do banco de dados quando o programa for encerrado
def close_database_connection():
    db = Database()
    db.Desconect()

atexit.register(close_database_connection)


class App:
    #Janela de login 
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Acesso")
        self.frame = tk.Frame(self.root)
        self.root.configure(background='#023535')
        self.root.minsize(width=250, height=250)

        self.username_label = tk.Label(self.root, text="Usuário:",fg="white",background="#023535",
                              font=("Inter", 20))
        self.username_label.place(relx=0.05,rely=0.02)

        self.username_entry = tk.Entry(self.root,background="#D8FFDB",fg="black",
                              font=("Inter", 12))
        self.username_entry.place(relx=0.05,rely=0.15, relwidth=0.80)

        self.password_label = tk.Label(self.root, text="Senha:",background="#023535",fg="white",
                              font=("Inter", 20))
        self.password_label.place(relx=0.05,rely=0.25)

        self.password_entry = tk.Entry(self.root,background="#D8FFDB",fg="black",
                              font=("Inter", 12), show="*")
        self.password_entry.place(relx=0.05,rely=0.40, relwidth=0.80)

        self.login_button = tk.Button(self.root, text="Login",background="#D8FFDB",fg="black",
                              font=("Inter", 12), command=self.login)
        self.login_button.place(relx=0.05,rely=0.60, relwidth=0.40)

        self.register_button = tk.Button(self.root, text="Cadastro",background="#D8FFDB",fg="black",
                              font=("Inter", 12), command=self.open_registration)
        self.register_button.place(relx=0.50,rely=0.60, relwidth=0.40)

        self.error_label = tk.Label(self.root, text="", fg="red",background="#D8FFDB")  # Label para exibir mensagens de erro
        self.error_label.place(relx=0.05, rely=0.75)
    #função responsável em fazer o login 
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if login.login(username, password): 
            print("Login bem-sucedido!")
            self.root.destroy()  # Fecha a janela de login
            app_window = tk.Tk()  # Cria a janela principal do aplicativo
            app_main = AppMain(app_window)
            app_window.mainloop()
        else:
            self.show_error("Credenciais inválidas")
    #Acusa erro de login
    def show_error(self, error_message):
        self.error_label.config(text=error_message)
    #função responsavel por abrir a janela de cadastro 
    def open_registration(self):
        self.root.withdraw()  # Esconde a janela atual de login
        registration_window = tk.Toplevel()  # Cria uma nova janela de cadastro
        registration_app = RegistrationApp(registration_window, self.root)  # Passa a referência da janela de login
        registration_window.mainloop()

class RegistrationApp:
    #janela de cadastro administrativo
    def __init__(self, root, login_window):
        self.root = root
        self.login_window = login_window  # Referência à janela de login
        self.root.title("Cadastro de Funcionário")
        self.frame = tk.Frame(self.root)
        self.root.configure(background='#023535')
        self.root.minsize(width=250, height=300)

        self.label = tk.Label(self.root, text="Novo Cadastro Adiministrativo",background="#023535",fg="white",
                              font=("Inter", 11))
        self.label.place(relx=0.05, rely=0.01)

        self.new_Name = tk.Label(self.root, text="Usuário:",background="#023535",fg="white",
                              font=("Inter", 15))
        self.new_Name.place(relx=0.05, rely=0.07)

        self.name_Entry =tk.Entry(self.root,background="#D8FFDB",fg="black",
                              font=("Inter", 12))
        self.name_Entry.place(relx=0.05,rely=0.17)

        self.new_Pass = tk.Label(self.root, text="Senha",background="#023535",fg="white",
                              font=("Inter", 15))
        self.new_Pass.place(relx=0.05,rely=0.27)

        self.pass_Entry =tk.Entry(self.root, show="*",background="#D8FFDB",fg="black",
                              font=("Inter", 12))
        self.pass_Entry.place(relx=0.05,rely=0.37)

        self.new_Pass2 = tk.Label(self.root, text="Confirmar senha",background="#023535",fg="white",
                              font=("Inter", 15))
        self.new_Pass2.place(relx=0.05,rely=0.47)

        self.pass2_Entry =tk.Entry(self.root, show="*",background="#D8FFDB",fg="black",
                              font=("Inter", 12))
        self.pass2_Entry.place(relx=0.05,rely=0.57)

        self.senha_Mae = tk.Label(self.root, text="Senha Mãe ",background="#023535",fg="white",
                              font=("Inter", 15))
        self.senha_Mae.place(relx=0.05,rely=0.67)

        self.senha_Mae2 =tk.Entry(self.root, show="*",background="#D8FFDB",fg="black",
                              font=("Inter", 12))
        self.senha_Mae2.place(relx=0.05,rely=0.77)

        self.login_button = tk.Button(self.root, text="Cadastrar",background="#D8FFDB",fg="black",
                              font=("Inter", 10), command=self.cadastro)
        self.login_button.place(relx=0.55,rely=0.87, relwidth=0.30)

        self.error_label = tk.Label(self.root, text="", background="#D8FFDB",fg="red")  # Label para exibir mensagens de erro
        self.error_label.place(relx=0.05, rely=0.87)

    #função que faz o cadastro 
    def cadastro(self):
        new_User = self.name_Entry.get()
        new_Pass = self.pass_Entry.get()
        new_Pass2 = self.pass2_Entry.get()
        senha_Mae2 = self.senha_Mae2.get()

        if cadastro.cadastro(new_User,new_Pass,new_Pass2,senha_Mae2):
            self.root.destroy()  # Fecha a janela de cadastro
            self.login_window.deiconify()
        else:
            self.show_error("Credenciais inválidas")
    
    def show_error(self, error_message):
        self.error_label.config(text=error_message)

class AppMain:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo Principal")  
          
        self.frame = tk.Frame(self.root)
        self.root.configure(background='#023535')
        lado, cima = (root.winfo_screenwidth()), (root.winfo_screenheight())
        self.root.geometry('%dx%d+0+0' % (lado, cima))
        self.root.resizable(True, True,)
        self.root.attributes('-fullscreen', True)

        self.current_frame = None
        self.frame_Cad = None
        self.frames = []

        self.frame_entrada = tk.Frame(self.root, background='#D6D58E')
        self.frame_saida = tk.Frame(self.root, background='#D6D58E')
        self.frame_visitas = tk.Frame(self.root, background='#D6D58E')
        self.frame_cadastro = tk.Frame(self.root, background='#D6D58E')

        self.frames.extend([self.frame_entrada, self.frame_saida, self.frame_visitas, self.frame_cadastro])
        self.buttons = [
            ("Entrada", self.frame_entrada),
            ("Saida", self.frame_saida),
            ("Visitas", self.frame_visitas),
            ("Cadastro", self.frame_cadastro)    
        ]

        self.frame_cadastro_A =tk.Label(self.frame_cadastro, background='#D6D58E')
        
        self.frame_cadastro_Func =tk.Label(self.frame_cadastro, background='#D6D58E')



        self.cadastro_funcionario = tk.Button(self.frame_cadastro, text="Cadastro funcionario",command=self.show_Aba_Cadastro_funcionario)
        self.cadastro_funcionario.place(relx=0.01, rely=0.01)

        self.cadastro_Aluno = tk.Button(self.frame_cadastro, text="Cadastro Aluno",command=self.show_Aba_Cadastro_Aluno)
        self.cadastro_Aluno.place(relx=0.15, rely=0.01)

        self.image = PhotoImage(file="fotos/Santos.png")  # Substitua pelo caminho da sua imagem
        self.image_label = tk.Label(self.frame_entrada, image=self.image)
        self.image_label.place(relx=0.01, rely=0.01)

    
        self.dados_Aluno = tk.Label(self.frame_cadastro_A,text="Dados Discente", background="#023535",
                                   fg="White",font=("Inter", 20)) 
        self.dados_Aluno.place(relx=0.01, rely=0.01)
              
        self.nome_Aluno = tk.Label(self.frame_cadastro_A,text="Nome Do Aluno", background="#D6D58E",
                                   fg="#023535",font=("Inter", 20) )
        self.nome_Aluno.place(relx=0.01, rely=0.05)
        
        self.Entry_Aluno = tk.Entry(self.frame_cadastro_A, background="white",font=("Inter", 15))
        self.Entry_Aluno.place(relx=0.01,rely=0.10,relwidth=0.30,relheight=0.03)

        self.data_Nascimento = tk.Label(self.frame_cadastro_A,text="Data de nascimento", background="#D6D58E",
                                   fg="#023535",font=("Inter", 20) ) 
        self.data_Nascimento.place(relx=0.01,rely=0.15)

        self.data_Entry = tk.Entry(self.frame_cadastro_A, background="white",font=("Inter", 15))
        self.data_Entry.place(relx=0.01,rely=0.20,relwidth=0.15,relheight=0.03)
        self.data_Entry.bind('<KeyPress>', self.on_date)


        self.matricula_label = tk.Label(self.frame_cadastro_A,text="Numero de matricula", background="#D6D58E",
                                   fg="#023535",font=("Inter", 20)) 
        self.matricula_label.place(relx=0.01, rely=0.25)

        self.matricula_entry = tk.Entry(self.frame_cadastro_A, background="white", font=("Inter", 15))
        self.matricula_entry.place(relx=0.01,rely=0.30,relwidth=0.30,relheight=0.03)

        self.curso_Label = tk.Label(self.frame_cadastro_A,text="curso", background="#D6D58E",
                                   fg="#023535",font=("Inter", 20) ) 
        self.curso_Label.place(relx=0.01, rely=0.35)

        self.curso_entry = tk.Entry(self.frame_cadastro_A, background="white", font=("Inter", 15))
        self.curso_entry.place(relx=0.01,rely=0.40,relwidth=0.30,relheight=0.03)





        self.Turma_Label = tk.Label(self.frame_cadastro_A,text="Turma", background="#D6D58E",
                                   fg="#023535",font=("Inter", 20) ) 
        self.Turma_Label.place(relx=0.01, rely=0.45,relwidth=0.25, relheight=0.03)

        self.Turma_entry = tk.Entry(self.frame_cadastro_A, background="white", font=("Inter", 12))
        self.Turma_entry.place(relx=0.01,rely=0.50,relwidth=0.25,relheight=0.03)

        self.turno_Label = tk.Label(self.frame_cadastro_A,text="Turno", background="#D6D58E",
                                   fg="#023535",font=("Inter", 20)) 
        self.turno_Label.place(relx=0.25, rely=0.45,relwidth=0.25, relheight=0.03)

        self.turno_entry = tk.Entry(self.frame_cadastro_A, background="white", font=("Inter", 12))
        self.turno_entry.place(relx=0.25,rely=0.50,relwidth=0.25,relheight=0.03)



        self.Dadosresp_Label = tk.Label(self.frame_cadastro_A,text="Dados Responsavel", background="#023535",
                                   fg="White",font=("Inter", 20) ) 
        self.Dadosresp_Label.place(relx=0.01, rely=0.55)

         
        self.nomeresp_Label = tk.Label(self.frame_cadastro_A,text="Nome", background="#D6D58E",
                                   fg="#023535",font=("Inter", 20) ) 
        self.nomeresp_Label.place(relx=0.01, rely=0.60)

        self.nomeresp_entry = tk.Entry(self.frame_cadastro_A, background="white", font=("Inter", 15))
        self.nomeresp_entry.place(relx=0.01,rely=0.65,relwidth=0.30,relheight=0.03)

        self.email_Label = tk.Label(self.frame_cadastro_A,text="Email", background="#D6D58E",
                                   fg="#023535",font=("Inter", 20) ) 
        self.email_Label.place(relx=0.01, rely=0.70)

        self.email_entry = tk.Entry(self.frame_cadastro_A, background="white", font=("Inter", 15))
        self.email_entry.place(relx=0.01,rely=0.75,relwidth=0.30,relheight=0.03)

  
        self.Telefone_Label = tk.Label(self.frame_cadastro_A,text="Telefone", background="#D6D58E",
                                   fg="#023535",font=("Inter", 20) ) 
        self.Telefone_Label.place(relx=0.01, rely=0.80)

        self.Telefone_entry = tk.Entry(self.frame_cadastro_A, background="white", font=("Inter", 15))
        self.Telefone_entry.place(relx=0.01,rely=0.85,relwidth=0.30,relheight=0.03)
    
        self.foto = tk.Button(self.frame_cadastro_A,text="Selecionar foto",command=self.selecionar_Foto)
        self.foto.place(relx=0.05,rely=0.90)



        #wigets do frame de cadastro funcionario

        self.dados_funcionario = tk.Label(self.frame_cadastro_Func,text="Dados funcionario",background="#023535", fg="White",font=("Inter", 20))
        self.dados_funcionario.place(relx=0.05, rely=0.01)

        self.nome_Funcionario_Label = tk.Label(self.frame_cadastro_Func, text="Nome",background="#D6D58E",
                                   fg="#023535",font=("Inter", 20) )
        self.nome_Funcionario_Label.place(relx=0.05, rely=0.10)

        self.nome_Funcionario_Entry = tk.Entry(self.frame_cadastro_Func,background="white", font=("Inter", 15))
        self.nome_Funcionario_Entry.place(relx=0.05, rely=0.15)

        self.cargo_Funcionario = tk.Label(self.frame_cadastro_Func, text="Cargo",background="#D6D58E",
                                   fg="#023535",font=("Inter", 20) )
        self.cargo_Funcionario.place(relx=0.05,rely=0.20)

        self.cargo_Entry = tk.Entry(self.frame_cadastro_Func,background="white", font=("Inter", 15))
        self.cargo_Entry.place(relx=0.05, rely=0.25)

        self.botao_CadastroFuncionario = tk.Button(self.frame_cadastro_Func, text="Cadastrar")
        self.botao_CadastroFuncionario.place(relx=0.35, rely=0.30)

        self.botao_Foto_Func = tk.Button(self.frame_cadastro_Func, text="Foto",command=self.selecionar_Foto)
        self.botao_Foto_Func.place(relx=0.20, rely=0.30)

 

        for text, frame in self.buttons:
            button = tk.Button(self.root, text=text, font=("Inter", 12), command=lambda f=frame: self.show_frame(f))
            button.place(relx=0.01, rely=0.01 + self.buttons.index((text, frame)) * 0.10, relheight=0.05, relwidth=0.06)

        self.Fechar = tk.Button(self.root, text="fechar", font=("Inter", 12), command=self.close_app, borderwidth=5, relief="ridge")
        self.Fechar.place(relx=0.01, rely=0.90, relheight=0.05, relwidth=0.06)

        self.current_frame = None  # Frame atualmente exibido

        self.show_frame(self.frame_entrada)


    def cadastrar_Aluno(self):
        pass


    def selecionar_Foto(self):
        foto = filedialog.askopenfilename(
            filetypes=[
                ("PNG Files", "*.png"),
                ("GIF Files", "*.gif"),
                ("JPEG Files", "*.jpg *.jpeg")
            ]
        )
        if foto:
            Database_foto_folder = ("Controle de acesso/foto")
            os.makedirs(Database_foto_folder, exist_ok=True)
            shutil.copy(foto, Database_foto_folder)



    def on_date(self,event):
        position = self.data_Entry.index(tk.INSERT)
        if position == 2 or position == 5:
            self.data_Entry.insert(tk.INSERT, '/')

    def show_frame(self, frame):
        if self.current_frame is not None:
            self.current_frame.place_forget()  # Oculta o frame atual
        self.current_frame = frame
        self.current_frame.place(relx=0.08,rely=0.01, relheight=0.98,relwidth=0.91)

    def show_cad(self, frame):
        if self.frame_Cad is not None:
            self.frame_Cad.place_forget()
        self.frame_Cad = frame
        self.frame_Cad.place(relx=0.01,rely=0.05,relheight=0.90,relwidth=0.50)

    def show_Aba_Cadastro_Aluno(self):
        self.show_cad(self.frame_cadastro_A)

    def show_Aba_Cadastro_funcionario(self):
        self.show_cad(self.frame_cadastro_Func)

    def show_entrada_frame(self):
        self.show_frame(self.frame_entrada)

    def show_saida_frame(self):  
        self.show_frame(self.frame_saida)

    def show_visitas_frame(self):
        self.show_frame(self.frame_visitas)

    def show_cadastro_frame(self):
        self.show_frame(self.frame_cadastro)

    def close_app(self):
        self.root.destroy()  # Fecha a janela principal



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
