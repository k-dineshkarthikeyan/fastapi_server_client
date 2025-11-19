from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class PingData(BaseModel):
    message: str


@app.post("/ping")
def ping(data: PingData):
    print(f"Your message: {data.message}")
    return {"response": "pong"}
