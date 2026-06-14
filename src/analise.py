import pandas as pd


def identificar_colunas(df):

    info = {}

    for coluna in df.columns:
        info[coluna] = str(df[coluna].dtype)

    return info


def analisar_dados(df):

    resultado = {
        "linhas": len(df),
        "colunas": len(df.columns),
        "estatisticas": {}
    }

    colunas_numericas = df.select_dtypes(include="number").columns

    for coluna in colunas_numericas:

        resultado["estatisticas"][coluna] = {
            "soma": df[coluna].sum(),
            "media": df[coluna].mean(),
            "maximo": df[coluna].max(),
            "minimo": df[coluna].min()
        }

    return resultado


def gerar_insights(resultado):

    insights = []

    insights.append(
        f"O dataset possui {resultado['linhas']} registros e {resultado['colunas']} colunas."
    )

    for coluna, dados in resultado["estatisticas"].items():

        variacao = dados["maximo"] - dados["minimo"]

        insights.append(
            f"A coluna '{coluna}' possui média de {dados['media']:.2f}."
        )

        insights.append(
            f"O maior valor encontrado foi {dados['maximo']:.2f} e o menor foi {dados['minimo']:.2f}."
        )

        insights.append(
            f"A variação observada foi de {variacao:.2f}."
        )

    return insights