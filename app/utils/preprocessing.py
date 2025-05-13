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

## Ingredientes que foram escolhidos aleatoriamente no treinamento do modelo para que se realizem as combinações de cada refeição (Seção: Criação do Dataset do modelo no arquivo model_training.ipynb)
ingredientesAleatóriosModelo = [
    "Biscoito doce recheado com morango",
    "Brócolis cozido",
    "Caju suco concentrado envasado",
    "Camarão Rio Grande grande cozido",
    "Carne bovina fígado grelhado",
    "Cenoura cozida",
    "Chá preto infusão 5%",
    "Cocada branca",
    "Corvina grande assada",
    "Estrogonofe de carne",
    "Feijão tropeiro mineiro",
    "Frango filé à milanesa",
    "Hambúrguer bovino grelhado",
    "Leite de vaca integral pó",
    "Linhaça semente",
    "Macarrão molho bolognesa",
    "Mamão doce em calda drenado",
    "Merluza filé frito",
    "Milho verde enlatado drenado",
    "Peru congelado assado",
    "Porco pernil assado",
    "Pão de queijo assado",
    "Pé-de-moleque amendoim",
    "Sarapatel",
    "Soja queijo (tofu)"
]


## Nesse passo, a partir dos ingredientes do objeto refeicao e de seus valores de nutrientes, montamos um df que pode ser utilizada como argumento para a previsão do modelo (de acordo com o modelo que fizemos, em que cada ingrediente tem um valor 1 ou 0 associado para sinalizar presença na refeição, além das colunas de nutrientes)
def transformaRefeicaoModeloPadronizado(refeicao, ingredientesAleatóriosModelo = ingredientesAleatóriosModelo):
    dados = {}

    for ingrediente in ingredientesAleatóriosModelo:
        dados[ingrediente] = 1 if ingrediente in refeicao.ingredientes else 0

    dados["Calorias"] = refeicao.calorias
    dados["Proteinas"] = refeicao.proteinas
    dados["Gorduras"] = refeicao.gorduras
    dados["Carboidratos"] = refeicao.carboidratos

    df = pd.DataFrame.from_dict([dados])
    return dados


## Junta as funções definidas em cima em uma só, a fim de que se facilite leitura no arquivo de endpoints
def padronizaRefeicao(refeicao):
   refeicaoNumericoPadronizada = padronizaValoresNuméricos(refeicao)

   refeicaoIngredientePadronizada = transformaRefeicaoModeloPadronizado(refeicaoNumericoPadronizada) 

   return refeicaoIngredientePadronizada
   


