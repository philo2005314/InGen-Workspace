# InGen Market Dashboard

## Overview

This project was completed as part of the InGen Dynamics Data Analysis Internship.

The dashboard provides an interactive interface for exploring market sizing, demographic indicators, and competitor analysis across two InGen Dynamics product verticals:

- Fari (Eldercare Robotics)
- Sentinel Prime AI (Physical Security)

The dashboard is backed by a SQLite data warehouse developed during Week 3 of the internship.

---

## Features

### US Market Overview

Displays market sizing estimates for:

- Eldercare
- Physical Security

Including:

- Total Addressable Market (TAM)
- Serviceable Available Market (SAM)

### Fari Eldercare

Displays eldercare demographic indicators and market sizing metrics.

### Sentinel Prime AI

Displays physical security market indicators and market sizing metrics.

### Competitor Explorer

Allows users to explore competitors by:

- Geography
- Vertical
- Distribution channel

---

## Project Structure

capstone_dashboard/

├── app.py

├── ingen_market_warehouse.sqlite

├── requirements.txt

└── README.md

---

## Installation

Install required packages:

pip install -r requirements.txt

---

## Running the Dashboard

Launch Streamlit:

streamlit run app.py

Open:

http://localhost:8501

in your browser.

---

## Data Sources

Public data sources used throughout the internship include:

- US Census
- BLS
- OECD
- Pew Research
- Security Industry Association
- SEC EDGAR
- JSAER
- arXiv
- NIH
- NCES
- Learning Policy Institute
- Competitor websites 

---

## Reproducibility

The dashboard is backed by the SQLite warehouse:

ingen_market_warehouse.sqlite

All visualizations are generated directly from the SQL warehouse using Streamlit, Pandas, and Plotly.

---

## Disclaimer

All market estimates are based on publicly available information and should be interpreted as directional estimates rather than precise forecasts.
