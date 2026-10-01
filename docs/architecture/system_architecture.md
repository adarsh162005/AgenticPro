# System Architecture

```mermaid
flowchart LR
  Student[Student / Faculty UI] -->|HTTP JSON| API[FastAPI API]
  API --> Runtime[Evaluation Orchestrator]
  Runtime --> Agents[Specialized Agents]
  Runtime --> Skills[Evaluation Skills]
  Runtime --> Sandbox[Docker Sandbox]
  Sandbox -->|stdout / stderr / exit code| Runtime
  API --> DB[(SQLite starter database)]
  Runtime --> Audit[Audit Logger]
  Agents --> Memory[Memory and Retrieval]
```

The frontend sends exam and submission requests to the API. Runtime services coordinate validation, sandbox execution, scoring, and result publication. Each language runner is isolated in a Docker image; the starter setup disables network access and applies resource limits.
