import flet as ft

def _is_hovered(data) -> bool:
    if isinstance(data, bool):
        return data
    return str(data).lower() == "true"


def _set_option_hover_state(
    option_tile: ft.Container, 
    selected_option: int | None,
    is_hovered: bool
) -> None:
    option_index = option_tile.data
    if selected_option == option_index:
        return
    
    option_tile.bgcolor = "#F9FAFB" if is_hovered else "#FFFFFF"
    option_tile.border = ft.Border.all(1, "#D4D4D8" if is_hovered else "#E4E4E7")
    option_tile.update()

def _set_list_card_hover_state(card: ft.Container, is_hovered: bool) -> None:
    card.bgcolor = "#FAFAFA" if is_hovered else "#FFFFFF"
    card.border = ft.Border.all(1, "#D4D4D8" if is_hovered else "#E4E4E7")
    card.update()


def build_course_card(course: dict, on_click) -> ft.Control:
    card = ft.Container(
        bgcolor="#FFFFFF",
        border=ft.Border.all(1, "#E4E4E7"),
        border_radius=10,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        content=ft.ListTile(
            title=ft.Text(course["title"], size=16, weight=ft.FontWeight.W_600, color="#111111"),
            subtitle=ft.Text(course.get("description") or "Sem descrição.", size=12, color="#71717A"),
            trailing=ft.Text(f"{course.get('total_lessons', 0)} aulas", size=12, color="#71717A"),
            content_padding=ft.Padding.symmetric(horizontal=14, vertical=14),
            hover_color=ft.Colors.TRANSPARENT,
            splash_color=ft.Colors.TRANSPARENT,
            mouse_cursor=ft.MouseCursor.CLICK,
            data=course,
            on_click=lambda e: on_click(e.control.data),
        )

    )

    card.on_hover = lambda e, c=card: _set_list_card_hover_state(c, _is_hovered(e.data))
    return card