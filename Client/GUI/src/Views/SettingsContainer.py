import flet as ft

class SettingsContainer:
    def __init__(self):
        self.column = ft.Column(
            controls=[
                ft.Text("Settings Container"),
            ],
        )
    def build(self):
        return self.column