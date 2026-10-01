import json
from pathlib import Path
from typing import Any


class LongTermMemory:
    def __init__(self, path: Path = Path("./database/memory.jsonl")) -> None:
        self.path = path

    def add(self, item: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(item, ensure_ascii=True) + "\n")

    def all(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        with self.path.open(encoding="utf-8") as stream:
            return [json.loads(line) for line in stream if line.strip()]
