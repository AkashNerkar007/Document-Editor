from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request ,Form
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from app.services.ai import get_suggestions


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

active_connections = []

@router.post("/suggest")
async def suggest(text: str = Form(...)):
    suggestion = get_suggestions(text)
    return JSONResponse(content={"suggestion": suggestion})

@router.get("/editor", response_class=HTMLResponse)
async def get_editor(request: Request):
    return templates.TemplateResponse("editor.html", {"request": request})

@router.websocket("/ws/editor")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast to all except sender
            for conn in active_connections:
                if conn != websocket:
                    await conn.send_text(data)
    except WebSocketDisconnect:
        active_connections.remove(websocket)
