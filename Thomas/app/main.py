import pickle
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import json

pickle_in = open('./RandomForest.pkl', 'rb') 
modelRandomForest = pickle.load(pickle_in)

app = FastAPI()

class request_body(BaseModel):
    State : str
    BankState: str
    NAICS : str
    Term : int
    NoEmp : int
    NewExist : int
    CreateJob : int
    RetainedJob: int
    FranchiseCode : int
    UrbanRural :int
    RevLineCr : int
    LowDoc:int
    DisbursementGross: float

@app.post("/predict")
def predict(data : request_body):
    pred=pd.DataFrame(dict(data),index = [0])
    class_idx = modelRandomForest.predict(pred)[0]

    return {'class':class_idx}