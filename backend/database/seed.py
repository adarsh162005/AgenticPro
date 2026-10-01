from backend.database.connection import get_connection
from backend.database.schema import initialize_schema


def seed_demo_data() -> None:
    initialize_schema()
    with get_connection() as connection:
        connection.execute(
            "INSERT OR IGNORE INTO evaluations (submission_id, feedback, status) VALUES (?, ?, ?)",
            ("demo-submission", "Demo evaluation record", "queued"),
        )
