from datetime import datetime
from enum import Enum
from typing import Optional, Union, Any

from gorgias.schemas.api_resource import Resource


class ChannelTypes(str, Enum):
    email = "email"
    phone = "phone"
    chat = "chat"
    twitter = "twitter"
    facebook = "facebook"
    instagram = "instagram"
    instagram_dm = "instagram-direct-message"


class CustomerChannel(Resource):
    id: Union[int, None] = None
    type: ChannelTypes
    address: str
    preferred: bool = False

    class Config:
        use_enum_values = True


class Customer(Resource):
    id: Union[int, None] = None
    external_id: Optional[Any]

    channels: Optional[list[CustomerChannel]]
    created_datetime: Optional[datetime]
    updated_datetime: Optional[datetime]
    name: Optional[str]
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str]  # EmailStr
    note: Optional[str]
    timezone: Optional[str]  # IANA timezone name

    data: Optional[dict]  # object

    integrations: Optional[dict]
    language: Optional[str]  # format: ISO_639-1
