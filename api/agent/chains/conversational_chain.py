from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

from agent.prompt.system_prompt import POETRY_PROMPT

from dotenv import load_dotenv

from typing import Dict
from pydantic import BaseModel

from app.domain.poetry import PoetryOutput

import os

load_dotenv(dotenv_path=".env-production")


class PoetryLlm:
    GOOGLE_API_KEY = str(os.getenv("GOOGLE_API_KEY"))
    
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=1.0,
            api_key=self.GOOGLE_API_KEY
        )

        self.poetry_chain = self.llm.with_structured_output(PoetryOutput)
    
    def generate_poetry(self, mensagem: str) -> Dict:
        output = self.poetry_chain.invoke([
            SystemMessage(content=POETRY_PROMPT),
            HumanMessage(content=mensagem)
        ])
        
        if isinstance(output, BaseModel):
            return output.model_dump()

        return output