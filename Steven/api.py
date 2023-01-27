import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

pickle_in = open('./model_XGBoost.pkl', 'rb') 
model_XGBoost = pickle.load(pickle_in)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5500",
    "http://localhost:8000",
    "https://localhost",
    "https://localhost:8080",
    "https://localhost:5500",
    "https://localhost:8000",
    "127.0.0.1:8000",
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


@app.get("/predict/")
def predict(State : str,
    BankState: str,
    Term : float,
    NoEmp : float,
    NewExist : str,
    UrbanRural :str,
    LowDoc : int,
    GrAppv : float,
    have_franchise : int,
    sector : str,
    in_recession: int):

    data={
        "State" : State,
        "BankState": BankState,
        "Term" : Term,
        "NoEmp" : NoEmp,
        "NewExist" : NewExist,
        "UrbanRural" :UrbanRural,
        "LowDoc" : LowDoc,
        "GrAppv" : GrAppv,
        "have_franchise" : have_franchise,
        "sector" : sector,
        "in_recession": in_recession
    }
    pred=pd.DataFrame(dict(data),index=[0])
    class_pred = model_XGBoost.predict(pred)[0]
    if class_pred == 0 :
        return {'class':"Le credit à peu de risque d'etre en default"}
    elif class_pred == 1:
        return {'class':"Le credit à un risque important d'etre en default"}