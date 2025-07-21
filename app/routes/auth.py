from fastapi import APIRouter, HTTPException, Form, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.database import SessionLocal
from app.models import User
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register Page
@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# Register Logic
@router.post("/register")
def register_user(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    hashed_pw = bcrypt.hash(password)
    new_user = User(email=email, password=hashed_pw)
    db.add(new_user)
    db.commit()
    return RedirectResponse(url="/login", status_code=302)

# Login Page
@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Login Logic
@router.post("/login")
def login_user(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not bcrypt.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    response = RedirectResponse(url="/editor", status_code=302)
    # In real case, set cookie or token here
    return response
