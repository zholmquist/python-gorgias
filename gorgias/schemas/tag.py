from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel


class TagDecoration(BaseModel):
    color: Optional[str]


class Tag(BaseModel):
    id: Union[int, None] = None
    created_datetime: Optional[datetime]
    deleted_datetime: Optional[datetime]

    name: Optional[str]
    description: Optional[str]
    decoration: Optional[TagDecoration]
    usage: Optional[int]
