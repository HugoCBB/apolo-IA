from fastapi import APIRouter

from agent.chains.conversational_chain import PoetryLlm

from app.domain.poetry import PoetryRequest, PoetryOutput

router = APIRouter()
poetry_agent = PoetryLlm()

@router.post("/poetry/generate", response_model=PoetryOutput)
async def create_poetry(request: PoetryRequest):
    poetry_data = poetry_agent.generate_poetry(request.message)

    return poetry_data


    