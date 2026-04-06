import flet as ft

def build_courses_view(courses, on_course_click):
    print("teste")
    list_items = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)

    for c in courses:
        list_items.controls.append(
            ft.Container(
                content=ft.ListTile(
                    title=ft.Text(c['title'], weight="bold"),
                    subtitle=ft.Text(c['description']),
                    on_click=lambda e, course=c: on_course_click(course)
                ),
                border=ft.border.all(1, ft.Colors.OUTLINE_VARIANT),
                border_radius=10
            )
        )

    return ft.Column([
        ft.Text("Catálogo de Cursos", size=25, weight="bold"),
        list_items
    ])