from fastapi import APIRouter
from backend.models.evaluation import Evaluation

router = APIRouter()


@router.get("/{submission_id}", response_model=Evaluation)
def get_evaluation(submission_id: str) -> Evaluation:
    return Evaluation(submission_id=submission_id, status="queued")
