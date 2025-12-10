from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Be Hoc Vui API"

    # DB
    DATABASE_URL: str = "postgresql+psycopg2://user:password@postgres:5432/behocvui"

    # Auth
    SECRET_KEY: str = "CHANGE_THIS_TO_A_RANDOM_LONG_SECRET_KEY"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
