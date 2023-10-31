from flet import *
import login2
from time import sleep
import cadastro


class LoginPage(UserControl):

    def __init__(self):
        super().__init__()
    def cadastroadm(self,e):
        if not self.userCadastro.value:
            # se o user for vazio imprime mensagem de erro na tela
            self.userCadastro.error_text = "Campo Obrigatorio "
            self.update()

        if not self.senha.value:
            # se o user for vazio imprime mensagem de erro na tela
            self.senha.error_text = "Campo Obrigatorio "
            self.update()

        if not self.senha2.value:
            # se o user for vazio imprime mensagem de erro na tela
            self.senha2.error_text = "Campo Obrigatorio "
            self.update()

        if not self.senhaMae.value:
            # se o user for vazio imprime mensagem de erro na tela
            self.senhaMae.error_text = "Campo Obrigatorio "
            self.update()

        else:
            new_User = self.userCadastro.value
            new_Pass = self.senha.value
            new_Pass2 = self.senha2.value
            senha_Mae2 = self.senhaMae.value

            if cadastro.cadastro1(new_User, new_Pass, new_Pass2, senha_Mae2):
                self.controls.append(
                    Text("Cadastro realizado com sucesso", color="#591C21")
                )
                self.update()
                sleep(1)
                self.controls.pop()
                self.update()

            else:
                self.controls.append(Text("Error Tente novamente", color="#591C21",TextAlign=alignment.center))                                       
                self.update()
                sleep(1)
                self.controls.pop()
                self.update()

    def login(self,e):
        # verifica se a entrada user ta prenchida
        if not self.usernameLogin.value:
            # se o user for vazio imprime mensagem de erro na tela
            self.usernameLogin.error_text = "Campo Obrigatorio "
            self.update()
        # verifica se a senha foi prenchida
        if not self.password.value:
            # se o senha for vazio imprime mensagem de erro na tela
            self.password.error_text = "Campo Obrigatorio"
            self.update()
        else:
            # se estiver os dois campos verificados ele captura a variavel e armazena em user e senha
            user = self.usernameLogin.value
            senha = self.password.value
            # aqui ele chama a função login que ta em, outra pasta
            if login2.login(user, senha):
                # se o retorno for true deu certo
                print("Login bem-sucedido!")
                self.page.clean()
                self.page.go("/app")

            else:
                # se o retorno for falso ele imprime erro
                self.page.controls.append(
                    Text("Error Tente novamente", color="#591C21")
                )
                self.update()
                sleep(1)
                self.page.controls.pop()
                self.update()

        
    def build(self):
        self.usernameLogin = TextField(
            label="Usuário",
            cursor_color=colors.GREEN_900,
            border_color=colors.GREEN_900,
            height=75,
            text_align=TextAlign.CENTER,
            color=colors.GREEN_900,
            bgcolor=colors.GREY_100,
        )

        self.password = TextField(
            label="Senha",
            height=75,
            cursor_color=colors.GREEN_900,
            border_color=colors.GREEN_900,
            text_align=TextAlign.CENTER,
            color=colors.GREEN_900,
            password=True,
            can_reveal_password=True,
            bgcolor=colors.GREY_100,
        )

        self.botao = ElevatedButton(
            "Fazer Login",
            icon="arrow_circle_right",
            bgcolor=colors.GREEN_200,
            on_click=self.login,
        )  # widgets cadastro
        self.userCadastro = TextField(
            label="Usuário",
            cursor_color=colors.GREEN_900,
            border_color=colors.GREEN_900,
            height=75,
            text_align=TextAlign.CENTER,
            color=colors.GREEN_900,
            bgcolor=colors.GREY_100,
        )

        self.senha = TextField(
            label="senha",
            cursor_color=colors.GREEN_900,
            password=True,
            can_reveal_password=True,
            border_color=colors.GREEN_900,
            height=75,
            text_align=TextAlign.CENTER,
            color=colors.GREEN_900,
            bgcolor=colors.GREY_100,
        )

        self.senha2 = TextField(
            label="confirmação da senha",
            cursor_color=colors.GREEN_900,
            password=True,
            can_reveal_password=True,
            border_color=colors.GREEN_900,
            height=75,
            text_align=TextAlign.CENTER,
            color=colors.GREEN_900,
            bgcolor=colors.GREY_100,
        )
        self.senhaMae = TextField(
            label="senha mãe",
            cursor_color=colors.GREEN_900,
            password=True,
            can_reveal_password=True,
            border_color=colors.GREEN_900,
            height=75,
            text_align=TextAlign.CENTER,
            color=colors.GREEN_900,
            bgcolor=colors.GREY_100,
        )



        self.botaocad = ElevatedButton(
            "Fazer cadastro",
            icon="arrow_circle_right",
            bgcolor=colors.GREEN_200,
            on_click=self.cadastroadm,
        )
        self.tabs = Tabs(
            selected_index=2,
            animation_duration=500,
            label_color=colors.GREEN_700,
            unselected_label_color=colors.GREY_700,
            tabs=[
                Tab(
                    text="Login",
                    content=Container(
                        Container(
                            content=Column(
                                [
                                    Container(
                                        alignment=alignment.center,
                                        content=Image(
                                            src="fotos/ifpa.png",
                                            width=150,
                                            height=150,
                                        ),
                                        padding=5,
                                        width=300,
                                    ),
                                    Container(
                                        alignment=alignment.center,
                                        content=self.usernameLogin,
                                        padding=5,
                                        width=300,
                                    ),
                                    Container(
                                        alignment=alignment.center,
                                        content=self.password,
                                        padding=5,
                                        width=300,
                                    ),
                                    Container(
                                        alignment=alignment.center,
                                        content=self.botao,
                                        padding=5,
                                        width=300,
                                    ),
                                ]
                            ),
                            alignment=alignment.center,
                            bgcolor=colors.GREY_300,
                            width=200,
                            height=250,
                            border_radius=10,
                        ),
                    ),
                ),
                Tab(
                    text="cadastro",
                    content=Container(
                        Container(
                            content=Column(
                                [
                                    Container(
                                        alignment=alignment.center,
                                        content=Image(
                                            src="fotos/ifpa.png",
                                            width=125,
                                            height=125,
                                        ),
                                        padding=5,
                                        width=300,
                                    ),
                                    Container(
                                        alignment=alignment.center,
                                        content=self.userCadastro,
                                        height=50,
                                        width=300,
                                    ),
                                    Container(
                                        alignment=alignment.center,
                                        content=self.senha,
                                        height=50,
                                        width=300,
                                    ),
                                    Container(
                                        alignment=alignment.center,
                                        content=self.senha2,
                                        height=50,
                                        width=300,
                                    ),
                                    Container(
                                        alignment=alignment.center,
                                        content=self.senhaMae,
                                        height=50,
                                        width=300,
                                    ),
                                    Container(
                                        alignment=alignment.center,
                                        content=self.botaocad,
                                        height=50,
                                        width=300,
                                    ),
                                ]
                            ),
                            alignment=alignment.center,
                            bgcolor=colors.GREY_300,
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
        self.fundo = Container(
            bgcolor=colors.GREY_100,
            content=self.tabs,
            border_radius=10,
            width=400,
            height=500,
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=colors.BLUE_GREY_700,
                offset=Offset(0, 0),
                blur_style=ShadowBlurStyle.OUTER,
            ),
        )
        # pagina app



        return Container(
            content=Column([
                self.fundo
            ]),
        )



