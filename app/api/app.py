from fastapi import FastAPI

from app.core.db.database import set_engine

app = FastAPI()


@app.on_event("startup")
def on_startup():
    set_engine()
