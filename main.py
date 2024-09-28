from fastapi import FastAPI

from routers import routerCultivo
app=FastAPI()

app.include_router(routerCultivo.router)
