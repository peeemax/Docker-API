from fastapi import FastAPI, Depends

from project.app.config import Settings, get_settings

# Criado a API
app = FastAPI()


# Criando a página para API
@app.get("/ping")
def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.enviroment,
        "testing": settings.testing
    }
