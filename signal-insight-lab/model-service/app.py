"""Optional atspm-detector prediction backend for Signal Insight Lab.
Run with uvicorn app:app --host 127.0.0.1 --port 8000.
No uploaded events are saved by this application.
"""
import os
from threading import Lock
from typing import Any

import pandas as pd
from atspm_detector import predict, __version__
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

APP_ORIGINS = [s.strip() for s in os.getenv("ALLOWED_ORIGINS", "https://markrahmanph.github.io").split(",") if s.strip()]
API_TOKEN = os.getenv("MODEL_API_TOKEN", "")
if not API_TOKEN:
    raise RuntimeError("Set MODEL_API_TOKEN to a random secret; this service is intentionally closed by default.")

app = FastAPI(title="Signal Insight Lab Model Service", version="0.1")
app.add_middleware(CORSMiddleware, allow_origins=APP_ORIGINS, allow_methods=["POST", "GET"], allow_headers=["Content-Type", "Authorization"])
lock = Lock()

class Event(BaseModel):
    timestamp: str
    code: int
    parameter: int

class PredictionRequest(BaseModel):
    events: list[Event] = Field(min_length=1, max_length=1500000)
    device_id: str = Field(default="uploaded-signal", min_length=1, max_length=128)

@app.get("/health")
def health():
    return {"status":"ready","model":"atspm-detector","version":__version__}

@app.post("/predict")
def prediction(payload: PredictionRequest, request: Request):
    if request.headers.get("Authorization", "") != f"Bearer {API_TOKEN}":
        raise HTTPException(401, "Invalid access token")
    if not lock.acquire(blocking=False):
        raise HTTPException(429, "Model busy; try again shortly")
    try:
        df = pd.DataFrame({
            "DeviceId": payload.device_id,
            "Timestamp": pd.to_datetime([e.timestamp for e in payload.events], errors="coerce"),
            "EventId": [e.code for e in payload.events],
            "Parameter": [e.parameter for e in payload.events],
        }).dropna(subset=["Timestamp"])
        if df.empty:
            raise HTTPException(422, "No valid timestamps")
        # Use original package and its bundled trained model weights.
        output = predict(df, threads=2, memory="2GB", min_actuations=5, min_prob=0.0)
        output = output.astype(object).where(pd.notna(output), None)
        fields = ["Detector","phase_pred","phase_prob","function_pred","function_prob","phase_guess","function_guess",
                  "status","review_flag","health_status","health_reason","lanes","distance_ft"]
        rows = []
        for entry in output.to_dict(orient="records"):
            rows.append({k:entry.get(k) for k in fields})
        return {"model":"atspm-detector","version":__version__,"detectors":rows}
    finally:
        lock.release()
