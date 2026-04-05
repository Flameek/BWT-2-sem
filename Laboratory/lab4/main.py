from fastapi import FastAPI, status, Query, HTTPException
import pyjokes
import uvicorn
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

# Задание 1 - Добавить Get-эндпоинты - статус 200 ОК
# Задание 2 - Валидация входные данных
@app.get("/", status_code=status.HTTP_200_OK)
def joke():
    return {"joke": pyjokes.get_joke()}


@app.get("/{friend}", status_code=status.HTTP_200_OK)
def friends_joke(friend: str):
    return friend + "tells his joke:" + pyjokes.get_joke()


@app.get("/multi/{friend}", status_code=status.HTTP_200_OK)
def multi_friends_joke(
        friend: str,
        jokes_number: int = Query(..., ge=1, le=10, description="Количество шуток от 1 до 10")
):
    # Проверка (третье задание)
    if jokes_number < 1 or jokes_number > 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Количество шуток должно быть от 1 до 10"
        )
    result = ""
    for i in range(jokes_number):
        result += friend + f"tells his joke #{i + 1}:" + pyjokes.get_joke() + " "
    return {"result:": result}

# 4ое задание добавление два новых эндпоинта с path и query параметром
@app.get("/joke-for/{friend}", status_code=status.HTTP_200_OK)
def joke_by_path(friend: str):
    return {
        "method": "path-parameter",
        "friend": friend,
        "joke": pyjokes.get_joke()
    }

@app.get("/joke-for", status_code=status.HTTP_200_OK)
def joke_by_query(friend: str):
    return {
        "method": "query-parameter",
        "friend": friend,
        "joke": pyjokes.get_joke()
    }

class Joke(BaseModel):
    friend: str
    joke: str
class JokeInput(BaseModel):
    friend: str = Field(..., min_length=2, max_length=50, description="Имя друга (минимум 2 символа)")

    @field_validator('friend')
    def validate_friend(cls, v):
        if not v.strip():
            raise ValueError('Имя не може тбы тьпустым или состоять из пробелов')
        return v.strip()


@app.post("/joke", status_code=status.HTTP_201_CREATED)
def create_joke(joke_input: JokeInput):
    return joke_input.friend + " tells his joke:" + pyjokes.get_joke()

@app.post("/", response_model=Joke, status_code=status.HTTP_201_CREATED)
def create_joke_structired(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
