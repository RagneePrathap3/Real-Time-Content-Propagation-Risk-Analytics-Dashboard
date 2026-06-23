# Real-Time Content Propagation & Risk Analytics Dashboard

## Overview

This project is an end-to-end analytics solution that ingests live news data from NewsAPI, stores it in PostgreSQL, computes custom risk metrics, and visualizes content propagation patterns through an interactive Power BI dashboard.

The goal is to monitor news content across multiple sources, classify articles into topics, calculate risk indicators, and provide actionable insights through KPI-driven reporting.

---

## Architecture

NewsAPI → Python ETL Pipeline → PostgreSQL → SQL Analytics → Power BI Dashboard

---

## Features

* Live news ingestion using NewsAPI
* Automated ETL pipeline built in Python
* PostgreSQL data storage
* Topic classification
* Risk scoring framework
* Topic velocity analysis
* Source distribution analysis
* Interactive Power BI dashboard

---

## Tech Stack

* Python
* Pandas
* NewsAPI
* PostgreSQL
* psycopg2
* SQL
* Power BI

---

## Key Metrics

* Articles Analyzed
* Sources Monitored
* Highest Risk Score
* Total Risk Score
* Topic Velocity
* Source Distribution

---

## Dashboard Insights

The dashboard provides visibility into:

* Topic-wise risk distribution
* News source contribution
* Content propagation velocity
* Overall risk trends
* Source concentration patterns

---

## Project Workflow

1. Fetch live articles using NewsAPI
2. Transform and clean data using Python
3. Load records into PostgreSQL
4. Compute KPIs using SQL
5. Visualize insights in Power BI

---

## Future Enhancements

* Automated topic classification using NLP
* Sentiment analysis
* Real-time dashboard refresh
* Trend prediction models
* Alerting system for high-risk topics
