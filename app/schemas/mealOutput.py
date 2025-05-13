from pydantic import BaseModel

class RefeicaoOutput(BaseModel):
    classificacao: int
    probabilidade: float
    mensagem: str