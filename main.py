
from fastapi import FastAPI
from backend.routes.articles import router as articles_router
from backend.routes.trends import router as trends_router

app = FastAPI(title="Nepal Global Trends Platform")

app.include_router(articles_router)
app.include_router(trends_router)

@app.get("/")
def home():
    return {"message": "Nepal Global Trends API running"}
