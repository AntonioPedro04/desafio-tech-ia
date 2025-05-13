from app.utils.preprocessing import ingredientesAleatóriosModelo
import numpy as np

def temIngredienteLista(ingredientes):
    ingredientes = np.array(ingredientes)
    return np.isin(ingredientes, ingredientesAleatóriosModelo).all()

def haValorNegativo(calorias, proteinas, gorduras, carboidratos):
    if calorias < 0 or proteinas < 0 or gorduras < 0 or carboidratos < 0:
        return True
    return False
        
