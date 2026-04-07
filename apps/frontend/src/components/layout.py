import flet as ft

MAX_WIDTH = 1040

def wrap_page(content: ft.Control) -> ft.Control:
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(content=content, width=MAX_WIDTH, expand=False),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
            expand=True,
        ),
        bgcolor="#FFFFFF",
        padding=ft.Padding.only(top=20, right=16, bottom=20, left=16),
        expand=True,
    )