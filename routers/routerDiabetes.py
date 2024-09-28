import pickle
from fastapi import APIRouter, FastAPI
from Diabetesdata import Diabetesdata
import numpy as np
from schemas import schemas

router=APIRouter()

pkl_filenamec="RFDiabetesv102.pkl"
with open(pkl_filenamec,'rb') as file:
    model =pickle.load(file)

labels=["sano","posible diabetes"]


@router.get("/")
async def root():
    return{
         "message":"hola"
    }

@router.post("/predict")
def predic_diabetes(data:schemas.Diabetesdata):
    data=data.model_dump()
    Pregnancies=data['Pregnancies']
    Glucose=data['Glucose']
    BloodPressure=data['BloodPressure']
    SkinThickness=data['SkinThickness']
    Insulin=data['Insulin']
    BMI=data['BMI']
    DiabetesPedigreeFunction=data['DiabetesPedigreeFunction']
    Age=data['Age']

    xin=np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]).reshape(1,8)
    prediction=model.predict(xin)
    yout=labels[prediction[0]]
    return {
        'prediction':yout
    }



