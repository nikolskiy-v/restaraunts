from fastapi import FastAPI
from src.restaraunts.endpoints import v1_router

app = FastAPI()
app.include_router(v1_router, prefix="/api")

@app.get('/test')
async def get_test():
    return {"status": "OK"}