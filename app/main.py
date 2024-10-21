from fastapi import FastAPI, Query
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version
from typing import Annotated
# import uvicorn
# import os 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ValuesInput(BaseModel):
    value1: Annotated[float, Query(gt=0)]
    value2: Annotated[float, Query(gt=0)]
    value3: Annotated[float, Query(gt=0)]
    value4: Annotated[float, Query(gt=0)]

    class Config:
        extra = "forbid"

class PredictionOut(BaseModel):
    class_name: str

@app.get("/")
async def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
async def predict(payload: ValuesInput):
    result = predict_pipeline(payload)
    return {"class_name": result}
