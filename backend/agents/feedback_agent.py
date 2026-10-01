from backend.models.evaluation import Evaluation


class FeedbackAgent:
    def summarize(self, evaluation: Evaluation) -> str:
        if evaluation.total == 0:
            return "No test cases are configured for this question yet."
        return f"{evaluation.feedback} Score: {evaluation.score:g} points."
