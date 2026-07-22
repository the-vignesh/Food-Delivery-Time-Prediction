from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ConfigDict
import pandas as pd
import joblib

# ==========================
# Load Trained Model
# ==========================
model = joblib.load("linear_model.pkl")

# ==========================
# Create FastAPI App
# ==========================
app = FastAPI(
    title="Food Delivery Time Prediction API",
    description="Predicts food delivery time using a trained Linear Regression model.",
    version="1.0.0"
)

# ==========================
# Custom Validation Handler
# ==========================
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):

    errors = []

    for error in exc.errors():
        errors.append({
            "field": error["loc"][-1],
            "message": error["msg"]
        })

    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "message": "Invalid input provided.",
            "errors": errors
        }
    )


# ==========================
# Input Schema
# ==========================
class DeliveryInput(BaseModel):

    city_tier: int = Field(..., ge=1, le=3, description="City Tier (1-3)")
    customer_age: int = Field(..., ge=18, le=100)
    customer_loyalty_score: float = Field(..., ge=0)

    order_hour: int = Field(..., ge=0, le=23)
    order_day_of_week: int = Field(..., ge=0, le=6)
    order_month: int = Field(..., ge=1, le=12)

    delivery_distance_km: float = Field(..., gt=0)
    preparation_time_minutes: float = Field(..., gt=0)

    traffic_level_score: float = Field(..., ge=0)
    weather_severity_score: float = Field(..., ge=0)

    restaurant_rating: float = Field(..., ge=1, le=5)
    delivery_partner_rating: float = Field(..., ge=1, le=5)
    customer_rating: float = Field(..., ge=1, le=5)

    order_value: float = Field(..., gt=0)
    delivery_fee: float = Field(..., ge=0)
    discount_amount: float = Field(..., ge=0)
    tip_amount: float = Field(..., ge=0)
    final_amount_paid: float = Field(..., gt=0)

    number_of_items: int = Field(..., ge=1)

    promo_code_used: int = Field(..., ge=0, le=1)
    premium_customer_flag: int = Field(..., ge=0, le=1)
    festival_or_weekend_flag: int = Field(..., ge=0, le=1)

    delivery_partner_experience_years: float = Field(..., ge=0)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
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
        }
    )


# ==========================
# Home Endpoint
# ==========================
@app.get("/", summary="API Home")
def home():

    return {
        "status": "success",
        "message": "Welcome to the Food Delivery Time Prediction API",
        "model": "Linear Regression",
        "version": "1.0.0"
    }


# ==========================
# Health Check Endpoint
# ==========================
@app.get("/health", summary="Health Check")
def health():

    return {
        "status": "healthy",
        "model_loaded": True
    }


# ==========================
# Prediction Endpoint
# ==========================
@app.post(
    "/predict",
    summary="Predict Delivery Time",
    description="Predicts the estimated food delivery time in minutes."
)
def predict(data: DeliveryInput):

    # Convert input JSON to DataFrame
    df = pd.DataFrame([data.model_dump()])

    # Predict delivery time
    prediction = float(model.predict(df)[0])

    # Prevent impossible negative predictions
    prediction = max(0.0, prediction)

    return {
        "status": "success",
        "predicted_delivery_time_minutes": round(prediction, 2),
        "unit": "minutes",
        "model": "Linear Regression"
    }