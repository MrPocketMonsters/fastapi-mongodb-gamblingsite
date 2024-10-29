from fastapi import FastAPI
from routes.route import router
from config.database import client

try:
    client.admin.command('ping')
    app = FastAPI()
    app.include_router(router)
except Exception as e:
    print(e)
