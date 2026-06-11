from fastapi import FastAPI 
from app.routers.players import router as player_router
from app.routers.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(player_router)

@app.get("/")
def root():
    return {"message": "Hello World"}
    