import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

pickle_in = open('./model_XGBoost.pkl', 'rb') 
model_XGBoost = pickle.load(pickle_in)

app = FastAPI()


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
   
    print("La classe pred:",model_XGBoost.predict(pred)[0])
    class_pred = model_XGBoost.predict(pred)[0]
    if class_pred == 0 :
        return {'class':"Le credit à peu de risque d'etre en default"}
    elif class_pred == 1:
        return {'class':"Le credit à un risque important d'etre en default"}