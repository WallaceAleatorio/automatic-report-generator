# 📊 Gerador Inteligente de Relatórios

Sistema desenvolvido em Python para automatizar a análise de arquivos CSV e Excel, gerar gráficos, criar relatórios em PDF e armazenar os dados em PostgreSQL.

## 🚀 Funcionalidades

* Importação automática de arquivos CSV e Excel
* Identificação automática dos tipos de dados
* Estatísticas descritivas
* Geração automática de gráficos
* Geração de relatórios PDF
* Armazenamento dos dados em PostgreSQL
* Histórico de importações
* Estrutura preparada para integração com Power BI

## 🛠 Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib
* ReportLab
* PostgreSQL
* SQLAlchemy
* python-dotenv

## 📂 Arquitetura

```text
Excel / CSV
     ↓
Python
     ↓
Análise de Dados
     ↓
Gráficos
     ↓
Relatório PDF
     ↓
PostgreSQL
```

## ⚙️ Instalação

Clone o projeto:

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` baseado em `.env.example`.

Execute:

```bash
python src/main.py caminho_do_arquivo.csv
```

## 📈 Exemplo de Uso

```bash
python src/main.py data/vendas.csv
```

O sistema irá:

* Ler o arquivo
* Gerar análises
* Criar gráficos
* Gerar PDF
* Salvar os dados no PostgreSQL
* Registrar a importação no histórico

## 🔮 Próximas Melhorias

* Dashboard Power BI
* Insights com IA
* API REST para upload de arquivos
* Interface Web
* Agendamento automático de processamento

## 👨‍💻 Autor

Wallace
