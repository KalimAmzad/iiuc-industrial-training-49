from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel



app = FastAPI()


news = {
    1:
    {
        "id": 1,
        "title": "Top 10 programming languages",
        "content": "Python is the most popular programming language according to the TIOBE index. Other popular",
        "author": "Kalim"
    },
    2:
    {
        "id": 2,
        "title": "LLM race in modern era",
        "content": "Content on modern LLM models both close & open source",
        "author": "Ibrahim"
    },
    3:
    {
        "id": 3,
        "title": "Latest LLM models from Mistral!!!",
        "content": "ontent on modern LLM models both close & oper",
        "author": "Kalim"
    },
    4:
    {
        "id": 4,
        "title": "What's the Google calls on LLM!!",
        "content": "ontent on modern LLM models both close & ope",
        "author": "Kalim"
    }
}



class News(BaseModel):
   title: str
   content: str | None = None
   author: str


@app.get("/")
def index():
   return {"message": "Hello World"}


@app.get("/news/{author}")
def get_news_by_author(author: str, title_contains: str = None):
   filtered_news = [news for news in news.values() if news["author"].lower() == author.lower()]
   print(filtered_news)
   if title_contains:
      print(title_contains)
      filtered_by_title = [news for news in filtered_news if title_contains.lower() in news["title"].lower()]
      return filtered_by_title
   else:
      return filtered_news

@app.get("/news")
def get_news():
    return news


@app.get("/news/{id}")
def get_news_by_id(id: int):
   single_news = news.get(id, None)
   if single_news:
       return single_news
   return {"message": f"News item with id {id} not found"}


@app.post("/create_news")
def create_news(input_news: News):
   id = max(news.keys()) + 1
   news[id] = {
       "id": id,
       "title": input_news.title,
       "content": input_news.content,
       "author": input_news.author
   }

   print(news[id])
   return news[id]
   


if __name__ == '__main__':
    uvicorn.run("basic_female:app", host='localhost', port=8000, reload=True)

