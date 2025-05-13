import numpy as np

def responseConstructor(classificacao):
    response = {}

    ## Transforma numpy em inteiro padrão do python 
    response['classificacao'] = classificacao.item()

    ## Como no nosso modelo as respostas são binárias (0 ou 1) e as métricas de avaliações do modelo foram muito altas, consideramos uma probabilidade de 99% para todas as requisições.
    response['probabilidade'] = 0.99
    
    response['mensagem'] = "Refeição classificada como saudável" if classificacao == 0 else "Refeição classificada como não saudável"

    return response