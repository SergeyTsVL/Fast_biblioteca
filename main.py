from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})

@app.get('/home', response_class=HTMLResponse)
async def home1(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})
# uvicorn main:app --reload

