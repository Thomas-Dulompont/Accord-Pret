import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

pickle_in = open('./model_XGBoost.pkl', 'rb') 
model_XGBoost = pickle.load(pickle_in)

app = FastAPI()

class request_body(BaseModel):
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

@app.post("/predict")
def predict(data : request_body):
    pred=pd.DataFrame(dict(data),index=[0])
   
    print("La classe pred:",model_XGBoost.predict(pred)[0])
    class_pred = model_XGBoost.predict(pred)[0]
    
    return {'class':int(class_pred)}