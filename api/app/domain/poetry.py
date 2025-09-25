from pydantic import BaseModel, Field


class PoetryRequest(BaseModel):
    message: str = Field(description = "O tema ou filtro para a criacao da poesia")


class PoetryOutput(BaseModel):
    titulo: str = Field(description="Um título criativo para o poema.")
    estilo: str = Field(description="O estilo poético utilizado (ex: Verso Livre, Soneto, Haicai).")
    poema: str = Field(description="O texto completo do poema.")