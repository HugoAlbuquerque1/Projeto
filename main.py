import tkinter as tk
from tkinter import PhotoImage
import login  # Importando as funções do arquivo functions.py
import cadastro
from PIL import Image, ImageTk
class App:
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

    def show_error(self, error_message):
        self.error_label.config(text=error_message)

    def open_registration(self):
        self.root.withdraw()  # Esconde a janela atual de login
        registration_window = tk.Toplevel()  # Cria uma nova janela de cadastro
        registration_app = RegistrationApp(registration_window, self.root)  # Passa a referência da janela de login
        registration_window.mainloop()

class RegistrationApp:
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


        self.frameCima = tk.Frame(self.root, background="#DAFDBA")
        self.frameCima.place(relx=0.0, rely=0.0, relheight=10,relwidth=0.08)


        self.entrada_Alunos= tk.Button(self.root, text='Entrada',font=("Inter", 12),borderwidth=5,relief="ridge")
        self.entrada_Alunos.place(relx=0.01,rely=0.01,relheight=0.05,relwidth=0.06)


        self.saida_Alunos= tk.Button(self.root, text='Saida',font=("Inter", 12),borderwidth=5,relief="ridge")
        self.saida_Alunos.place(relx=0.01,rely=0.10,relheight=0.05,relwidth=0.06)

        self.visitas= tk.Button(self.root, text="Visitas",font=("Inter", 12),borderwidth=5,relief="ridge")
        self.visitas.place(relx=0.01,rely=0.20,relheight=0.05,relwidth=0.06)

        self.Cadastro= tk.Button(self.root,text="Cadastro",font=("Inter", 12),borderwidth=5,relief="ridge")
        self.Cadastro.place(relx=0.01,rely=0.30,relheight=0.05,relwidth=0.06)

        self.Fechar= tk.Button(self.root, text="fechar",font=("Inter", 12),command=self.close_app,borderwidth=5,relief="ridge")
        self.Fechar.place(relx=0.01,rely=0.90,relheight=0.05,relwidth=0.06)


    def close_app(self):
        self.root.destroy()  # Fecha a janela principal



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
