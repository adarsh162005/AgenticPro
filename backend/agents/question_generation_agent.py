from backend.skills.question_generation.skill import generate_question


class QuestionGenerationAgent:
    def run(self, topic: str, difficulty: str = "beginner") -> dict[str, str]:
        return generate_question(topic, difficulty)
