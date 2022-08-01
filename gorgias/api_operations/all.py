from pydantic import parse_obj_as
from gorgias.api_operations.base_operation import BaseOperation


class All(BaseOperation):
    """A mixin that provides `all` functionality."""

    def all(self):
        resource = self.schema_name_to_resource(self.schema)
        finder_url = "/%s" % (resource)

        response = self.client.get(finder_url)
        endpoint_data = response.json().get("data")

        resources = []
        for resource_data in endpoint_data:
            resources.append(parse_obj_as(self.schema, resource_data))

        return resources
