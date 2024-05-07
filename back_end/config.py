from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    class Config:
        env_file = ".env"


database_settings = DatabaseSettings()
