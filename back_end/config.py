from pydantic_settings import BaseSettings
from pydantic import SecretStr
import os


class AppSettings(BaseSettings):
    database_url: str
    database_port: int
    database: str
    DB_USERNAME: str
    database_password: str

    encryption_key_as_string_0: str
    encryption_key_as_string_1: str
    secret_key: SecretStr
    this_url: str
    session_expires_seconds: int
    mail_password: str
    system_users_mfa_secret: str
    super_user_name: str
    super_user_email: str
    super_user_password: SecretStr
    support_user_name: str
    support_user_email: str
    support_user_password: SecretStr
    instance_type: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '.env')


app_settings  = AppSettings()
