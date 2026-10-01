from sandbox.runner import run_code


def execute_code(source_code: str, language: str, stdin: str = "", timeout_seconds: int = 5) -> dict[str, object]:
    return run_code(source_code, language, stdin=stdin, timeout_seconds=timeout_seconds)
