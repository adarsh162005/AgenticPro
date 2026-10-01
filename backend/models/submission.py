from datetime import datetime, timezone
from pydantic import BaseModel, Field


class Submission(BaseModel):
    id: str
    exam_id: str
    question_id: str
    student_id: str
    language: str
    source_code: str
    submitted_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
