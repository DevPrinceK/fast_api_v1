from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def hello_world():
    return {
        "salutation":"Hello, world",
        "body":"I am learning fastapi"
    }


@app.get('/greet/{person}')
async def greet_person(person: str):
    return {
        'greeting': f'hello, {person}'
    }