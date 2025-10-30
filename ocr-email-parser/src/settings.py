import os
from typing import List, Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_ROOT_PATH: str = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    LOG_PATH: str = f"{PROJECT_ROOT_PATH}/logs/"
    LOG_LEVEL: str = "DEBUG"

    MODEL_PATH: str = f"{PROJECT_ROOT_PATH}/trained_models"

    API_ROOT_PATH: str = "/api"

    ENABLE_BUGSNAG_LOGGING: bool = True

    MONGO_HOST: List  # in .env = ["localhost", 27055]

    GEARMAN_HOST: Optional[str]

    class Config:
        case_sensitive = True

        # `.env.debug` takes priority over `.env`
        env_file = ".env", ".env.debug"


settings = Settings()
