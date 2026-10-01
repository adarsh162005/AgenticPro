from backend.models.question import Question


_questions: dict[str, Question] = {}


def get_question(question_id: str) -> Question | None:
    return _questions.get(question_id)


def save_question(question: Question) -> Question:
    _questions[question.id] = question
    return question
