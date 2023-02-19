from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello_world():
    '''Return a simple hellow world greeting'''
    return {"salutation": "Hello, world", "body": "I am learning fastapi"}


@app.get('/greet/{person}')
async def greet_person(person: str):
    '''Return a simple greeting using url params'''
    return {'greeting': f'hello, {person}'}
