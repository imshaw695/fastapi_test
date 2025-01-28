from pydantic_settings import BaseSettings
from pydantic import SecretStr
import os


class AppSettings(BaseSettings):
    DB_URL: str
    DB_PORT: int
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    ENCRYPTION_KEY_AS_STRING_0: str
    ENCRYPTION_KEY_AS_STRING_1: str
    SECRET_KEY: SecretStr
    this_url: str
    SESSION_EXPIRES_SECONDS: int
    MAIL_PASSWORD: str
    system_users_mfa_secret: str
    super_user_name: str
    super_user_email: str
    super_user_password: SecretStr
    support_user_name: str
    support_user_email: str
    support_user_password: SecretStr
    INSTANCE_TYPE: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '.env')


app_settings = AppSettings()
