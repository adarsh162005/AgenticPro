from fastapi import APIRouter
from backend.models.question import Question

router = APIRouter()


@router.get("/{question_id}", response_model=Question)
def get_question(question_id: str) -> Question:
    return Question(id=question_id, title="Add two numbers", prompt="Read two integers and print their sum.")
