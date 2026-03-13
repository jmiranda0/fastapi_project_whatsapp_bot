from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI(
    title="FastAPI WhatsApp Bot",
    description="Backend for a WhatsApp bot using FastAPI",
    version="0.1.0"
)

app.include_router(api_router)