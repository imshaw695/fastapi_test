import os
from dotenv import load_dotenv
from website import create_app

# Load environment variables
this_directory = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(this_directory, ".env"))

app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
