from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]


def read_project_file(relative_path: str) -> str:
    path = (WORKSPACE_ROOT / relative_path).resolve()
    if not path.is_relative_to(WORKSPACE_ROOT):
        raise ValueError("Path must stay inside the project workspace")
    return path.read_text(encoding="utf-8")
