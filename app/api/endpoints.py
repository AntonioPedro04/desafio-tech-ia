from fastapi import FastAPI
from schemas.meal import Refeicao
from schemas.mealOutput import RefeicaoOutput
from utils.preprocessing import padronizaRefeicao

app = FastAPI()


@app.put("/ola")
def read_root(refeicao: Refeicao):
    
    refeicaoPadronizada = padronizaRefeicao(refeicao)

    return refeicaoPadronizada
