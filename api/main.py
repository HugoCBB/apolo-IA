from fastapi import FastAPI
from app.infra.routes.poetry_routes import router as poetry_router


app = FastAPI(
    title="ApoloIA - Gerador de Poesias",
    description="Uma API para gerar poesias criativas com IA.",
    version="1.0.0"
)

app.include_router(poetry_router, prefix="/api/v1", tags=["Poesia"])

@app.get("/ping")
async def root():
    return {"message":"pong"}