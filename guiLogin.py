import flet as ft
import login2
from time import sleep
def main(page: ft.Page):
    
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.GREEN_700,
            primary_container=ft.colors.GREEN_100,
            on_primary_container=ft.colors.GREEN_200,
            on_secondary=ft.colors.GREEN_300
            
        ),
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_100
    page.window_width = 500 # Largura da janela é de 200 pixels
    page.window_height = 600  # Altura da janela é de 200 pixels
    page.window_resizable = False  # A janela não é redimensionável
    page.title = "login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    def login(e):
        
        #verifica se a entrada user ta prenchida
        if not usernameLogin.value:
            #se o user for vazio imprime mensagem de erro na tela
            usernameLogin.error_text = "Campo Obrigatorio "
            page.update()
        #verifica se a senha foi prenchida
        if not password.value:
            #se o senha for vazio imprime mensagem de erro na tela
            password.error_text = "Campo Obrigatorio"
            page.update()
        else:
            #se estiver os dois campos verificados ele captura a variavel e armazena em user e senha
            user = usernameLogin.value
            senha = password.value
            #aqui ele chama a função login que ta em, outra pasta 
            if login2.login(user, senha): 
                #se o retorno for true deu certo
                print("Login bem-sucedido!")
                page.clean()
            else:
                #se o retorno for falso ele imprime erro
                page.controls.append(ft.Text("Error Tenta novamente",color="#591C21"))
                page.update()
                sleep(1)
                page.controls.pop()
                page.update()
                
             
        
    usernameLogin = ft.TextField(label="Usuário",width=300, text_align=ft.TextAlign.CENTER,
                                 color=ft.colors.GREEN_900)
    password = ft.TextField(label="Senha",width=300, text_align=ft.TextAlign.CENTER,color=ft.colors.GREEN_900)

    

    page.add(
            ft.Container(
                ft.Stack(
                    controls=[                
                    usernameLogin,
                    password,
                    ft.ElevatedButton("Fazer Login",icon="arrow_circle_right",bgcolor=ft.colors.GREEN_200,
                                         top=250,right=100,on_click=login
                 )]),

                border_radius=8,
                padding=20,
                width=400,
                height=500,
                bgcolor=ft.colors.GREY,
            )
        )

ft.app(target=main)


