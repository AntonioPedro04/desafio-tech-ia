from fastapi import FastAPI, HTTPException
from app.models.ml_model import previsao
from app.utils.response import responseConstructor
from app.schemas.meal import Refeicao
from app.utils.preprocessing import padronizaRefeicao
from app.utils.verificacoesErrors import temIngredienteLista, haValorNegativo
import pandas as pd

app = FastAPI()


@app.put("/predict")
def read_root(refeicao: Refeicao):
    
    # Verifica se há algum ingrediente que não está na lista de ingredientes disponíveis
    if not temIngredienteLista(refeicao.ingredientes):
        raise HTTPException(status_code=404, detail="Há pelo menos um ingrediente não disponível")
    
    if haValorNegativo(refeicao.calorias, refeicao.proteinas,refeicao.gorduras, refeicao.carboidratos):
        raise HTTPException(status_code=404, detail="Valores negativos não permitidos")
    
       
    refeicaoPadronizada = padronizaRefeicao(refeicao)
    classificacao = previsao(refeicaoPadronizada)
    response = responseConstructor(classificacao)
    
    return response

