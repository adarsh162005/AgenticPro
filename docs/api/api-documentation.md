# API Documentation

Base URL: `http://localhost:8000/api`

Interactive OpenAPI documentation is served at `/docs` while the backend is running.

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/exams/{exam_id}` | Retrieve a demo exam record |
| GET | `/questions/{question_id}` | Retrieve a demo question |
| POST | `/submissions` | Accept a submission payload |
| GET | `/evaluations/{submission_id}` | Retrieve a queued evaluation placeholder |
| GET | `/results/{exam_id}/{student_id}` | Retrieve a demo result |

Health check: `GET /health`.

These routes are scaffolding. Authentication, authorization, durable exam/question storage, and API-level input policy are not implemented yet.
