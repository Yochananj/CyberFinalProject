import os
import flet as ft

from Dependencies.Constants import crypt_drive_blue


class HomeView:
    def __init__(self, window_height):
        self.nav_rail = ft.NavigationRail(
            label_type=ft.NavigationRailLabelType.SELECTED,
            min_width=100,
            height= window_height,
            group_alignment=-1,
            selected_label_text_style=ft.TextStyle(font_family="Aeonik Bold", size=16, color=crypt_drive_blue),
            selected_index=0,

            leading = ft.Image(
                src=os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets/icon.png"),
                width=100,
                height=100,
                fit=ft.ImageFit.FIT_WIDTH),

            destinations=[
                ft.NavigationRailDestination(
                    label="Files",
                    selected_icon=ft.Icons.FOLDER,
                    icon=ft.Icons.FOLDER_OUTLINED
                ),
                ft.NavigationRailDestination(
                    label="Account",
                    selected_icon=ft.Icons.ACCOUNT_CIRCLE,
                    icon=ft.Icons.ACCOUNT_CIRCLE_OUTLINED
                ),
                ft.NavigationRailDestination(
                    label="Settings",
                    selected_icon=ft.Icons.SETTINGS,
                    icon=ft.Icons.SETTINGS_OUTLINED
                )
            ])

        self.body = ft.Container(
            content=ft.Text("Body!")
        )


    def build(self):
        return ft.View(route="/home",
           controls=[(ft.Row(
                controls=[
                    self.nav_rail,
                    ft.VerticalDivider(width=1, color=crypt_drive_blue),
                    self.body
                ],
                expand=True
            ))])


def test(page: ft.Page):
    page.views.append(
        HomeView(page).build()
    )
    page.update()

if __name__ == "__main__":
    ft.app(test)