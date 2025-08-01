from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np
 
app = FastAPI()

# Load model
model = joblib.load("titanic_model.joblib")

# Input schema with validation
class Passenger(BaseModel):
    Pclass: int = Field(..., ge=1, le=3)
    Sex: int = Field(..., ge=0, le=1)
    Age: float = Field(..., ge=0)
    SibSp: int = Field(..., ge=0)
    Parch: int = Field(..., ge=0)
    Fare: float = Field(..., ge=0)
    Embarked: int = Field(..., ge=0, le=2)

@app.post("/predict")
def predict(data: Passenger):
    features = np.array([[data.Pclass, data.Sex, data.Age, data.SibSp, data.Parch, data.Fare, data.Embarked]])
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features).max()
    return {"prediction": int(prediction), "confidence": round(confidence, 2)}
# Health check endpoint
@app.get("/")
def health_check():
    return {"status": "ok", "message": "Titanic API is running"}                 