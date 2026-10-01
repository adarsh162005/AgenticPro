from pydantic import BaseModel, Field


class Result(BaseModel):
    student_id: str
    exam_id: str
    score: float = Field(ge=0)
    max_score: float = Field(ge=0)
    published: bool = False
