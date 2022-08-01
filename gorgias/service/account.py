from gorgias.api_operations.all import All
from gorgias.service.base_service import BaseService

from gorgias.schemas import customer


class Account(BaseService, All):
    schema = customer.Customer
