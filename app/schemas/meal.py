from pydantic import BaseModel

class Refeicao(BaseModel):
    ingredientes: list[str]
    calorias: int
    carboidratos: int
    proteínas: int
    gorduras:int 

class RefeicaoOutput(BaseModel):
    classificacao: int
    probabilidade: float
    mensagem: str