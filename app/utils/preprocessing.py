import numpy as np
import pandas as pd

def padronizaValoresNuméricos(refeicao):
  porcentagemProteína = 4/10
  porcentagemCarboidrato = 4/10
  porcentagemGordura = 2/10

  caloriasTotais = 500

  caloriasIdeaisProteina = porcentagemProteína * caloriasTotais
  caloriasIdeaisCarboidrato = porcentagemCarboidrato * caloriasTotais
  caloriasIdeaisGordura = porcentagemGordura * caloriasTotais

  caloriasGramaDeProteína = 4
  caloriasGramaDeGordura = 9
  caloriasGramaDeCarboidrato = 4

  refeicao.calorias = refeicao.calorias/caloriasTotais * 100

  refeicao.carboidratos = refeicao.carboidratos * caloriasGramaDeCarboidrato / caloriasIdeaisCarboidrato * 100

  refeicao.proteinas = refeicao.proteinas * caloriasGramaDeProteína / caloriasIdeaisProteina * 100

  refeicao.gorduras = refeicao.gorduras * caloriasGramaDeGordura / caloriasIdeaisGordura * 100

  return refeicao

## Ingredientes que foram escolhidos aleatoriamento no treinamento do modelo para que se realizem as combinações de cada refeição (Seção: Criação do Dataset do modelo no arquivo model_training.ipynb)
ingredientesAleatóriosModelo = np.array([
    "Mamão doce em calda drenado",
    "Leite de vaca integral pó",
    "Feijão tropeiro mineiro",
    "Sarapatel",
    "Hambúrguer bovino grelhado",
    "Peru congelado assado",
    "Corvina grande assada",
    "Caju suco concentrado envasado",
    "Pão de queijo assado",
    "Cocada branca",
    "Brócolis cozido",
    "Camarão Rio Grande grande cozido",
    "Carne bovina fígado grelhado",
    "Estrogonofe de carne",
    "Cenoura cozida",
    "Porco pernil assado",
    "Frango filé à milanesa",
    "Biscoito doce recheado com morango",
    "Linhaça semente",
    "Pé-de-moleque amendoim",
    "Macarrão molho bolognesa",
    "Soja queijo (tofu)",
    "Chá preto infusão 5%",
    "Merluza filé frito",
    "Milho verde enlatado drenado"
])


## Nesse passo, a partir dos ingredientes do objeto refeicao e de seus valores de nutrientes, montamos um df que pode ser utilizada como argumento para a previsão do modelo (de acordo com o modelo que fizemos, em que cada ingrediente tem um valor 1 ou 0 associado para sinalizar presença na refeição, além das colunas de nutrientes)
def transformaRefeicaoModeloPadronizado(refeicao, ingredientesAleatóriosModelo = ingredientesAleatóriosModelo):
    dados = {}

    for ingrediente in ingredientesAleatóriosModelo:
        dados[ingrediente] = 1 if ingrediente in refeicao.ingredientes else 0

    dados["calorias"] = refeicao.calorias
    dados["proteinas"] = refeicao.proteinas
    dados["gorduras"] = refeicao.gorduras
    dados["carboidratos"] = refeicao.carboidratos

    df = pd.DataFrame([dados])
    return dados


## Junta as funções definidas em cima em uma só, a fim de que se facilite leitura no arquivo de endpoints
def padronizaRefeicao(refeicao):
   refeicaoNumericoPadronizada = padronizaValoresNuméricos(refeicao)

   refeicaoIngredientePadronizada = transformaRefeicaoModeloPadronizado(refeicaoNumericoPadronizada) 

   return refeicaoIngredientePadronizada
   


