import flet as ft

from Dependencies.Constants import crypt_drive_blue_semilight, crypt_drive_purple, crypt_drive_blue


class FilesContainer:
    def __init__(self):
        self.title = ft.Text(value="Your Files", font_family="Aeonik Black", size=90, color=crypt_drive_blue)
        self.loading = ft.Container(
            content=
                ft.Row(
                    controls=[
                    ft.ProgressRing(color=crypt_drive_blue, aspect_ratio=1, stroke_width=8, stroke_cap=ft.StrokeCap.ROUND),
                    ],
                    height=60,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            expand=False,
            alignment=ft.Alignment(0,0),
            height=600,
        )
        self.fab = ft.FloatingActionButton(
            bgcolor=crypt_drive_blue_semilight,
            icon=ft.Icons.FILE_UPLOAD_OUTLINED,
            tooltip="Upload File",
            shape=ft.RoundedRectangleBorder(radius=10),
            width=90,
            height=90
        )
        self.column = ft.Column(
            controls=[],
        )
        self.current_directory: FolderTile = None
        self.directories: list[FolderTile] = []
        self.files: list[FileTile] = []

    def build(self):
        return self.column


class FileTile:
    def __init__(self, file_name, file_size):
        self.name = file_name
        self.size = file_size

        self.tile = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.INSERT_DRIVE_FILE),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls =[
                                    ft.Text(self.name, font_family="Aeonik Bold", size=20),
                                ft.Text(f"Size: {self.size} bytes", font_family="Aeonik", size=16)
                                ]
                            )
                        ], expand = True
                    ),
                    ft.IconButton(
                        ft.Icons.EDIT_DOCUMENT,
                        on_click=lambda _: None,
                        tooltip="Rename File"
                    ),
                    ft.IconButton(
                        ft.Icons.FILE_DOWNLOAD_OUTLINED,
                        on_click=lambda _: None,
                        tooltip="Download File"
                    ),
                    ft.IconButton(
                        ft.Icons.DELETE,
                        on_click=lambda _: None,
                        tooltip="Delete File"
                    )
                ]
            ), border_radius=10, bgcolor=crypt_drive_blue_semilight, padding=ft.padding.only(left=10, right=10, top=10, bottom=10)
        )



class FolderTile:
    def __init__(self, path, item_count, is_current_directory=False, root=False):
        self.name = path.split("/")[-1]
        if self.name == "": self.path = "/"
        else: self.path = path[:-len(self.name)]
        self.items = item_count
        self.parent_icon = ft.Icons.DRIVE_FOLDER_UPLOAD_ROUNDED
        self.tooltip = "Click to return to Parent Folder"

        if root:
            self.parent_icon = ft.Icons.HOME_ROUNDED
            self.tooltip = "Already at root folder"

        if is_current_directory:
            self.tile = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(self.parent_icon, color=crypt_drive_purple),
                        ft.Text(self.path, font_family="Aeonik Bold", size=20),
                        ft.Text(self.name, font_family="Aeonik Black", size=20)
                    ],
                ),
                tooltip=self.tooltip, border_radius=10, bgcolor=crypt_drive_blue_semilight, padding=ft.padding.only(left=10, right=10, top=10, bottom=10)
            )
        else:
            self.tile = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.FOLDER),
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls =[
                                        ft.Text(self.name, font_family="Aeonik Bold", size=20),
                                        ft.Text(f"{self.get_items_string(self.items)}", font_family="Aeonik", size=16)
                                    ]
                                )
                            ], expand = True
                        ),
                        ft.IconButton(
                            ft.Icons.EDIT,
                            on_click=lambda _: None,
                            tooltip="Rename Folder"
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE,
                            on_click=lambda _: None,
                            tooltip="Delete Folder"
                        )
                    ]
                ),
                border_radius=10,
                bgcolor=crypt_drive_blue_semilight,
                padding=ft.padding.all(10),
                tooltip="Click to open folder"
            )


    def get_items_string(self, item_count: int):
        if item_count == 1:
            return "1 item"
        else:
            return f"{item_count} items"



def test(page: ft.Page):
    flc = FilesContainer()
    page.add(
        flc.build()
    )
    flc.column.controls.append(FileTile("test.txt", "12345").tile)
    flc.column.width = 900
    page.update()


if __name__ == "__main__":
    ft.app(test)