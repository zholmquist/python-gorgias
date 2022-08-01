from gorgias.api_operations.all import All
from gorgias.api_operations.find import Find
from gorgias.api_operations.save import Save
from gorgias.api_operations.delete import Delete
from gorgias.api_operations.merge import Merge
from gorgias.service.base_service import BaseService

from gorgias.schemas import customer


class Customer(BaseService, All, Find, Save, Delete, Merge):
    schema = customer.Customer
