from collections import deque
from typing import Any


class ShortTermMemory:
    def __init__(self, capacity: int = 100) -> None:
        self._items: deque[dict[str, Any]] = deque(maxlen=capacity)

    def add(self, item: dict[str, Any]) -> None:
        self._items.append(item)

    def recent(self, limit: int = 10) -> list[dict[str, Any]]:
        return list(self._items)[-limit:]
