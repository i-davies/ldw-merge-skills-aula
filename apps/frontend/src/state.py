class AppState:
    def __init__(self) -> None:
        self.user_id = 1

        self.courses: list[dict] = []
        self.lessons: list[dict] = []

        self.current_course: dict | None = None
        self.current_lesson: dict | None = None

        # Estado das Perguntas
        self.current_question_ids: list[int] = []
        self.current_questions_map: dict[int, dict] = {}
        self.current_question_index = 0
        self.selected_option: int | None = None

    def reset_lesson_state(self) -> None:
        """Limpa o estado ao sair de uma lição."""
        self.current_lesson = None
        self.current_question_ids = []
        self.current_questions_map = {}
        self.current_question_index = 0
        self.selected_option = None

    def reset_course_state(self) -> None:
        """Limpa o estado ao voltar para a lista de cursos."""
        self.current_course = None
        self.lessons = []
        self.reset_lesson_state()

state = AppState()