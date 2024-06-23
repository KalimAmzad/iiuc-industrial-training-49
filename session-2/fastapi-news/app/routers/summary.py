from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies, utility

router = APIRouter(
    prefix="/summaries",
    tags=["summaries"],
)

@router.post("/", response_model=schemas.Summary)
def create_summary(summary: schemas.SummaryFast, db: Session = Depends(dependencies.get_db)):
    news_id = summary.news_id
    news_body = crud.get_news(db, news_id=news_id).body
    # summary_text = summary.summary_text

    summary_text = utility.generate_summary(news_body)


    return crud.insert_summary(db=db, news_id=news_id, summary_text=summary_text)


@router.get("/{summary_id}", response_model=schemas.Summary)
def read_summary(summary_id: int, db: Session = Depends(dependencies.get_db)):
    print(summary_id)
    db_summary = crud.get_summary(db, summary_id=summary_id)
    if db_summary is None:
        raise HTTPException(status_code=404, detail="Summary not found")
    return db_summary



