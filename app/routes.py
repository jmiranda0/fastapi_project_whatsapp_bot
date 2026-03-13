import os
from fastapi import APIRouter, Request, Query
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv

from app.models import WebhookBody

load_dotenv()
router = APIRouter()

@router.get("/")
def home():
    
    return {"status": "bot running"}

@router.get("/webhook")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token")
):
    verify_token = os.getenv("WHATSAPP_TOKEN")

    if hub_mode == "subscribe" and hub_verify_token == verify_token:
        print("Webhook verificado correctamente")
        return PlainTextResponse(content=hub_challenge)

    return PlainTextResponse("Verification failed", status_code=403)

@router.post("/webhook")
async def receive_message(body: WebhookBody):

    try:
        message = body.entry[0].changes[0].value.messages[0]

        phone_number = message.from_
        text = message.text.body if message.text else None

        print("Mensaje recibido")
        print("Telefono:", phone_number)
        print("Texto:", text)

    except Exception as e:
        print("Error procesando webhook:", e)

    return {"status": "received"}