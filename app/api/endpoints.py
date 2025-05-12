from fastapi import FastAPI
from schemas.meal import Refeicao , RefeicaoOutput


app = FastAPI()


@app.put("/ola")
def read_root(refeicao: Refeicao):
    return refeicao
