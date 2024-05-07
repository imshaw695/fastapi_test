import os
import platform
import socket
import sys
from config import app_settings
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from starlette.middleware.cors import CORSMiddleware

# Append the parent directory of website/ to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

DATABASE_URL = (
    f"postgresql+asyncpg://{app_settings.DB_USERNAME}:{app_settings.database_password}"
    f"@{app_settings.database_url}:{app_settings.database_port}/{app_settings.database}"
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


def create_app() -> FastAPI:
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
    static_files_path = os.path.join(this_directory, "templates", "static", "assets")
    app.mount("/static", StaticFiles(directory=static_files_path), name="static")
    print("Static files directory:", static_files_path)
    from website.frontend import routes as frontend

    app.include_router(frontend.router)

    return app
