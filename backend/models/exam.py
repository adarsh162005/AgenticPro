from datetime import datetime
from pydantic import BaseModel, Field


class Exam(BaseModel):
    id: str
    title: str
    starts_at: datetime | None = None
    duration_minutes: int = Field(gt=0)
    question_ids: list[str] = []
