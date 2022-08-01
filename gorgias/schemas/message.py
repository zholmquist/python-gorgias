from datetime import datetime
from typing import Optional, Union, Any
from gorgias.schemas.api_resource import Resource


class Message(Resource):
    id: Union[int, None] = None
    external_id: Optional[Any]
    created_datetime: Optional[datetime]

    channel: Optional[str]  # Enum?
    subject: Optional[str]
    body_html: Optional[str]
    body_text: Optional[str]
    stripped_html: Optional[str]
    stripped_text: Optional[str]

    ticket_id: Optional[int]
    rule_id: Optional[int]
    integration_id: Optional[int]

    from_agent: Optional[bool]
    uri: Optional[str]

    failed_datetime: Optional[datetime]
    last_sending_error: Optional[datetime]
    sent_datetime: Optional[datetime]

    # channel to channels.py?
    # source
    # sender
    # receiver
