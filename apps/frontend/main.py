import flet as ft
from src.api import get_courses, get_lessons, get_lesson_question_ids, get_question_details, submit_answer
from src.state import state
# Importaremos as views que criaremos no próximo passo
from src.views.courses import build_courses_view
# ...

def main(page: ft.Page):
    page.title = "MergeSkills - Aluno"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 450 # Tamanho de celular para teste
    page.window.height = 800

    def render(view_content: ft.Control):
        """Limpa a tela e desenha o novo conteúdo."""
        page.controls.clear()
        page.add(view_content)
        page.update()

    # --- Funções de Navegação ---

    def show_courses():
        state.reset_course_state()
        state.courses = get_courses()
        # Aqui chamaremos a view de cursos
        render(build_courses_view(state.courses, on_course_click=""))
        #render(ft.Text("Lista de Cursos (Construindo...)"))

    # Inicialização
    show_courses()

ft.run(main)