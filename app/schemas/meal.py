from pydantic import BaseModel

class Refeicao(BaseModel):
    ingredientes: list[str]
    calorias: float
    proteinas: float
    gorduras:float
    carboidratos: float
