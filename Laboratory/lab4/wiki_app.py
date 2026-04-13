from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import wikipedia
import uvicorn

app = FastAPI()

wikipedia.set_lang("ru")


# 1 Задание
@app.get("/wiki/path/{title}", status_code=status.HTTP_200_OK)
def wiki_path(title: str):
    try:
        summary = wikipedia.summary(title, sentences=2)
        return {
            "title": title,
            "summary": summary
        }

    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail="Page not found")


# 2 Задание

@app.get("/wiki/query", status_code=status.HTTP_200_OK)
def wiki_query(title: str):
    try:
        summary = wikipedia.summary(title, sentences=2)
        return {
            "title": title,
            "summary": summary
        }
    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail="Page not found")


# 3 ЗАДАНИЕ
class WikiREquest(BaseModel):
    title: str

@app.post("/wiki/body", status_code=status.HTTP_201_CREATED)
def wiki_body(data: WikiREquest):
    try:
        summary = wikipedia.summary(data.title, sentences=2)
        return {
            "title": data.title,
            "summary": summary
        }
    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail="Page not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)