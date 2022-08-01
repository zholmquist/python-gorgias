import requests

from gorgias.api_operations.base_operation import BaseOperation


class Save(BaseOperation):
    def create(self, **params):
        resource = self.schema_name_to_resource(self.schema)
        response = self.client.post(
            f"/{resource}", self.schema(**params).dict(exclude_unset=True)
        )

        return self.schema(**response.json())

    def save(self, obj):
        resource = self.schema_name_to_resource(self.schema)

        if not len(obj.changed_attributes):
            return obj

        response = self.client.put(
            f"{resource}/{obj.id}/",
            data=obj.json(
                exclude_unset=True,
                include=obj.changed_attributes,
            ),
        )
        return self.schema(**response.json())
