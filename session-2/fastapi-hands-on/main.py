from fastapi import FastAPI
import uvicorn
# from .routers import news, summary
from app.routers import news, summary

app = FastAPI()

app.include_router(news.router)
app.include_router(summary.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Summary API"}


if __name__ == "__main__":
    # uvicorn.run("main:app", host="localhost", port=8001, reload=True)
    uvicorn.run("main:app", host="localhost", port=8501, reload=True)