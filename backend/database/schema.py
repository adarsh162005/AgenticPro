from backend.database.connection import get_connection


SCHEMA = """
CREATE TABLE IF NOT EXISTS submissions (
    id TEXT PRIMARY KEY,
    exam_id TEXT NOT NULL,
    question_id TEXT NOT NULL,
    student_id TEXT NOT NULL,
    language TEXT NOT NULL,
    source_code TEXT NOT NULL,
    submitted_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS evaluations (
    submission_id TEXT PRIMARY KEY,
    passed INTEGER NOT NULL DEFAULT 0,
    total INTEGER NOT NULL DEFAULT 0,
    score REAL NOT NULL DEFAULT 0,
    feedback TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'queued'
);
"""


def initialize_schema() -> None:
    with get_connection() as connection:
        connection.executescript(SCHEMA)
