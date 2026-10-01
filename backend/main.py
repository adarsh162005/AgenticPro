from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import evaluation_routes, exam_routes, question_routes, result_routes, submission_routes
from backend.config.settings import settings
from backend.database.schema import initialize_schema


app = FastAPI(title=settings.app_name, version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(exam_routes.router, prefix="/api/exams", tags=["exams"])
app.include_router(question_routes.router, prefix="/api/questions", tags=["questions"])
app.include_router(submission_routes.router, prefix="/api/submissions", tags=["submissions"])
app.include_router(evaluation_routes.router, prefix="/api/evaluations", tags=["evaluations"])
app.include_router(result_routes.router, prefix="/api/results", tags=["results"])


@app.on_event("startup")
def on_startup() -> None:
    initialize_schema()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
