from backend.models.evaluation import Evaluation
from backend.models.submission import Submission
from backend.runtime.state import WorkflowState
from backend.tools.test_case_tool import get_test_cases
from backend.tools.code_execution_tool import execute_code
from backend.skills.code_evaluation.evaluator import evaluate_outputs


def evaluate_submission(submission: Submission) -> tuple[WorkflowState, Evaluation]:
    state = WorkflowState(submission_id=submission.id, status="running")
    cases = get_test_cases(submission.question_id)
    actual_outputs = []
    for case in cases:
        result = execute_code(submission.source_code, submission.language, case.stdin)
        actual_outputs.append(str(result.get("stdout", "")))
    evaluation = evaluate_outputs(submission.id, cases, actual_outputs)
    state.status = "completed"
    state.outputs["evaluation"] = evaluation.model_dump()
    return state, evaluation
