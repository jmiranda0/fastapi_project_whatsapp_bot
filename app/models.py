from pydantic import BaseModel, Field
from typing import List, Optional

class Text(BaseModel):
    body: str

class Message(BaseModel):
    from_: str = Field(alias="from")

    text: Optional[Text] = None

    type: Optional[str] = None

class Value(BaseModel):
    messages: Optional[List[Message]] = None

class Change(BaseModel):
    value: Value

class Entry(BaseModel):
    changes: List[Change]


class WebhookBody(BaseModel):
    entry: List[Entry]