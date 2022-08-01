from pydantic import parse_obj_as
from gorgias.api_operations.base_operation import BaseOperation


class All(BaseOperation):
    def all(self):
        resource = self.schema_name_to_resource(self.schema)

        response = self.client.get(f"/{resource}")
        endpoint_data = response.json().get("data")

        resources = []
        for resource_data in endpoint_data:
            resources.append(self.schema(**resource_data))

        return resources
