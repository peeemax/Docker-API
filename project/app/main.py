from fastapi import FastAPI

# Criado a API
app = FastAPI()


# Criando a página para API
@app.get("/ping")
def ping():
    return {
        "ping": "pong"
    }
