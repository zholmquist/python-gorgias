class Merge(object):
    def merge(self, source, target):
        resource = self.schema_name_to_resource(self.schema)
        params = {"source_id": source.id, "target_id": target.id}
        response = self.client.put(f"{resource}/merge", params)
        return response
