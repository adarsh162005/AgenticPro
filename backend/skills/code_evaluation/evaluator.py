from backend.models.evaluation import Evaluation


def evaluate_outputs(submission_id: str, test_cases: list, outputs: list[str]) -> Evaluation:
    if len(test_cases) != len(outputs):
        raise ValueError("Each test case must have exactly one output")
    passed = 0
    score = 0.0
    total_points = sum(case.points for case in test_cases)
    for case, output in zip(test_cases, outputs):
        if output.strip() == case.expected_stdout.strip():
            passed += 1
            score += case.points
    return Evaluation(
        submission_id=submission_id,
        passed=passed,
        total=len(test_cases),
        score=score,
        feedback=f"Passed {passed} of {len(test_cases)} test cases.",
        status="completed",
    )
