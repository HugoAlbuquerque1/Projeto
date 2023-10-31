import flet as ft

import login2
from time import sleep
import cadastro
from login_page import LoginPage
from tela3 import Tela2
from tela_entrada import Tela1
from tela_Info import Tela3
from tela_cadastro import Tela4


def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.GREEN_700,
            primary_container=ft.colors.GREEN,
            on_primary_container=ft.colors.GREEN_200,
            on_secondary=ft.colors.GREEN_300,
        ),
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_100
    page.window_width = 500  # Largura da janela é de 200 pixels
    page.window_height = 600  # Altura da janela é de 200 pixels
    page.window_resizable = False  # A janela não é redimensionável
    page.title = "login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    def fechar(e):
        page.window_destroy()

    def route_change(route):
        def botaologoff(e):
            page.window_full_screen = False
            page.window_width = 500  # Largura da janela é de 200 pixels
            page.window_height = 600
            page.update()
            page.go("/")


        # pagina app

        appbar_items = [    
            ft.PopupMenuItem(text="Fechar", on_click=fechar),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="logoff", on_click=botaologoff),
        ]
        appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.DOOR_SLIDING_OUTLINED,color=ft.colors.WHITE),
            leading_width=100,
            title=ft.Text("Controle de Acesso", size=32, text_align="start",color=ft.colors.WHITE),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.colors.BLACK,
            actions=[
                ft.Container(          
                    content=ft.PopupMenuButton(items=appbar_items),
                    margin=ft.margin.only(left=50, right=25),
                )
            ],
        )
        telalogin = LoginPage()
        page.views.append(
            
            ft.View(
                "/",
                [telalogin],
                bgcolor=ft.colors.WHITE,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        if page.route == "/app":
            page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLACK,
            primary_container=ft.colors.BLACK,
            on_primary_container=ft.colors.BLACK,
            on_secondary=ft.colors.BLACK,
            

            
        ),
    )
            page.window_full_screen = True
            page.update()
            page.views.append(
                ft.View(
                    "/app",
                    [
                        appbar,
                        ft.Row(
                            [
                                rail,
                                ft.VerticalDivider(width=1),
                                safeArea,
                            ],
                            expand=True,
                        ),
                    ],
                    bgcolor=ft.colors.WHITE,
                )
            )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    tela1 = Tela1()
    tela2 = Tela2()
    tela3 = Tela3()
    tela4 =  Tela4()
    screen_list = [tela1, tela2, tela3,tela4]
    safeArea = ft.SafeArea(content=screen_list[0], expand=True)

    def set_screen(e):
        safeArea.content = screen_list[e.control.selected_index]
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER,
                selected_icon=ft.icons.FAVORITE,
                label="Entrada",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Saida",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Visitas"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Cadastro"),
            ),
        ],
        on_change=set_screen,
    )


ft.app(target=main)
