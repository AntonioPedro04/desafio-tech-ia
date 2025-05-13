# Desafio Técnico - Classificador de Refeições Saudáveis 🍽️🤖

Este desafio foi criado para avaliar suas habilidades em ciência de dados, machine learning e desenvolvimento de APIs.

## 🎯 Objetivo

Construir uma API que classifique refeições como **saudáveis** ou **não saudáveis** com base em dados nutricionais.

## 📋 Pré-requisitos

- Python 3.8+
- Docker
- Git
- Conhecimento em:
  - Machine Learning
  - APIs REST
  - Containerização
  - Versionamento de código

## 🧩 O que você deve fazer

1. Utilizar Python (preferencialmente com **FastAPI**) para criar uma API REST.
2. Treinar um modelo supervisionado (ex: RandomForest, MLP) com um dataset que contenha:
   - `ingredientes`
   - `calorias`
   - `carboidratos`
   - `proteínas`
   - `gorduras`
   - `classificação` (0 = não saudável, 1 = saudável)
3. Pré-processar os dados:
   - Limpeza e padronização de textos
   - Normalização ou padronização dos dados numéricos
4. Expor um endpoint `/predict` que receba os dados de uma refeição em JSON e retorne a classificação.
5. Encapsular tudo em um container Docker com instruções de uso.
6. Documentar no README como rodar o projeto localmente.

## 📁 Estrutura do Projeto

