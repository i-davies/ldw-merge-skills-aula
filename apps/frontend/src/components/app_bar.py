import flet as ft

def build_app_bar(
    title: str,
    subtitle: str | None = None,
    show_back: bool = False,
    on_back = None,
) -> ft.Control:
    left_controls: list[ft.Control] = []

    if show_back and on_back is not None:
        left_controls.append(
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="#111111",
                on_click=on_back,
            )
        )

    text_column = [
        ft.Text(title, size=20, weight=ft.FontWeight.W_700, color="#111111"),
    ]

    if subtitle:
        text_column.append(ft.Text(subtitle, size=12, color="#71717A"))

    left_controls.append(ft.Column(controls=text_column, spacing=2, expand=True))

    return ft.Container(
        content=ft.Row(
            controls=left_controls,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.Padding.symmetric(horizontal=8, vertical=8),
    )

