from sqlalchemy.orm import Session
from . import models, schemas

def get_news(db: Session, news_id: int):
    return db.query(models.News).filter(models.News.id == news_id).first()

def get_news_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.News).offset(skip).limit(limit).all()

def create_news(db: Session, news: schemas.NewsCreate):
    db_news = models.News(title=news.title, content=news.content)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

def create_summary(db: Session, summary: schemas.SummaryCreate):
    db_summary = models.Summary(news_id=summary.news_id, summary=summary.summary)
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)
    return db_summary
