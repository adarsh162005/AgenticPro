import subprocess
import tempfile
from pathlib import Path

from sandbox.resource_limits import (
    CPU_LIMIT,
    DEFAULT_TIMEOUT_SECONDS,
    MAX_TIMEOUT_SECONDS,
    MEMORY_LIMIT,
    PID_LIMIT,
)
from sandbox.security import validate_language


LANGUAGE_CONFIG = {
    "python": ("programming-lab-python", "main.py", ["python", "/workspace/main.py"]),
    "cpp": (
        "programming-lab-cpp",
        "main.cpp",
        ["sh", "-lc", "g++ -O2 -std=c++17 /workspace/main.cpp -o /tmp/program && /tmp/program"],
    ),
    "java": (
        "programming-lab-java",
        "Main.java",
        ["sh", "-lc", "javac -d /tmp /workspace/Main.java && java -cp /tmp Main"],
    ),
}


def run_code(source_code: str, language: str, stdin: str = "", timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS) -> dict[str, object]:
    normalized = validate_language(language)
    if not source_code.strip():
        raise ValueError("Source code cannot be empty")
    timeout = max(1, min(timeout_seconds, MAX_TIMEOUT_SECONDS))
    image, filename, command = LANGUAGE_CONFIG[normalized]
    with tempfile.TemporaryDirectory(prefix="lab-run-") as temp_dir:
        source_path = Path(temp_dir) / filename
        source_path.write_text(source_code, encoding="utf-8")
        docker_command = [
            "docker", "run", "--rm", "-i",
            "--network", "none",
            "--memory", MEMORY_LIMIT,
            "--cpus", CPU_LIMIT,
            "--pids-limit", str(PID_LIMIT),
            "--read-only",
            "--tmpfs", "/tmp:rw,nosuid,size=32m",
            "--cap-drop", "ALL",
            "--security-opt", "no-new-privileges",
            "--mount", f"type=bind,source={temp_dir},target=/workspace,readonly",
            image,
            *command,
        ]
        try:
            completed = subprocess.run(
                docker_command,
                input=stdin,
                text=True,
                capture_output=True,
                timeout=timeout,
                check=False,
            )
            return {
                "stdout": completed.stdout,
                "stderr": completed.stderr,
                "returncode": completed.returncode,
                "timed_out": False,
            }
        except subprocess.TimeoutExpired as error:
            return {
                "stdout": error.stdout or "",
                "stderr": error.stderr or "Execution timed out",
                "returncode": None,
                "timed_out": True,
            }
