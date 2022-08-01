from datetime import datetime
from typing import Optional, Union

from gorgias.schemas.api_resource import Resource


class TagDecoration(Resource):
    color: Optional[str]


class Tag(Resource):
    id: Union[int, None] = None
    created_datetime: Optional[datetime]
    deleted_datetime: Optional[datetime]

    name: Optional[str]
    description: Optional[str]
    decoration: Optional[TagDecoration]
    usage: Optional[int]
