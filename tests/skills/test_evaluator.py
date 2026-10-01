import unittest

from backend.models.test_case import TestCase
from backend.skills.code_evaluation.evaluator import evaluate_outputs


class EvaluatorTests(unittest.TestCase):
    def test_scores_matching_outputs_and_reports_failures(self) -> None:
        cases = [
            TestCase(id="1", question_id="q1", expected_stdout="5", points=2),
            TestCase(id="2", question_id="q1", expected_stdout="0", points=3),
        ]

        result = evaluate_outputs("submission-1", cases, ["5\n", "1\n"])

        self.assertEqual(result.passed, 1)
        self.assertEqual(result.total, 2)
        self.assertEqual(result.score, 2)
        self.assertEqual(result.status, "completed")


if __name__ == "__main__":
    unittest.main()