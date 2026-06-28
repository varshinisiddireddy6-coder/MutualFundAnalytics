# Mutual Fund Analytics Platform

## Overview

A full-stack Mutual Fund Analytics Platform built using real Indian mutual fund data from AMFI and mfapi.in. The project implements an end-to-end analytics pipeline including data ingestion, ETL processing, database design, exploratory analysis, risk analytics, and dashboard visualization.

## Objectives

* Build an automated ETL pipeline using Python.
* Design a normalized SQL database schema.
* Analyze NAV, AUM, SIP, and investor transaction data.
* Compute risk metrics such as Sharpe Ratio, Sortino Ratio, Alpha, Beta, and Maximum Drawdown.
* Develop an interactive Power BI dashboard.
* Generate actionable business insights from mutual fund and investor data.

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* SQLAlchemy
* Jupyter Notebook
* Power BI
* Git & GitHub

## Datasets

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

## Key Insights

* 32,778 investor transactions analyzed.
* SIP transactions represent 60.15% of all transactions.
* Highest Sharpe Ratio: ICICI Prudential Liquid Fund (7.68).
* Highest Alpha: HDFC Short Term Debt Fund (1.98).
* Investors aged 26–35 form the largest investment segment.
* T30 cities account for approximately 66% of transactions.

## Dashboard Pages

### Page 1: Market Overview

* Industry AUM
* SIP Trends
* Folio Growth
* Category Inflows

### Page 2: Fund Performance & Risk

* Sharpe Ratio Analysis
* Alpha Ranking
* Risk vs Return

### Page 3: Investor Demographics

* Age Distribution
* Gender Analysis
* State-wise Participation
* Income Distribution


## Project Outcome

Successfully developed a complete mutual fund analytics platform capable of processing 87,000+ records and generating business intelligence insights through interactive dashboards.
