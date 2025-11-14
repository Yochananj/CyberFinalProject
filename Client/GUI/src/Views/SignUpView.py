import os
import flet as ft


class SignUpView:
    def __init__(self, username_start_value: str = "", password_start_value: str = ""):
        self.logo = ft.Row(
            controls=[
                ft.Column(width=30, controls=[ft.Text("")]),
                ft.Image(
                    src=os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets/icon.png"),
                    width=200,
                    height=200,
                    fit=ft.ImageFit.FIT_WIDTH
                )]
        )
        self.username = ft.TextField(value=username_start_value, label="Username", width=300, autofocus=True, prefix_icon=ft.Icons.PERSON_ROUNDED)
        self.password = ft.TextField(value=password_start_value, label="Password", text_vertical_align=ft.VerticalAlignment.START, width=300, password=True, prefix_icon=ft.Icons.KEY_ROUNDED, can_reveal_password=True)
        self.password_confirmation = ft.TextField(label="Confirm Password", text_vertical_align=ft.VerticalAlignment.START, width=300, password=True, prefix_icon=ft.Icons.KEY_ROUNDED, can_reveal_password=True)
        self.log_in_button = ft.ElevatedButton(text="Sign Up", width=300, disabled=True)
        self.switch_to_log_in_button = ft.ElevatedButton(text="Log In Instead", width=300, disabled=False)
        self.taken_username_snack_bar = ft.SnackBar(
            duration=5000,
            content=ft.Row(
                controls=[ft.Icon(ft.Icons.CLOSE_ROUNDED, color=ft.Colors.RED),
                          ft.Text("Sign Up Failed: Username is already taken.", color=ft.Colors.RED)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            behavior=ft.SnackBarBehavior.FLOATING,
            bgcolor=ft.Colors.RED_100,
            shape=ft.ContinuousRectangleBorder(radius=10),
            margin=ft.margin.all(10)
        )

        self.passwords_must_match_snack_bar = ft.SnackBar(
            duration=5000,
            content=ft.Row(
                controls=[ft.Icon(ft.Icons.CLOSE_ROUNDED, color=ft.Colors.RED),
                          ft.Text("Password and Password Confirmation must be identical.", color=ft.Colors.RED)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            behavior=ft.SnackBarBehavior.FLOATING,
            bgcolor=ft.Colors.RED_100,
            shape=ft.ContinuousRectangleBorder(radius=10),
            margin=ft.margin.all(10)
        )

        self.username_length_snack_bar = ft.SnackBar(
            duration=5000,
            content=ft.Row(
                controls=[ft.Icon(ft.Icons.CLOSE_ROUNDED, color=ft.Colors.RED),
                          ft.Text("Username must be between 3 and 32 characters long.", color=ft.Colors.RED)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            behavior=ft.SnackBarBehavior.FLOATING,
            bgcolor=ft.Colors.RED_100,
            shape=ft.ContinuousRectangleBorder(radius=10),
            margin=ft.margin.all(10)
        )

        self.password_length_snack_bar = ft.SnackBar(
            duration=5000,
            content=ft.Row(
                controls=[ft.Icon(ft.Icons.CLOSE_ROUNDED, color=ft.Colors.RED),
                          ft.Text("Password must be between 8 and 64 characters long.", color=ft.Colors.RED)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            behavior=ft.SnackBarBehavior.FLOATING,
            bgcolor=ft.Colors.RED_100,
            shape=ft.ContinuousRectangleBorder(radius=10),
            margin=ft.margin.all(10)
        )


    def build(self):
        return ft.View(
            route = "/sign_up",
            controls=[ft.Row(
                controls=[
                    ft.Column([
                        self.logo,
                        self.username,
                        self.password,
                        self.password_confirmation,
                        self.log_in_button,
                        self.switch_to_log_in_button]
                    )],
                alignment=ft.MainAxisAlignment.CENTER)],
            can_pop=False,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )


