from backend.models.submission import Submission
from backend.runtime.audit_logger import log_event
from backend.runtime.workflow import evaluate_submission


def run_evaluation(submission: Submission):
    log_event("evaluation.started", submission_id=submission.id)
    state, evaluation = evaluate_submission(submission)
    log_event("evaluation.finished", submission_id=submission.id, status=state.status, score=evaluation.score)
    return evaluation
