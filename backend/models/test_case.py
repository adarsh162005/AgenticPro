from pydantic import BaseModel, Field


class TestCase(BaseModel):
    id: str
    question_id: str
    stdin: str = ""
    expected_stdout: str
    points: float = Field(default=1, ge=0)
    is_hidden: bool = True
