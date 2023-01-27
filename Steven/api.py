import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
pickle_in = open('./model_XGBoost.pkl', 'rb') 
model_XGBoost = pickle.load(pickle_in)


origins = [
    "http://127.0.0.1:5500",
]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]


app = FastAPI(middleware=middleware)

class Request(BaseModel):
    State : str
    BankState: str
    Term : float
    NoEmp : float
    NewExist : str
    UrbanRural :str
    LowDoc : int
    GrAppv : float
    have_franchise : int
    sector : str
    in_recession: int


@app.post("/predict/")
def predict(data:Request):

    pred=pd.DataFrame(dict(data),index=[0])
    class_pred = model_XGBoost.predict(pred)[0]
    if class_pred == 0 :
        return {'class':"Le credit à peu de risque d'etre en default"}
    elif class_pred == 1:
        return {'class':"Le credit à un risque important d'etre en default"}