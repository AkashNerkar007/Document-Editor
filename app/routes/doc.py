from fastapi import APIRouter

router = APIRouter()

@router.get("/editor")
def editor_page():
    return {"message": "Editor coming soon..."}
