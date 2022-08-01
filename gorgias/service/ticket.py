from gorgias.api_operations.all import All
from gorgias.api_operations.find import Find
from gorgias.api_operations.save import Save
from gorgias.api_operations.delete import Delete
from gorgias.service.base_service import BaseService

from gorgias.schemas import ticket


class Ticket(BaseService, All, Find, Delete, Save):
    schema = ticket.Ticket
