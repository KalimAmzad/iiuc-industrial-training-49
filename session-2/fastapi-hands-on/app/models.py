from sqlalchemy import Column, Integer, String, Text
from .database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)

class Summary(Base):
    __tablename__ = "summary"

    id = Column(Integer, primary_key=True, index=True)
    news_id = Column(Integer)
    summary = Column(Text)
