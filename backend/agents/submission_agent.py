from backend.models.submission import Submission


class SubmissionAgent:
    def validate(self, submission: Submission) -> Submission:
        if not submission.source_code.strip():
            raise ValueError("Submission source code cannot be empty")
        if submission.language not in {"python", "cpp", "java"}:
            raise ValueError("Unsupported submission language")
        return submission
