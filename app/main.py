from fastapi import FastAPI
from.routes import task

app = FastAPI()

@app.get('/')
def root_message():
    return {'meesage' : 'hello world'}

app.include_router(task.router)