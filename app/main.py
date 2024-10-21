from fastapi import FastAPI, Query
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version
from typing import Annotated

app = FastAPI()


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
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: ValuesInput):
    result = predict_pipeline(payload)
    return {"class_name": result}
