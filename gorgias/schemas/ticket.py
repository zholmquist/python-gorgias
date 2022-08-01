from datetime import datetime
from enum import Enum
from typing import Optional, Union, Any

from gorgias.schemas.customer import Customer
from gorgias.schemas.message import Message
from gorgias.schemas.tag import Tag
from gorgias.schemas.api_resource import Resource


class TicketStatus(str, Enum):
    open = "open"
    closed = "closed"


class Ticket(Resource):
    id: Union[int, None] = None
    external_id: Optional[Any]
    created_datetime: Optional[datetime]
    updated_datetime: Optional[datetime]

    status: Optional[TicketStatus]
    channel: Optional[str]
    subject: Optional[str]
    customer: Optional[Customer]

    messages: Optional[list[Message]]
    tags: Optional[list[Tag]]

    from_agent: Optional[bool]
    via: Optional[str]
    spam: Optional[bool]

    trashed_datetime: Optional[datetime]
    opened_datetime: Optional[datetime]
    snooze_datetime: Optional[datetime]
    last_received_message_datetime: Optional[datetime]
    last_message_datetime: Optional[datetime]
    closed_datetime: Optional[datetime]

    language: Optional[str]  # format: ISO_639-1
