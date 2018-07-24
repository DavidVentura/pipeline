class SourceMixin():
    def get_value(self):
        raise NotImplementedError

class SinkMixin():
    def put_value(self):
        raise NotImplementedError

class FilterMixin():
    def filter(self, data):
        raise NotImplementedError

class MapMixin():
    def process(self, data):
        raise NotImplementedError
