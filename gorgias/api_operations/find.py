from gorgias.api_operations.base_operation import BaseOperation


class Find(BaseOperation):
    def find(self, **params):
        resource = self.schema_name_to_resource(self.schema)

        if not "id" in params:
            return None

        response = self.client.get(f"{resource}/{params['id']}/", **params)

        return self.schema(**response.json())
