from fastapi import FastAPI
from models.ml_model import previsao
from utils.response import responseConstructor
from schemas.meal import Refeicao
from schemas.mealOutput import RefeicaoOutput
from utils.preprocessing import padronizaRefeicao
import pandas as pd

app = FastAPI()


@app.put("/predict")
def read_root(refeicao: Refeicao):
    
    refeicaoPadronizada = padronizaRefeicao(refeicao)
    classificacao = previsao(refeicaoPadronizada)

    print(classificacao)
    response = responseConstructor(classificacao)
    
    return response

