import pickle
from fastapi import APIRouter
import numpy as np
from schemas import schemas

router=APIRouter()

pkl_filenamec="prediccionCultivo.pkl"
with open(pkl_filenamec,'rb') as file:
    model =pickle.load(file)

labels = ["apple", "banana", "blackgram", "chickpea", "coconut", "coffee", "cotton",
          "grapes", "jute", "kidneybeans", "lentil", "maize", "mango", "mothbeans",
          "mungbean", "muskmelon", "orange", "papaya", "pigeonpeas", "pomegranate",
          "rice", "watermelon"]

@router.get("/")
async def root():
    return{
         "message":"hola"
    }

@router.post("/predict")
def predic_cultivo(data:schemas.Cultivodata):
    data=data.model_dump()
    N = data['N']
    P = data['P']
    K = data['K']
    temperature = data['temperature']
    humidity = data['humidity']
    ph = data['ph']
    rainfall = data['rainfall']

    xin = np.array([N, P, K, temperature, humidity, ph, rainfall]).reshape(1, 7)

    # Realizar la predicción con el modelo
    prediction = model.predict(xin)

    # Obtener la etiqueta correspondiente de las predicciones
    yout = labels[prediction[0]]

    return {
        'prediction': yout
    }



