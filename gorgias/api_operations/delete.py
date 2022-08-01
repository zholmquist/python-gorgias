class Delete(object):
    def delete(self, obj):
        resource = self.schema_name_to_resource(self.schema)
        self.client.delete(f"/{resource}/{obj.id}")
        return obj
