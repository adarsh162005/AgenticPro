from fastapi import APIRouter
from backend.models.exam import Exam

router = APIRouter()


@router.get("/{exam_id}", response_model=Exam)
def get_exam(exam_id: str) -> Exam:
    return Exam(id=exam_id, title="Sample programming lab", duration_minutes=60)
