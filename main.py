from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# NLU.
from backend.intent_classifier import classify_user_input
from backend.agent import response_handler


app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", context={
        "request": request
    })


class Chat(BaseModel):
    """
    Validating the POST sent from client.
    """
    user_input: str


@app.post("/chat")
def chat_with_bot(chat: Chat):
    """
    Generates Bot Responses.
    """
    user_input = chat.user_input
    user_input_tokens, intent_detected, confidence, unk_percent = classify_user_input(user_input=user_input)

    response = response_handler(intent_detected=intent_detected,
                                user_input_tokens=user_input_tokens,
                                confidence=confidence,
                                unk_percent=unk_percent)
    return {
        "bot_response": response
    }


@app.get("/about")
def about(request: Request):
    """
    Displays About page.
    """
    return templates.TemplateResponse("about.html", {
        "request": request
    })