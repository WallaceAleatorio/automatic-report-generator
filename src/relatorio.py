from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os


def gerar_relatorio(resultado, caminho_pdf="reports/relatorio.pdf", insights=None):
    os.makedirs("reports", exist_ok=True)

    doc = SimpleDocTemplate(caminho_pdf)

    estilos = getSampleStyleSheet()

    elementos = []

    titulo = Paragraph(
        "Relatório Automático de Dados",
        estilos["Title"]
    )

    elementos.append(titulo)
    elementos.append(Spacer(1, 20))

    elementos.append(
        Paragraph(
            f"Total de linhas: {resultado['linhas']}",
            estilos["Normal"]
        )
    )

    elementos.append(
        Paragraph(
            f"Total de colunas: {resultado['colunas']}",
            estilos["Normal"]
        )
    )

    elementos.append(Spacer(1, 20))

    elementos.append(
        Paragraph(
            "Estatísticas das colunas numéricas",
            estilos["Heading2"]
        )
    )

    elementos.append(Spacer(1, 10))

    for coluna, dados in resultado["estatisticas"].items():

        texto = f"""
        <b>{coluna}</b><br/>
        Soma: {dados['soma']:.2f}<br/>
        Média: {dados['media']:.2f}<br/>
        Máximo: {dados['maximo']:.2f}<br/>
        Mínimo: {dados['minimo']:.2f}
        """

        elementos.append(
            Paragraph(texto, estilos["BodyText"])
        )

        elementos.append(Spacer(1, 10))

        elementos.append(Spacer(1, 20))
        
        elementos.append(
        Paragraph(
            "Insights Automáticos",
            estilos["Heading1"]
        )
    )

    elementos.append(Spacer(1, 10))

    if insights:

        for insight in insights:

            elementos.append(
                Paragraph(
                    f"• {insight}",
                    estilos["BodyText"]
                )
            )

            elementos.append(
                Spacer(1, 5)
            )
    elementos.append(PageBreak())

    elementos.append(
        Paragraph(
            "Gráficos",
            estilos["Heading1"]
        )
    )

    elementos.append(Spacer(1, 20))

    for arquivo in os.listdir("charts"):

        if arquivo.endswith(".png"):

            elementos.append(
                Paragraph(
                    arquivo.replace(".png", ""),
                    estilos["Heading2"]
                )
            )

            elementos.append(
                Image(
                    f"charts/{arquivo}",
                    width=400,
                    height=250
                )
            )

            elementos.append(Spacer(1, 20))

    doc.build(elementos)

    print(f"PDF gerado: {caminho_pdf}")