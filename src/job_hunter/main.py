"""Application entry point for AI Job Hunter."""

from fastapi import FastAPI

app = FastAPI(
    title="AI Job Hunter",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return application health status."""
    return {"status": "ok"}