```
.
├── app/
│   ├── api/
│   │   └── endpoints.py
│   ├── models/
│   │   └── ml_model.py
│   ├── schemas/
│   │   └── meal.py
│   └── utils/
│       └── preprocessing.py
├── data/
│   └── raw/
├── notebooks/
│   └── model_training.ipynb
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

## 📊 Avaliação do Modelo

O modelo deve ser avaliado considerando as seguintes métricas:

- Acurácia (Accuracy)
- Precisão (Precision)
- Revocação (Recall)
- F1-score
- Matriz de Confusão

## 🔧 Considerações Técnicas

### Versões Recomendadas

- Python >= 3.8
- FastAPI >= 0.68.0
- scikit-learn >= 1.0.0
- pandas >= 1.3.0
- numpy >= 1.21.0

### Performance

- A API deve responder em menos de 1 segundo
- O modelo deve ser otimizado para inferência
- Considerar cache de predições frequentes

### Segurança

- Validação de inputs
- Rate limiting
- Logging de requisições
- Tratamento de erros

## 📝 Exemplos de Uso

### Exemplo de Request

```json
{
  "ingredientes": ["arroz", "feijão", "frango", "salada"],
  "calorias": 450,
  "carboidratos": 60,
  "proteinas": 30,
  "gorduras": 10
}
```

### Exemplo de Response

```json
{
  "classificacao": 1,
  "probabilidade": 0.85,
  "mensagem": "Refeição classificada como saudável"
}
```

## 🚀 Como entregar

1. Faça um **fork** deste repositório.
2. Realize o desafio no seu fork.
3. Ao finalizar, envie um **Pull Request** para este repositório com a sua solução.

## ✅ Critérios de Avaliação

- Estrutura e organização do código
- Clareza na documentação
- Qualidade do pipeline de dados e do modelo
- Funcionamento da API e da containerização
- Boas práticas de versionamento no Git

---

Boa sorte e divirta-se construindo! 🚀

## 📚 Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Docker Documentation](https://docs.docker.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs/python/tf)
- [Keras Documentation](https://keras.io/api/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/en/latest/)
- [LightGBM Documentation](https://lightgbm.readthedocs.io/en/latest/)
- [CatBoost Documentation](https://catboost.ai/en/docs/concepts/python-reference)
- [MLflow Documentation](https://www.mlflow.org/docs/latest/index.html)
- [Streamlit Documentation](https://docs.streamlit.io/library)
- [Plotly Documentation](https://plotly.com/python/)
- [Dash Documentation](https://dash.plotly.com/)
- [Flask-RESTful Documentation](https://flask-restful.readthedocs.io/en/latest/)
- [FastAPI Users Documentation](https://fastapi-users.github.io/fastapi-users/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Redis Documentation](https://redis.io/documentation)
- [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)
- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [Celery Documentation](https://docs.celeryproject.org/en/stable/)
- [Redis Queue Documentation](https://python-rq.org/)
- [APScheduler Documentation](https://apscheduler.readthedocs.io/en/stable/)
- [Airflow Documentation](https://airflow.apache.org/docs/)
- [Luigi Documentation](https://luigi.readthedocs.io/en/stable/)
- [Prefect Documentation](https://docs.prefect.io/)
- [Dask Documentation](https://docs.dask.org/en/latest/)
- [Ray Documentation](https://docs.ray.io/en/latest/)
- [Streamlit Sharing Documentation](https://docs.streamlit.io/streamlit-cloud/get-started)

## Como rodar o projeto? 🚀

É importante ressaltar que tais instruções estão de acordo com ambientes linux de desenvolvimento.

Caso o usuário esteja em um ambiente Windows, os mesmos efeitos podem ser tomados com a utilização do WSL.

Primeiramente, clone o repositório

```
git clone https://github.com/AntonioPedro04/desafio-tech-ia.git
```

Caso não possua o package manager pip instalado (necessário para baixar os pacotes do python) rode:

```
sudo apt install python3-pip
```

Após isso, vá para o diretório onde está o projeto

```
cd desafio-tech-ia
```

Em seguida, como o projeto está encapsulado em um container do docker, iremos buildar nosso projeto com:

```
sudo docker build -t projetofeatcode .
```

Espere alguns segundos, em seguida rode:

```
sudo docker run -p 8000:8000 projetofeatcode
```

Nessa fase, irá aparecer algo como "Uvicorn running on http://0.0.0.0:8000" no terminal. Sendo assim, acesse esse link usando CTRL+CLICK.
Isso o vai direcionar para o browser.

No browser, adicione "/docs" no link principal. Dessa forma, você conseguirá testar a API, podendo utilizar quaisquer valores no RequestBody da api.

## Pequenos testes

Valores interessante para um teste inicial seriam:

```
{
  "ingredientes": [
    "Feijão tropeiro mineiro", "Leite de vaca integral pó", "Mamão doce em calda drenado", "Sarapatel"
  ],
  "calorias": 968.0,
  "proteinas": 54.3,
  "gorduras": 38.3,
  "carboidratos": 113.9
}
```

O ResponseBody retornará:

```
{
  "classificacao": 0,
  "probabilidade": 0.99,
  "mensagem": "Refeição classificada como não saudável"
}
```

Além disso, podemos testar valores negativos, como:

```
{
  "ingredientes": [
    "Feijão tropeiro mineiro", "Leite de vaca integral pó", "Mamão doce em calda drenado", "Sarapatel"
  ],
  "calorias": -10.0,
  "proteinas": 54.3,
  "gorduras": 38.3,
  "carboidratos": 113.9
}
```

Isso retornará:

```
{
  "detail": "Valores negativos não permitidos"
}
```

Outro teste interessante pode ser realizado pelos seguintes dados:

```
{
  "ingredientes": [
    "Mamão doce em calda drenado", "Sarapatel", "Camarão Rio Grande grande cozido", "Feijão tropeiro mineiro"
  ],
  "calorias": 500,
  "proteinas": 40,
  "gorduras": 10,
  "carboidratos": 40
}
```

Retornará:

```
{
  "classificacao": 1,
  "probabilidade": 0.99,
  "mensagem": "Refeição classificada como saudável"
}
```

Se aumentarmos a quantidade de carboidratos para 100g, o seguinte resultado aparece:

```
{
  "classificacao": 0,
  "probabilidade": 0.99,
  "mensagem": "Refeição classificada como não saudável"
}
```

Caso utilizemos algum ingrediente que não está na nossa lista de treinamento do modelo, como:

```
{
"ingredientes": [
"-->Banana<--", "Sarapatel", "Camarão Rio Grande grande cozido", "Feijão tropeiro mineiro"
],
"calorias": 500,
"proteinas": 40,
"gorduras": 10,
"carboidratos": 100
}
```

Isso nos retornará:

```
{
  "detail": "Há pelo menos um ingrediente não disponível"
}

```
