<h1 align="center">Food Delivery Time Prediction API</h1>

<p align="center">
  A Machine Learning REST API built using FastAPI to predict food delivery time using a trained Linear Regression model.
</p>

<p align="center">

<a href="https://github.com/the-vignesh/Food-Delivery-Time-Prediction">
<img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" />
</a>

<img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" />

<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />

<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />

<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />

<img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge" />

<img src="https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge" />

</p>

---

# Overview

This project deploys a Machine Learning model using **FastAPI** to predict food delivery time based on customer, restaurant, order, and delivery-related information.

The model was trained using **Linear Regression** and exposed as a REST API with automatic documentation, input validation, and structured JSON responses.

---

# Repository

**GitHub**

https://github.com/the-vignesh/Food-Delivery-Time-Prediction

---

# Features

- Machine Learning model deployment using FastAPI
- Linear Regression prediction model
- Input validation using Pydantic
- Interactive Swagger Documentation
- Health Check endpoint
- Custom validation error handling
- Structured JSON responses
- Negative prediction handling

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| API Framework | FastAPI |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas |
| Model Serialization | Joblib |
| Validation | Pydantic |
| Server | Uvicorn |

---

# Project Structure

```text
Food-Delivery-Time-Prediction
│
├── app.py
├── linear_model.pkl
├── requirements.txt
├── README.md
│
├── Wk1_EDA.ipynb
├── Wk2_Rigorous_Modelling.ipynb
└── Wk3_Explainability_Failure_Analysis.ipynb
```

---

# Machine Learning Model

| Property | Value |
|----------|-------|
| Algorithm | Linear Regression |
| Target Variable | delivery_time_minutes |
| Deployment Framework | FastAPI |
| Model Format | Joblib (.pkl) |

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Information |
| GET | `/health` | Health Check |
| POST | `/predict` | Predict Delivery Time |

---

# Sample Request

```json
{
  "city_tier": 2,
  "customer_age": 28,
  "customer_loyalty_score": 7.5,
  "order_hour": 19,
  "order_day_of_week": 5,
  "order_month": 7,
  "delivery_distance_km": 6.2,
  "preparation_time_minutes": 18,
  "traffic_level_score": 7,
  "weather_severity_score": 2,
  "restaurant_rating": 4.5,
  "delivery_partner_rating": 4.7,
  "customer_rating": 4.8,
  "order_value": 650,
  "delivery_fee": 45,
  "discount_amount": 50,
  "tip_amount": 30,
  "final_amount_paid": 645,
  "number_of_items": 3,
  "promo_code_used": 1,
  "premium_customer_flag": 1,
  "festival_or_weekend_flag": 0,
  "delivery_partner_experience_years": 3
}
```

---

# Sample Response

```json
{
    "status": "success",
    "predicted_delivery_time_minutes": 34.82,
    "unit": "minutes",
    "model": "Linear Regression"
}
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/the-vignesh/Food-Delivery-Time-Prediction.git
```

Navigate to the project

```bash
cd Food-Delivery-Time-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the FastAPI server

```bash
uvicorn app:app --reload
```

Application URL

```
http://127.0.0.1:8000
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# Input Validation

The API validates incoming requests before performing predictions.

Validation includes:

- Customer age range
- City tier validation
- Restaurant and customer ratings
- Positive delivery distance
- Valid order month
- Valid order hour
- Binary flag validation

Invalid requests return structured validation errors.

---

# Future Improvements

- Deploy the API to a cloud platform
- Add Docker support
- Implement authentication
- Build a frontend dashboard
- Support multiple machine learning models

---

# Author

**Vignesh**

Software Engineering Intern

InfoPluse Technologies

GitHub: https://github.com/the-vignesh

---

<p align="center">
Built using FastAPI and Scikit-learn
</p>