import flet as ft
import login2
from flet import (
    UserControl,
    Column,
    Container,
    Row,
    Text,
    NavigationRail,
    NavigationRailDestination,
    alignment,
    border_radius,
    colors,
    icons,
    padding,
    margin,
)
from time import sleep
import cadastro
'''def main(page: ft.Page): 
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.GREEN_700,
            primary_container=ft.colors.GREEN,
            on_primary_container=ft.colors.GREEN_200,
            on_secondary=ft.colors.GREEN_300        
        ),
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor= ft.colors.GREY_100
    page.window_width = 500 # Largura da janela é de 200 pixels
    page.window_height = 600  # Altura da janela é de 200 pixels
    page.window_resizable = False  # A janela não é redimensionável
    page.title = "login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()'''


def app(page: ft.Page):
    def fechar(e):
        page.window_destroy()


    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor= ft.colors.GREY_100
    page.window_frameless = True
    page.window_full_screen = True
    page.window_resizable = False  # A janela não é redimensionável
    page.title = "Controle de Acesso"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    
    appbar_items = [
            ft.PopupMenuItem(text="Fechar",on_click=fechar),
            ft.PopupMenuItem(),  # divider
            ]
    appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text("Controle de Acesso",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.colors.GREEN,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ])
    
    def top_nav_change(e):
        top_nav_rail.selected_index = ft.control.selected_index
        page.update()
    
    top_nav_items = [
            NavigationRailDestination(
                label_content=Text("Boards"),
                label="Boards",
                icon=icons.BOOK_OUTLINED,
                selected_icon=icons.BOOK_OUTLINED

            ),
            NavigationRailDestination(
                label_content=Text("Members"),
                label="Members",
                icon=icons.PERSON,
                selected_icon=icons.PERSON
            ),
    ]

    top_nav_rail = NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=top_nav_change,
            destinations=top_nav_items,
            bgcolor=colors.BLUE_GREY,
            extended=True,
            expand=True
        )
    
    view = Container(
            content=ft.Column([
                ft.Row([
                    Text("Workspace"),
                ]),
                # divider
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
                top_nav_rail(),
                # divider
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
            ], tight=True),
            padding=ft.padding.all(15),
            margin=margin.all(0),
            width=250,
            bgcolor=colors.BLUE_GREY,
        )
    


    page.add(appbar, view,top_nav_rail,top_nav_items)









