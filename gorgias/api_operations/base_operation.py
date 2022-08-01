import inflection


class BaseOperation(object):
    def pluralize(self, str):
        return inflection.pluralize(str)

    def schema_name_to_resource(self, schema):
        return self.pluralize(schema.__name__.lower())
