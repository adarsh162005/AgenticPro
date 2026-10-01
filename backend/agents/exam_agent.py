from backend.models.exam import Exam


class ExamAgent:
    def validate(self, exam: Exam) -> Exam:
        if not exam.title.strip():
            raise ValueError("Exam title cannot be empty")
        return exam
