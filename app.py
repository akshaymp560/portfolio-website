from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def load_projects():
    with open('data/projects.json', 'r') as file:
        return json.load(file)

@app.get("/")
async def home(request: Request):
    projects = load_projects()
    # FIXED: Using explicit keyword arguments for the latest FastAPI version
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"projects": projects}
    )

@app.get("/project/{project_id}")
async def project_detail(request: Request, project_id: str):
    projects = load_projects()
    project = projects.get(project_id)
    # FIXED: Using explicit keyword arguments for the latest FastAPI version
    return templates.TemplateResponse(
        request=request, 
        name="project_detail.html", 
        context={"project": project}
    )