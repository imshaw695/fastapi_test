import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

this_directory = os.path.abspath(os.path.dirname(__file__))
path_to_templates = os.path.join(this_directory, "../templates")
templates = Jinja2Templates(directory=path_to_templates)

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    # Render the template using the context which includes the request
    return templates.TemplateResponse("index.html", {"request": request})
