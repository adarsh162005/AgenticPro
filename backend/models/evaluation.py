from pydantic import BaseModel, Field


class Evaluation(BaseModel):
    submission_id: str
    passed: int = 0
    total: int = 0
    score: float = Field(default=0, ge=0)
    feedback: str = ""
    status: str = "queued"
