import os
import platform
import socket
import sys
from config import database_settings
from dotenv import load_dotenv
from fastapi import FastAPI
from pathlib import Path
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from starlette.middleware.cors import CORSMiddleware

# Append the parent directory of website/ to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

DATABASE_URL = (
    f"postgresql+asyncpg://{database_settings.db_user}:{database_settings.db_password}"
    f"@{database_settings.db_host}:{database_settings.db_port}/{database_settings.db_name}"
)


this_directory = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(this_directory, '..', '.env'), override=True)

# instantiate db for initialisation with app later
db = create_async_engine(DATABASE_URL, echo=True)

# Session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db, class_=AsyncSession)

# Base class for models
Base = declarative_base()

# create the holder for site config stuff
site_config = {}
site_config["platform"] = platform.system()
site_config["base_directory"] = os.path.abspath(os.path.dirname(__file__))
site_config["host_name"] = socket.gethostname()
site_config["environment"] = (
    f'host:{site_config["host_name"]}, platform:{site_config["platform"]}'
)
site_config["INSTANCE_TYPE"] = os.environ.get("INSTANCE_TYPE")
site_config["this_url"] = os.environ.get("this_url")

# Application instance
app = FastAPI()
# CORS middleware configuration
origins = [
    "https://localhost:5000",
    "https://localhost:5001",
    "https://localhost:5173",
    os.environ.get("this_url"),
    os.environ.get("video_call_url")
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


def create_app():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    static_folder = os.path.join(this_directory, "templates", "static")
    app.config.from_object("config.Config")

    from website.admin import bp as admin_bp

    app.register_blueprint(admin_bp, url_prefix="/api/admin")

    from website.auth import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    from website.users import bp as users_bp

    app.register_blueprint(users_bp, url_prefix="/api/users")

    from website.frontend import bp as frontend_bp

    app.register_blueprint(frontend_bp, url_prefix="/")

    from website.video_call import bp as video_call_bp

    app.register_blueprint(video_call_bp, url_prefix="/api/video_call")
