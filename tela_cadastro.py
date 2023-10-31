from flet import *
import cadastrouser
import cadastroFunc
import cadastroVisit
from datetime import datetime
import qrcode
import os

class Tela4(UserControl):
    def __init__(self):
        super().__init__()

    
    def criar_qr(self,matricula):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # Aqui, você fornece a matrícula como dado a ser codificado no QR code
        qr.add_data(matricula)
        qr.make(fit=True)

        qr_code = qr.make_image(fill_color='black', back_color="white")

        pasta_aluno = f"qr_codes/{matricula}"
        if not os.path.exists(pasta_aluno):
            os.makedirs(pasta_aluno)

        caminho_arquivo = os.path.join(pasta_aluno, f"{matricula}.png")
        qr_code.save(caminho_arquivo)

        return caminho_arquivo

    def cadastrarVisit(self, e):

        if not self.nome.value:
            self.nome.error_text = "Campo Obrigatorio "
            self.update()
        if not self.cpf.value:
            self.cpf.error_text = "Campo Obrigatorio "
            self.update()
        if not self.contato.value:
            self.contato.error_text = "Campo Obrigatorio "
            self.update()
        else:
            nome = self.nome.value
            cpf = self.cpf.value
            contato =self.contato.value

            if cadastroVisit.cadastrar_Visit(nome,cpf,contato):
                self.page.controls.append(
                    Text("Cadastro realizado com sucesso", color="#591C21")
                )
                self.page.update()
                print("Deu certo ")
                self.page.controls.pop()
                self.update()
            else:
                print("Deu certo não")
                self.page.controls.append(Text("Error Tente novamente", color="#591C21"))
                self.page.update()
                self.page.controls.pop()
                self.page.update()


        

    def cadastrarFunc(self,e ):
        if not self.Nome_Func.value:
            self.Nome_Func.error_text = "Campo Obrigatorio "
            self.update()

        if not self.Matricula_Func.value:
            self.Matricula_Func.error_text = "Campo Obrigatorio "
            self.update()

        if not self.cpf.value:
            self.cpf.error_text = "Campo Obrigatorio "
            self.update()

        if not self.Telefone_Func.value:
            self.Telefone_Func.error_text = "Campo Obrigatorio "
            self.update()

        else:
            nomefunc = self.Nome_Func.value
            matriculaFunc=self.Matricula_Func.value
            cpf = self.cpf.value
            telefoneFunc = self.Telefone_Func.value
            codef = self.criar_qr(matriculaFunc)

            if cadastroFunc.cadastrar_Func(nomefunc, matriculaFunc, cpf, telefoneFunc, codef):
                self.page.controls.append(
                    Text("Cadastro realizado com sucesso", color="#591C21")
                )
                self.page.update()
                print("Deu certo ")
                self.page.controls.pop()
                self.page.update()
            else:
                print("Deu certo não")
                self.page.controls.append(Text("Error Tente novamente", color="#591C21"))
                self.page.update()
                self.page.controls.pop()
                self.page.update()

    def cadastro_Usuarios(self,e):
        if not self.nome.value:
            self.nome.error_text = "Campo Obrigatorio "
            self.update()
        if not self.matricula.value:
            self.matricula.error_text = "Campo Obrigatorio "
            self.update()
        if not self.turma.value:
            self.turma.error_text = "Campo Obrigatorio "
            self.update()
        if not self.Turno.value:
            self.Turno.error_text = "Campo Obrigatorio "
            self.update()
        if not self.curso.value:
            self.curso.error_text = "Campo Obrigatorio "
            self.update()
        if not self.nomeResp.value:
            self.nomeResp.error_text = "Campo Obrigatorio "
            self.update()
        if not self.email.value:
            self.email.error_text = "Campo Obrigatorio "
            self.update()
        if not self.Telefone.value:
            self.Telefone.error_text = "Campo Obrigatorio "
            self.update()
        else:
            self.setarData()
            nome= self.nome.value
            matricula=self.matricula.value
            datanasc= self.datanasc
            turma=self.turma.value
            turno=self.Turno.value
            curso=self.curso.value
            nomeresp=self.nomeResp.value
            email=self.email.value
            telefone=self.Telefone.value

            code = self.criar_qr(matricula)
            if cadastrouser.cadastrar_Aluno1(nome,matricula,datanasc,turma,turno,curso,nomeresp,email,telefone,code):
                self.page.controls.append(
                    Text("Cadastro realizado com sucesso", color="#591C21")
                )
                self.page.update()
                print("Deu certo ")
                self.page.controls.pop()
                self.page.update()

            else:
                print("Deu certo não")
                self.page.controls.append(Text("Error Tente novamente", color="#591C21"))
                self.page.update()
                self.page.controls.pop()
                self.page.update()

    def setarData(self):
        self.datanasc = f"{self.dia.value}/{self.mes.value}/{self.ano.value}"
        print(self.datanasc)



        self.page.update()

    def build(self):

        self.nome = TextField(  label="Nome",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.WHITE,
        )
        self.matricula = TextField(  label="Matricula",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        )

        self.turma = TextField(  label="Turma",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        ) 
        self.Turno = Dropdown(
            width=100,
            bgcolor=colors.BLACK,
            options=[
                dropdown.Option("Manhã"),
                dropdown.Option("Tarde"),
                dropdown.Option("Noite"),                                  
            ],
        )
        self.Turnotxt= Text("Turno",
                          color=colors.BLACK,text_align=TextAlign.CENTER)
      
      
        self.curso = TextField(  label="Curso",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        )
        self.nomeResp = TextField(  label="Nome do responsável",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        )
        self.email = TextField(  label="Email",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        )
        self.Telefone = TextField(  label="Telefone",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        )
        self.botao_Cad_aluno = ElevatedButton(
            "Cadastrar aluno",
            icon="arrow_circle_right",
            bgcolor=colors.BLACK,
            color=colors.WHITE,
            on_click=self.cadastro_Usuarios,
        )
        self.dia = Dropdown(
            width=100,
            bgcolor=colors.BLACK,
            
            options=[
                dropdown.Option("01"),
                dropdown.Option("02"),
                dropdown.Option("03"),
                dropdown.Option("04"),
                dropdown.Option("05"),
                dropdown.Option("06"),
                dropdown.Option("07"),
                dropdown.Option("08"),
                dropdown.Option("09"),
                dropdown.Option("10"),
                dropdown.Option("11"),
                dropdown.Option("12"),
                dropdown.Option("13"),
                dropdown.Option("14"),
                dropdown.Option("15"),
                dropdown.Option("16"),
                dropdown.Option("17"),
                dropdown.Option("18"),
                dropdown.Option("19"),
                dropdown.Option("20"),
                dropdown.Option("21"),
                dropdown.Option("22"),
                dropdown.Option("23"),
                dropdown.Option("24"),
                dropdown.Option("25"),
                dropdown.Option("26"),
                dropdown.Option("27"),
                dropdown.Option("28"),
                dropdown.Option("29"),
                dropdown.Option("30"),
                dropdown.Option("31"),                                                          
            ],
        )
        self.mes = Dropdown(
            width=100,
            bgcolor=colors.BLACK,

            options=[
                dropdown.Option("01"),
                dropdown.Option("02"),
                dropdown.Option("03"),
                dropdown.Option("04"),
                dropdown.Option("05"),
                dropdown.Option("06"),
                dropdown.Option("07"),
                dropdown.Option("08"),
                dropdown.Option("09"),
                dropdown.Option("10"),
                dropdown.Option("11"),
                dropdown.Option("12"),                                                      
            ],
        )
        self.ano = Dropdown(
            width=100,
            bgcolor=colors.BLACK,

            options=[
            dropdown.Option("2023"),
            dropdown.Option("2022"),
            dropdown.Option("2021"),
            dropdown.Option("2020"),
            dropdown.Option("2019"),
            dropdown.Option("2018"),
            dropdown.Option("2017"),
            dropdown.Option("2016"),
            dropdown.Option("2015"),
            dropdown.Option("2014"),
            dropdown.Option("2013"),
            dropdown.Option("2012"),
            dropdown.Option("2011"),
            dropdown.Option("2010"),
            dropdown.Option("2009"),
            dropdown.Option("2008"),
            dropdown.Option("2007"),
            dropdown.Option("2006"),
            dropdown.Option("2005"),
            dropdown.Option("2004"),
            dropdown.Option("2003"),
            dropdown.Option("2002"),
            dropdown.Option("2001"),
            dropdown.Option("2000"),
            dropdown.Option("1999"),
            dropdown.Option("1998"),
            dropdown.Option("1997"),
            dropdown.Option("1996"),
            dropdown.Option("1995"),
            dropdown.Option("1994"),
            dropdown.Option("1993"),
            dropdown.Option("1992"),
            dropdown.Option("1991"),
            dropdown.Option("1990"),
            dropdown.Option("1989"),
            dropdown.Option("1988"),
            dropdown.Option("1987"),
            dropdown.Option("1986"),
            dropdown.Option("1985"),
            dropdown.Option("1984"),
            dropdown.Option("1983"),
            dropdown.Option("1982"),
            dropdown.Option("1981"),
            dropdown.Option("1980"),
            dropdown.Option("1979"),
            dropdown.Option("1978"),
            dropdown.Option("1977"),
            dropdown.Option("1976"),
            dropdown.Option("1975"),
            dropdown.Option("1974"),
            dropdown.Option("1973")



            ],
        )        
        self.diatxt= Text("Dia",
                          color=colors.BLACK, text_align=TextAlign.CENTER)
        self.mestxt= Text("Mês",
                          color=colors.BLACK,text_align=TextAlign.CENTER)
        self.anotxt= Text("Ano",
                          color=colors.BLACK,text_align=TextAlign.CENTER)
      
      
        #Dados Funcionarios
        self.Nome_Func = TextField(  label="Nome",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        )
        self.Matricula_Func = TextField(  label="matricula",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        )
        self.Telefone_Func = TextField(  label="Telefone",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        )
        self.cpf = TextField(  label="cpf",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.GREY_100,
        )
        self.botao_Cad_Func = ElevatedButton(
            "Cadastrar",
            icon="arrow_circle_right",
            bgcolor=colors.BLACK,
            color=colors.WHITE,
            on_click=self.cadastrarFunc,
            
        )
        #Dados visitas
        self.nomeVisit = TextField(  label="Nome",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.WHITE,
        )
        self.cpfVisit = TextField(  label="Cpf",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.WHITE,
        )
        self.contatoVisit = TextField(  label="Contato",
            cursor_color=colors.BLACK,
            border_color=colors.BLACK,
            height=75,
            width=500,
            text_align=TextAlign.CENTER,
            color=colors.BLACK,
            bgcolor=colors.WHITE,
        )
        self.botao_Cad_Visita = ElevatedButton(
            "Cadastrar Visitas",
            icon="arrow_circle_right",
            bgcolor=colors.BLACK,
            color=colors.WHITE,
            on_click=self.cadastrarVisit,
            
        )



        self.tabsCad = Tabs( 
            
            indicator_color=colors.BLACK,
            label_color=colors.BLACK,
            selected_index=1,
            animation_duration=600,
            tabs=[
                Tab(
                    text="Cadastro Aluno",
                    content=Container(
                        Container(
                        content=Column(
                            [
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.nome,
                                        height=50,
                                        width=500,
                                    ),
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.matricula,
                                        height=50,
                                        width=500,
                                    ),


                        Container(
                                        alignment=alignment.top_left,
                                        content=self.turma,
                                        height=50,
                                        width=500,
                                    ),

                        Container(
                                        alignment=alignment.top_left,
                                        content=self.curso,
                                        height=50,
                                        width=500,
                                    ),
                        Container(
                                        alignment=alignment.top_center,
                                        content=self.Turnotxt,
                                        width=100,
                                    ),
                        Container(
                                        bgcolor=colors.BLACK,
                                        alignment=alignment.top_left,
                                        content=self.Turno,
                                        width=100,
                                    ),                
                        Container(
                                        alignment=alignment.top_left,
                                        content=
                                            Row([
                                                Container(
                                                    content=self.diatxt,
                                                    width=100,
                                                    height=20,
                                                ),
                                                Container(
                                                    content=self.mestxt,
                                                    width=100,
                                                    height=20,
                                                ),
                                                Container(
                                                    content=self.anotxt,
                                                    width=100,
                                                    height=20,
                                                ),
                                            ]),
                                        height=20,
                                        width=500,
                        ),
                        Container(
                                        alignment=alignment.top_left,
                                        
                                        content=Row([
                                            self.dia,
                                            self.mes,
                                            self.ano,
                                            ]),
                                        width=350,
                                        bgcolor=colors.BLACK
                                    ),
                        self.botao_Cad_aluno,
                        
                        ],

                        )
                        )   
                    ),
                ),
                Tab(
                    text="Cadastro Funcionario",
                    content=Container(
                        Container(
                        content=Column(
                            [
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.Nome_Func,
                                        height=50,
                                        width=500,
                                    ),
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.Matricula_Func,
                                        height=50,
                                        width=500,
                                    ),
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.Telefone_Func,
                                        height=50,
                                        width=500,
                                    ),
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.cpf,
                                        height=50,
                                        width=500,
                                    ),
                        self.botao_Cad_Func
                        
                        
                        ],
                        ),),)
                ),
            Tab(
                text="Cadastrar Visitas",
                content=Container(
                    Container(
                        content=Column([
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.nomeVisit,
                                        height=50,
                                        width=500,
                                    ),
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.cpfVisit,
                                        height=50,
                                        width=500,
                                    ),
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.contatoVisit,
                                        height=50,
                                        width=500,
                                    ),
                        Container(
                                        alignment=alignment.top_left,
                                        content=self.botao_Cad_Visita,
                                        height=50,
                                        width=500,
                                    ),


                    ]))
                )

            )
            ],
            expand=1,
        )


        return Container( 
                
            content=Column(
                alignment=alignment.top_center
                [  
                self.tabsCad    
            ]),
        )

