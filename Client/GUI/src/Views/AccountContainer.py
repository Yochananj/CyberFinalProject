import flet as ft

class AccountContainer:
    def __init__(self):
        self.column = ft.Column(
            controls=[
                ft.Text("Account Container"),
            ],
        )
    def build(self):
        return self.column