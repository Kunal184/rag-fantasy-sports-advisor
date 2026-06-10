from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class PlayerAnalyzeRequest(BaseModel):
    player_name:str

@router.post("/players/analyze")
def analyze_player(request:PlayerAnalyzeRequest):
    return {"message": f"Analyzing player {request.player_name}"}