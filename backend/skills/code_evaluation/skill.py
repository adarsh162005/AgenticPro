from backend.skills.code_evaluation.evaluator import evaluate_outputs


class CodeEvaluationSkill:
    def evaluate(self, submission_id: str, test_cases: list, outputs: list[str]):
        return evaluate_outputs(submission_id, test_cases, outputs)
