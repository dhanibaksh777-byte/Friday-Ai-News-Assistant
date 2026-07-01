from fastapi import FastAPI
from pydantic import BaseModel
from core.agent import chat_With_friday


app = FastAPI()


class ChatRequest(BaseModel):
    message : str

@app.get("/")
def home():
    return {"status" : "friday is online"}

@app.post("/chat")
def chat(Request : ChatRequest):
   reply = chat_With_friday(Request.message)
   return {"reply":reply}
