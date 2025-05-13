import joblib
import os
import pandas as pd

# Pega o path da pasta atual
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Determina o path em que o modelo está
MODEL_PATH = os.path.join(CURRENT_DIR, 'modeloTreinado.pkl')

model = joblib.load(MODEL_PATH)


def previsao(refeicaoPadronizada):

  dfRefeicao = pd.DataFrame.from_dict([refeicaoPadronizada])

  classificacao = model.predict(dfRefeicao)

  return classificacao[0]