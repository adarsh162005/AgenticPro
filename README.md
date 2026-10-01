# Programming Lab Auto Evaluation

A starter workspace for managing programming exams, running submissions in language-specific Docker containers, evaluating test cases, and publishing results.

## Project layout

- `backend/`: FastAPI API, evaluation agents, tools, skills, memory, MCP endpoints, and SQLite persistence.
- `sandbox/`: Docker-based runners for Python, C++, and Java submissions.
- `frontend/`: React/Vite student and faculty workspace.
- `tests/`: unit and integration test areas.
- `docs/`: architecture, lab component notes, and API reference.

## Local development

Backend (Python 3.10+):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
uvicorn backend.main:app --reload
```

Frontend (Node.js 20+):

```powershell
cd frontend
npm install
npm run dev
```

The API is available at `http://localhost:8000`; the frontend is at `http://localhost:5173`.

## Docker

Build the runner images and start the application:

```powershell
docker compose --profile sandbox up --build
```

The sandbox runner requires Docker to be installed and available to the backend process. Submitted code is run with networking disabled, read-only root filesystems, resource limits, and dropped Linux capabilities. Container isolation should still be reviewed for the deployment environment before accepting untrusted code.

## Configuration

Local settings may be provided in `.env`. Never put real credentials in a committed environment file. The default database is SQLite at `./database/evaluations.db`.

The API and UI currently contain demonstration data and starter routes; production authentication, persistent question/exam APIs, and instructor workflows remain to be implemented.
