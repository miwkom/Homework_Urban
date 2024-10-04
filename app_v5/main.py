from fastapi import FastAPI
from app_v5.routers import task, user

app = FastAPI()


@app.get('/')
async def home():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(user.router)
app.include_router(task.router)