'''    def cadastroadm(e):
        new_User = userCadastro.value
        new_Pass = senha.value
        new_Pass2 = senha2.value
        senha_Mae2 = senhaMae.value

        if cadastro.cadastro1(new_User,new_Pass,new_Pass2,senha_Mae2):
            page.controls.append(ft.Text("Cadastro realizado com sucesso",color="#591C21"))
            page.update()
            sleep(1)
            page.controls.pop()
            page.update() 

        else:
                page.controls.append(ft.Text("Error Tente novamente",color="#591C21"))
                page.update()
                sleep(1)
                page.controls.pop()
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
                page.controls.append(ft.Text("Error Tente novamente",color="#591C21"))
                page.update()
                sleep(1)
                page.controls.pop()
                page.update()
                app()
     #widgets login           
    usernameLogin = ft.TextField(label="Usuário",cursor_color=ft.colors.GREEN_900  
                                 ,border_color=ft.colors.GREEN_900,height=75, text_align=ft.TextAlign.CENTER,
                                color=ft.colors.GREEN_900,
                                bgcolor=ft.colors.GREY_100)
    
    password = ft.TextField(label="Senha",height=75,cursor_color=ft.colors.GREEN_900, border_color=ft.colors.GREEN_900,text_align=ft.TextAlign.CENTER,color=ft.colors.GREEN_900,
                            password=True, can_reveal_password=True,bgcolor=ft.colors.GREY_100)
    
    botao = ft.ElevatedButton("Fazer Login",icon="arrow_circle_right",bgcolor=ft.colors.GREEN_200,
                                        on_click=login)

    #widgets cadastro
    userCadastro = ft.TextField(label="Usuário", cursor_color=ft.colors.GREEN_900  
                                 ,border_color=ft.colors.GREEN_900,height=75, text_align=ft.TextAlign.CENTER,
                                color=ft.colors.GREEN_900,
                                bgcolor=ft.colors.GREY_100)   

    senha = ft.TextField(label="senha", cursor_color=ft.colors.GREEN_900  
                                 ,password=True, can_reveal_password=True,border_color=ft.colors.GREEN_900,height=75, text_align=ft.TextAlign.CENTER,
                                color=ft.colors.GREEN_900,
                                bgcolor=ft.colors.GREY_100)    


    senha2 = ft.TextField(label="confirmação da senha", cursor_color=ft.colors.GREEN_900 ,
                          password=True, can_reveal_password=True 
                                 ,border_color=ft.colors.GREEN_900,height=75, text_align=ft.TextAlign.CENTER,
                                color=ft.colors.GREEN_900,
                                bgcolor=ft.colors.GREY_100)   
    senhaMae = ft.TextField(label="senha mãe", cursor_color=ft.colors.GREEN_900,
                            password=True, can_reveal_password=True 
                                 ,border_color=ft.colors.GREEN_900,height=75, text_align=ft.TextAlign.CENTER,
                                color=ft.colors.GREEN_900,
                                bgcolor=ft.colors.GREY_100) 

    botaocad = ft.ElevatedButton("Fazer cadastro",icon="arrow_circle_right",bgcolor=ft.colors.GREEN_200,
                                        on_click=cadastroadm)



    tabs = ft.Tabs(
            selected_index=2,
            animation_duration=500,
            label_color=ft.colors.GREEN_700, 
            unselected_label_color=ft.colors.GREY_700,     
            tabs=[
                ft.Tab(
                    text= "Login",
                    content=ft.Container(  
                        ft.Container(      
                            content=ft.Column(
                                [
                                ft.Container(
                                alignment=ft.alignment.center,
                                content= ft.Image(
                                src="fotos/ifpa.png", 
                                width=150,
                                height=150,
                            ),
                                padding=5,
                                width=300,
                                ),
                                ft.Container(
                                alignment=ft.alignment.center,
                                content=usernameLogin,
                                padding=5,
                                width=300,
                                ),
                                ft.Container(
                                alignment=ft.alignment.center,
                                content=password,
                                padding=5,
                                width=300,
                            ),
                                ft.Container(
                                alignment=ft.alignment.center,
                                content=botao, 
                                padding=5,
                                width=300,
                            )]),
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.GREY_300,
                        width=200,
                        height=250,
                        border_radius=10,            
                    ),        
                    ),
                ),
                ft.Tab(
                    text="cadastro",
                    content=ft.Container(
                        ft.Container(
                            content=ft.Column(
                                [
                                ft.Container(
                                alignment=ft.alignment.center,
                                content= ft.Image(
                                src="fotos/ifpa.png", 
                                width=125,
                                height=125,
                                 ),
                                padding=5,
                                width=300,
                                ),
                                ft.Container(
                                alignment=ft.alignment.center,
                                content=userCadastro,
                                height=50,
                                width=300,
                                ),
                                ft.Container(
                                alignment=ft.alignment.center,
                                content=senha,
                                height=50,
                                width=300,
                                ),
                                ft.Container(
                                alignment=ft.alignment.center,
                                content=senha2,
                                height=50,
                                width=300,
                            ),
                                ft.Container(
                                alignment=ft.alignment.center,
                                content=senhaMae, 
                                height=50,
                                width=300,
                            ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    content=botaocad, 
                                    height=50,
                                    width=300,
                            )]

                            ),
                        
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.GREY_300,
                        width=200,
                        height=250,
                        border_radius=10,

                        ),
                        
                    ),
                    
                ),
            ],

            width=400,
            height=400,
        )

    fundo =  ft.Container(
            bgcolor=ft.colors.GREY_100,
            content=tabs,
            border_radius=10,
            width=400,
            height=500,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.BLUE_GREY_700,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ))
    
    page.add(

        fundo
        )'''


ft.app(target=app)


