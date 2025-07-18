from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import auth, doc
from app.database import init_db

app = FastAPI()

# Mount static files (JS, CSS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load HTML templates
templates = Jinja2Templates(directory="app/templates")

# Register routes
app.include_router(auth.router)
app.include_router(doc.router)

# Create DB tables on startup
@app.on_event("startup")
async def startup():
    init_db()
