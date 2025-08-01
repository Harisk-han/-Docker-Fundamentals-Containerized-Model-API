# 🚢 Titanic Survival Prediction API (FastAPI + Docker)

This project provides a RESTful API for predicting Titanic passenger survival based on features like class, sex, age, and fare. It's built using **FastAPI** and served via **Docker**.

---

## 📦 Features

- 🚀 FastAPI-based backend for ML prediction  
- 🔍 Swagger UI at `/docs` for testing  
- 🐳 Dockerized for easy deployment  
- 🔮 Uses a trained Scikit-learn model (`titanic_model.joblib`)

---

## 📁 Project Structure

```
titanic_api/
│
├── app/
│   ├── main.py                # FastAPI app
│   └── titanic_model.joblib   # Pretrained ML model
│
├── requirements.txt           # Python dependencies
└── Dockerfile                 # Docker configuration
```

---

## 🔧 API Input Schema

```json
{
  "Pclass": 2,
  "Sex": 1,
  "Age": 25,
  "Fare": 30.5
}
---

## 🚀 How to Run with Docker

### 1. Build the Docker image

```bash
docker build -t titanic-fastapi .
```

### 2. Run the container

```bash
docker run -d -p 8000:8000 titanic-fastapi
```

### 3. Open in browser

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)  
You’ll see an interactive Swagger UI to test the `/predict` endpoint.

---

## 📤 Example Response

```json
{
  "prediction": 1,
  "confidence": 0.86
}
```

---

## 🧪 Test Locally without Docker

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
**Haris Khan**

---

## 📃 License

MIT License
