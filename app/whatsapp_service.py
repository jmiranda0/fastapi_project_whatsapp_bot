import os
import httpx
from dotenv import load_dotenv

load_dotenv()


WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")
WHATSAPP_API_KEY = os.getenv("WHATSAPP_API_KEY")

WHATSAPP_API_URL = f"https://graph.facebook.com/v19.0/{WHATSAPP_PHONE_ID}/messages"


async def send_message(to: str, message: str) -> dict:
    
    headers = {
        "Authorization": f"Bearer {WHATSAPP_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",  
        "to": to,                          
        "type": "text",                    
        "text": {
            "body": message               
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            WHATSAPP_API_URL,
            headers=headers,
            json=payload
        )

    return response.json()