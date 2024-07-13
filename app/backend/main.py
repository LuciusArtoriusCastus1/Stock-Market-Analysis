from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
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


@app.get("/{url}/page/{page}")
async def root(url: str, page: int):
    return parse_url(urls[url] + f'{page}')
