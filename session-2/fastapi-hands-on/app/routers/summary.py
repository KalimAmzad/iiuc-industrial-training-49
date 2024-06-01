from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter(
    prefix="/summaries",
    tags=["summaries"],
)

@router.post("/", response_model=schemas.Summary)
def create_summary(summary: schemas.SummaryCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_summary(db=db, summary=summary)

@router.get("/{summary_id}", response_model=schemas.Summary)
def read_summary(summary_id: int, db: Session = Depends(dependencies.get_db)):
    db_summary = crud.get_summary(db, summary_id=summary_id)
    if db_summary is None:
        raise HTTPException(status_code=404, detail="Summary not found")
    return db_summary
