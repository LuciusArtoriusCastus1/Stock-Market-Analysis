from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from services.parsing_logic import parse_url
from services.urls import urls

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/static",
    StaticFiles(directory="app/frontend"),
    name="static"
)
app.mount(
    "/images",
    StaticFiles(directory="app/backend/images"),
    name="images"
)
templates = Jinja2Templates(directory="app/frontend/templates")


@app.get("/{url}/page/{page}")
async def root(url: str, page: int):
    return parse_url(urls[url] + f'{page}')


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
