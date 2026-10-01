from fastapi import APIRouter
from backend.models.result import Result

router = APIRouter()


@router.get("/{exam_id}/{student_id}", response_model=Result)
def get_result(exam_id: str, student_id: str) -> Result:
    return Result(exam_id=exam_id, student_id=student_id, score=0, max_score=0)
