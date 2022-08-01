from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel


class Rule(BaseModel):
    id: Union[int, None] = None
    created_datetime: Optional[datetime]
    updated_datetime: Optional[datetime]
    deactivated_datetime: Optional[datetime]

    name: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    uri: Optional[str]

    code: Optional[str]
    code_ast: Optional[dict]
