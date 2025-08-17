from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
import os
import crud


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(BASE_DIR, "templates")

templates = Jinja2Templates(template_dir)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class = HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})


   

