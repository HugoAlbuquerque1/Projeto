import flet as ft

logado = False

def main(page: ft.Page):
    page.title = "Routes Example"

    def teste(e):
        logado = True
        print(logado)

    def route_change(route):
        print("Sistema de rotas")
        print(page.route)
        page.views.clear() # Limpa sua lista de rotas

        page.views.append(
            ft.View(
                "/login",
                [
                    ft.AppBar(title=ft.Text("Tela de login"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("login123", on_click= teste),
                    ft.ElevatedButton("login", on_click=lambda _: page.go("/home")),
                ],
            )
        )
        
        if (page.route == "/home"):
            page.clor
            page.views.append(
                ft.View(
                    "/home",
                    [
                        ft.AppBar(title=ft.Text("Home page"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Olá mundo", on_click=lambda _: page.go("/login")),
                    ],
                )
            )

        # if page.route == "/home":
        #     page.views.append(
        #         ft.View(
        #             "/store",
        #             [
        #                 ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
        #                 ft.ElevatedButton("Olá mundo", on_click=lambda _: page.go("/login")),
        #             ],
        #         )
        #     )
        print(page.route)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)