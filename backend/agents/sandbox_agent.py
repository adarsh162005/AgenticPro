from backend.tools.code_execution_tool import execute_code


class SandboxAgent:
    def run(self, source_code: str, language: str, stdin: str = "") -> dict[str, object]:
        return execute_code(source_code, language, stdin)
