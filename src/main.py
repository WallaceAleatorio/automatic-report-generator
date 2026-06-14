import sys
import os

from leitor import carregar_dados

from analise import (
    analisar_dados,
    identificar_colunas,
    gerar_insights
)

from graficos import gerar_graficos
from relatorio import gerar_relatorio
from database import (
    salvar_dataframe,
    registrar_importacao
)


def main():

    if len(sys.argv) < 2:

        print(
            "Uso: python src/main.py caminho_do_arquivo"
        )

        return

    arquivo = sys.argv[1]

    df = carregar_dados(arquivo)

    nome_tabela = os.path.splitext(
        os.path.basename(arquivo)
    )[0]

    print(f"\nArquivo carregado: {arquivo}")

    tipos = identificar_colunas(df)

    print("\n=== TIPOS DE COLUNAS ===")

    for coluna, tipo in tipos.items():
        print(f"{coluna}: {tipo}")

    resultado = analisar_dados(df)

    print("\n=== RESUMO DO DATASET ===")
    print(f"Linhas : {resultado['linhas']}")
    print(f"Colunas: {resultado['colunas']}")

    salvar_dataframe(
        df,
        nome_tabela
    )
    registrar_importacao(
         arquivo=arquivo,
         tabela=nome_tabela,
         linhas=resultado["linhas"],
         colunas=resultado["colunas"]
    )

    gerar_graficos(df)

    insights = gerar_insights(resultado)

    gerar_relatorio(
        resultado,
        "reports/relatorio.pdf",
        insights
    )

    print("\nProcessamento concluído com sucesso!")


if __name__ == "__main__":
    main()