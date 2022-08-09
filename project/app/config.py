import logging
import os

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


# Classe Settings
class Settings(BaseSettings):
    enviroment: str = os.getenv("ENVIRONMENT", "dev")  # Definindo ambiente dev
    testing: bool = os.getenv("TESTING", 0)  # Definindo se esta no modo teste ou não


def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
