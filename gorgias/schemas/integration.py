from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel


class Integration(BaseModel):
    id: Union[int, None] = None
    uri: Optional[str]

    name: Optional[str]
    description: Optional[str]
    type: Optional[str]

    created_datetime: Optional[datetime]
    deactivated_datetime: Optional[datetime]
    updated_datetime: Optional[datetime]
