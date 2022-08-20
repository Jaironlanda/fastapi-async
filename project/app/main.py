from fastapi import FastAPI


from . import v1
from .v1 import main

app = FastAPI()

@app.get('/')
async def root():
  return {'message': 'Hello World'}
    
app.include_router(v1.main.router)