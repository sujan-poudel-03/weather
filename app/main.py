from fastapi import FastAPI
from app.routes.weather import router as weather_router
import joblib

app = FastAPI(title="Weather API")

model = joblib.load("app/decision_tree_weather.pkl")

# Include weather routes
app.include_router(weather_router, prefix="/api/v1")

@app.post("/predict-weather")
def predict_weather(precipitation: float, temp_max: float, temp_min: float, wind: float, month: int, day: int, year: int):
    prediction = model.predict([[precipitation, temp_max, temp_min, wind, month, day, year]])
    return {"predicted_weather": int(prediction[0])}
