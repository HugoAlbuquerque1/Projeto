from flet import *


class Tela1(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):

        
        return Container(
            expand=True,
            
            content=Column([
                ElevatedButton("Tela1",bgcolor=colors.WHITE),
            ]),
        )

