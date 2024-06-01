from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, dependencies

router = APIRouter(
    prefix="/news",
    tags=["news"],
)

@router.post("/", response_model=schemas.News)
def create_news(news: schemas.NewsCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_news(db=db, news=news)

@router.get("/{news_id}", response_model=schemas.News)
def read_news(news_id: int, db: Session = Depends(dependencies.get_db)):
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news

@router.get("/", response_model=list[schemas.News])
def read_news_list(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    return crud.get_news_list(db=db, skip=skip, limit=limit)
