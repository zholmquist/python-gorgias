from datetime import datetime
from typing import Optional, Union
from gorgias.schemas.api_resource import Resource


class Rule(Resource):
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
