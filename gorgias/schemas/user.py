from datetime import datetime
from enum import Enum
from typing import Optional, Union, Any
from pydantic import BaseModel


class RoleTypes(str, Enum):
    admin = "admin"
    user = "user"
    agent = "agent"
    basic_agent = "basic-agent"
    lite_agent = "lite-agent"
    observer_agent = "observer-agent"
    bot = "bot"


class Role(BaseModel):
    id: Union[int, None] = None
    name: Optional[RoleTypes]


class User(BaseModel):
    id: Union[int, None] = None
    external_id: Optional[Any]

    name: Optional[str]
    role: Optional[Role]
    roles: Optional[list[Role]]
    bio: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    email: Optional[str]
    active: Optional[bool]

    meta: Optional[dict]

    created_datetime: Optional[datetime]
    deactivated_datetime: Optional[datetime]
    updated_datetime: Optional[datetime]
