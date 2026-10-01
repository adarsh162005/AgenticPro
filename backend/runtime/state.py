from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowState:
    submission_id: str
    status: str = "queued"
    outputs: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
