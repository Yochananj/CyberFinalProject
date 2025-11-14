import flet as ft

class SettingsContainer:
    def __init__(self):
        self.title = ft.Text("Your Settings")


        self.column = ft.Column(
            controls=[
                self.title,
            ],
        )
    def build(self):
        return self.column