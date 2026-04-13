from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
import pyjokes
import uvicorn

app = FastAPI()

# ЗАДАНИЕ 200 HTTP STATUS

@app.get("/", status_code=status.HTTP_200_OK)
def joke():
    return {"joke": pyjokes.get_joke()}


@app.get("/{friend}", status_code=status.HTTP_200_OK)
def friends_joke(friend: str):
    return friend + " tells his joke: " + pyjokes.get_joke()


@app.get("/multi/{friend}", status_code=status.HTTP_200_OK)
def multi_friends_joke(friend: str, jokes_number: int):
    # ЗАДАНИЕ 3: ошибка 400
    if jokes_number < 1 or jokes_number > 10:
        raise HTTPException(
            status_code=400,
            detail="Количество шуток должно быть от 1 до 10"
        )

    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " "

    return {"result": result}


# ЗАДАНИЕ 4: path vs query

@app.get("/joke-path/{friend}", status_code=status.HTTP_200_OK)
def joke_by_path(friend: str):
    return {
        "method": "path",
        "friend": friend,
        "joke": pyjokes.get_joke()
    }


@app.get("/joke-query", status_code=status.HTTP_200_OK)
def joke_by_query(friend: str):
    return {
        "method": "query",
        "friend": friend,
        "joke": pyjokes.get_joke()
    }


#POST (ЗАДАНИЕ 1 + 2)

class Joke(BaseModel):
    friend: str
    joke: str


class JokeInput(BaseModel):
    friend: str = Field(..., min_length=2, max_length=50)


@app.post("/joke", response_model=Joke, status_code=status.HTTP_201_CREATED)
def create_joke(joke_input: JokeInput):
    return Joke(
        friend=joke_input.friend,
        joke=pyjokes.get_joke()
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
