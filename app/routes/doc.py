from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

active_connections = []

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
