from fastapi import FastAPI
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Price Transparency API",
    description="Community-powered price intelligence for Nigerian markets",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Price Transparency API is live", "status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
