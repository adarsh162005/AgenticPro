from backend.models.evaluation import Evaluation


class ScoringAgent:
    def percentage(self, evaluation: Evaluation, max_score: float) -> float:
        if max_score <= 0:
            return 0.0
        return min(100.0, evaluation.score / max_score * 100)
