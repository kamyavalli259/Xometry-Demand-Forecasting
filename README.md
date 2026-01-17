# Digital_Manufacturing_Demand_Forecasting
End-to-end demand forecasting and capacity optimization using Spark and ML

# End-to-End Demand Forecasting & Capacity Optimization for Digital Manufacturing

**Author:** Kamyavalli Mopidevi  
**Tech Stack:** Python, PySpark, XGBoost, ARIMA, MLflow, Linear Optimization, AWS-ready  

---

## 🚀 Project Overview

This project implements an **end-to-end data science pipeline** that forecasts manufacturing demand and optimizes manufacturer capacity allocation in a **digital manufacturing marketplace** context similar to **Xometry**.

The system is designed to simulate real-world challenges faced by on-demand manufacturing platforms:
- Volatile customer demand
- Capacity constraints across distributed manufacturers
- The need for accurate forecasting to improve delivery reliability and revenue

The pipeline spans **data ingestion → feature engineering → forecasting → optimization → evaluation**, following production-grade best practices.

---

## 🎯 Business Problem

In a manufacturing marketplace:
- Under-forecasting demand leads to **late deliveries and lost trust**
- Over-forecasting leads to **idle capacity and revenue loss**

**Goal:**  
Accurately forecast part-level demand and optimally allocate production across manufacturers while respecting capacity constraints.

---


## 🧠 Solution Architecture
```text
Raw Orders Data
↓
Spark ETL Pipeline
↓
Feature Engineering (lags, rolling stats, seasonality)
↓
Demand Forecasting Models
├─ ARIMA / SARIMAX (statistical baseline)
└─ XGBoost (machine learning)
↓
Capacity Optimization (Linear Programming)
↓
Evaluation & Business Impact Analysis

## 📦 Key Features

### 🔹 Scalable Data Pipeline
- Built using **PySpark** for large-scale data processing
- Clean separation between raw and processed datasets
- Ready for cloud deployment (AWS S3 / Glue / EMR)

### 🔹 Advanced Forecasting
- **Statistical Models:** ARIMA / SARIMAX for interpretability
- **Machine Learning:** XGBoost for non-linear demand patterns
- Time-based features: lags, rolling averages, seasonality

### 🔹 Capacity Optimization
- Formulated as a **linear programming problem**
- Minimizes cost while meeting forecasted demand
- Enforces manufacturer capacity constraints

### 🔹 Experiment Tracking
- Integrated **MLflow** for experiment logging
- Tracks parameters, metrics, and trained models

### 🔹 Business Impact Focus
- Evaluates RMSE & MAPE
- Simulates improvements in on-time delivery and capacity utilization

---

## 🗂 Project Structure

```text
xometry-demand-forecasting/
├── data/
│   ├── raw/                # Synthetic input data
│   ├── processed/          # Spark-processed datasets
│   └── generate_sample_data.py
├── etl/
│   └── spark_etl.py
├── features/
│   └── feature_engineering.py
├── models/
│   ├── arima_model.py
│   └── xgboost_model.py
├── optimization/
│   └── capacity_optimization.py
├── evaluation/
│   └── metrics.py
├── pipeline/
│   └── run_pipeline.py
├── requirements.txt
└── README.md


## ⚙️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/xometry-demand-forecasting.git
cd xometry-demand-forecasting

2. Install Dependencies
pip install -r requirements.txt. 

3. Generate sample data
python data/generate_sample_data.py


4. Run Spark ETL
spark-submit etl/spark_etl.py


5. Run the full pipeline
python pipeline/run_pipeline.py


6. View MLflow experiments
mlflow ui
Open: http://localhost:5000 





### 🧪 Experiments & Evaluation
--Rolling-origin time-series validation
--Comparison between statistical and ML-based models
--Sensitivity analysis on forecast error impact

###☁️ Cloud & Production Readiness
This project is designed to be easily extended to: 
-- **AWS S3** for cloud storage
-- **AWS Glue / EMR** for Spark processing
-- **Databricks** for collaborative development
-- **Airflow** for orchestration


###Skills Demonstrated
--Data Engineering (Spark, ETL, feature pipelines)
--Statistical Modeling & Machine Learning
--Time-Series Forecasting
--Optimization & Operations Research
--Experimentation & Model Tracking (MLflow)
--Business Impact Analysis
--Clear technical & non-technical communication


###📫 Contact

Kamyavalli Mopidevi
GitHub: https://github.com/kamyavalli259/Xometry-Demand-Forecasting 
LinkedIn: https://www.linkedin.com/in/kamyavallimopidevi259/ 

⭐ If you’re a recruiter or engineer reviewing this project, feel free to reach out!

