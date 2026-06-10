from fastapi import FastAPI 
from app.routers.players import router as player_router

app = FastAPI()

app.include_router(player_router)

@app.get("/")
def root():
    return {"message": "Hello World"}
