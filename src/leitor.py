import pandas as pd 
def carregar_dados(caminho):
    if caminho.endswith('.csv'):
        return pd.read_csv(caminho)
    elif caminho.endswith('.xlsx'):
        return pd.read_excel(caminho)
    else:
        raise Exception("Formato de arquivo não suportado. Use .csv ou .xlsx")