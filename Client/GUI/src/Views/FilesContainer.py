import flet as ft

class FilesContainer:
    def __init__(self):
        self.column = ft.Column(
            controls=[
                ft.Text("Files Container"),
            ],
        )
    def build(self):
        return self.column