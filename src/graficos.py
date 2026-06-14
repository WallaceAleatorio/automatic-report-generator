import os
import matplotlib.pyplot as plt


def gerar_graficos(df):

    os.makedirs("charts", exist_ok=True)

    colunas_numericas = df.select_dtypes(include="number").columns

    primeira_coluna = df.columns[0]

    for coluna in colunas_numericas:

        plt.figure(figsize=(10, 5))

        plt.bar(df[primeira_coluna], df[coluna])

        plt.title(f"{coluna}")

        plt.xticks(rotation=45)

        plt.tight_layout()

        arquivo = f"charts/{coluna}.png"

        plt.savefig(arquivo)

        plt.close()

        print(f"Gráfico criado: {arquivo}")