from typing import Any
from backend.database.connection import get_connection


def execute_query(sql: str, parameters: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    with get_connection() as connection:
        cursor = connection.execute(sql, parameters)
        if cursor.description is None:
            return []
        return [dict(row) for row in cursor.fetchall()]
