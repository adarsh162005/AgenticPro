from fastapi import APIRouter
from backend.models.submission import Submission

router = APIRouter()


@router.post("", response_model=Submission, status_code=201)
def create_submission(submission: Submission) -> Submission:
    return submission
