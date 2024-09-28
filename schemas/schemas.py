from pydantic import BaseModel

class Cultivodata(BaseModel):
    N: int                      # Contenido de nitrógeno en el suelo
    P: int                      # Contenido de fósforo en el suelo
    K: int                      # Contenido de potasio en el suelo
    temperature: float          # Temperatura ambiental
    humidity: float             # Humedad ambiental
    ph: float                   # pH del suelo
    rainfall: float 