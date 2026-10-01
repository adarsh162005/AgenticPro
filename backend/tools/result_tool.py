from backend.models.result import Result


_results: dict[tuple[str, str], Result] = {}


def get_result(exam_id: str, student_id: str) -> Result | None:
    return _results.get((exam_id, student_id))


def publish_result(result: Result) -> Result:
    published = result.model_copy(update={"published": True})
    _results[(result.exam_id, result.student_id)] = published
    return published
