
from fastapi import APIRouter
from backend.database import SessionLocal
from backend.models.article import Article

router = APIRouter(prefix="/articles")

@router.get("/")
def get_articles():

    db = SessionLocal()
    articles = db.query(Article).all()
    db.close()

    return articles
