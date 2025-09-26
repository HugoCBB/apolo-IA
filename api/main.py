from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.infra.routes.poetry_routes import router as poetry_router


app = FastAPI(
    title="ApoloIA - Gerador de Poesias",
    description="Uma API para gerar poesias criativas com IA.",
    version="1.0.0"
)

origins = "http://localhost:8080/"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(poetry_router, prefix="/api/v1", tags=["Poesia"])

@app.get("/ping")
async def root():
    return {"message":"pong"}