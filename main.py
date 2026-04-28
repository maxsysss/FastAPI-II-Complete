<<<<<<< HEAD
from fastapi import FastAPI
from router import blog_get, blog_post
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get("/hello")
def index():
    return {"message": "Hello world!"}

models.Base.metadata.create_all(bind=engine)
=======
from typing import Optional
from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from db.database import engine
from db import models


app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
  return {'message': 'Hello world!'}

models.Base.metadata.create_all(engine)
>>>>>>> 01480abdaa879c674741d43e01f5255f38bd5a2c
