from sqlalchemy import create_engine
from datetime import datetime
import pandas as pd

from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def salvar_dataframe(df, nome_tabela):

    df.to_sql(
        nome_tabela,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Tabela '{nome_tabela}' salva no PostgreSQL."
    )


def registrar_importacao(
    arquivo,
    tabela,
    linhas,
    colunas
):

    historico = pd.DataFrame([
        {
            "arquivo": arquivo,
            "tabela": tabela,
            "linhas": linhas,
            "colunas": colunas,
            "data_importacao": datetime.now()
        }
    ])

    historico.to_sql(
        "historico_importacoes",
        engine,
        if_exists="append",
        index=False
    )

    print(
        "Importação registrada com sucesso."
    )