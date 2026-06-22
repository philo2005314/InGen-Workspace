# InGen Dynamics Data Analysis Internship Capstone

## Program Summary

This repository contains the deliverables completed during a four-week Data Analysis Internship at InGen Dynamics.

The project focused on evaluating commercial opportunities across three product verticals:

* Fari (Eldercare Robotics)
* Sentinel Prime AI (Physical Security Intelligence)
* Senpai (Educational AI)

Key activities included market sizing, competitor analysis, customer segmentation, SQL warehouse development, and interactive dashboard construction.

The final capstone integrates these analyses into a reproducible market analysis workflow consisting of a SQL warehouse, Streamlit dashboard, executive memo, and presentation materials.

---

## Environment Setup

### Requirements

* Python 3.10+
* SQLite
* Streamlit
* Pandas
* Plotly

### Installation

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Dashboard

Navigate to the dashboard directory:

```bash
cd capstone_dashboard
```

Launch the application:

```bash
streamlit run app.py
```

Open the local URL displayed by Streamlit (typically http://localhost:8501).

---

## Reproducibility

The dashboard is powered by the SQLite warehouse:

```text
ingen_market_warehouse.sqlite
```

All visualizations are generated directly from warehouse tables using SQL queries, Pandas, and Plotly.

All market estimates are based on publicly available data sources documented in the corresponding analysis reports.

---

## Content Inventory

### Week 1

* Product and company research
* Competitor landscape review
* Data source inventory

### Week 2

* Eldercare market sizing (Fari)
* Physical security market sizing (Sentinel Prime AI)
* Vertical sizing workbook
* Midpoint review presentation

### Week 3

* Educational AI customer segmentation
* K-Means clustering analysis
* PCA analysis
* SQLite market warehouse
* SQL non-trivial analytical queries

### Week 4

* Streamlit dashboard
* Executive memo
* Handover presentation
* Exit reflection

---

## Public Data Sources

* US Census
* BLS
* OECD
* Pew Research
* Security Industry Association
* SEC EDGAR
* JSAER
* arXiv
* NIH
* NCES
* Learning Policy Institute
* Competitor websites 

---

## Disclaimer

- Market estimates should be interpreted as directional estimates rather than precise forecasts.
- No InGen confidential content is present and the repository is ready for later public release as a portfolio artifact.

