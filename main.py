from fastapi import FastAPI
from routes.routers import itemrouter
app = FastAPI()
app.include_router(itemrouter)

#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}