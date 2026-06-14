# 📊 Automatic Report Generator

An automated data analysis pipeline built with Python that processes CSV and Excel files, generates charts, creates PDF reports, and stores processed data in PostgreSQL.

## 🚀 Features

* Import CSV and Excel files
* Automatic data type detection
* Descriptive statistics generation
* Automatic chart creation
* PDF report generation
* PostgreSQL integration
* Import history tracking
* Scalable architecture for BI dashboards

## 🛠 Tech Stack

* Python
* Pandas
* Matplotlib
* ReportLab
* PostgreSQL
* SQLAlchemy
* python-dotenv

## 📂 Architecture

```text
CSV / Excel
     ↓
Python
     ↓
Data Analysis
     ↓
Charts
     ↓
PDF Report
     ↓
PostgreSQL
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/automatic-report-generator.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file based on `.env.example`.

Run the application:

```bash
python src/main.py data/sample.csv
```

## 📈 Example Output

The system automatically:

* Reads CSV/Excel files
* Analyzes the dataset
* Generates visual charts
* Creates a PDF report
* Saves data to PostgreSQL
* Records the import history

## 🗄 Database Features

The application stores:

* Imported datasets
* Import history
* Processing metadata

This enables future integration with BI tools such as Power BI.

## 🔮 Future Improvements

* Power BI Dashboard
* AI-generated insights
* REST API
* Web interface
* Scheduled processing
* Cloud deployment

## 👨‍💻 Author

Wallace
