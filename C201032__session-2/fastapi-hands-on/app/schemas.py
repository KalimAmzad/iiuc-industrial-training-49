from pydantic import BaseModel

class NewsBase(BaseModel):
    title: str
    content: str

class NewsCreate(NewsBase):
    pass

class News(NewsBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True

class SummaryBase(BaseModel):
    news_id: int
    summary: str

class SummaryCreate(SummaryBase):
    pass

class Summary(SummaryBase):
    id: int

    class Config:
        from_attributes = True
