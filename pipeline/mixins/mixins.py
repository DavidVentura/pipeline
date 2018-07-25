class SourceMixin():
    def __init__(self, config):
        self.config = config

    def get_value(self):
        raise NotImplementedError

class SinkMixin():
    def __init__(self, config):
        self.config = config

    def put_value(self):
        raise NotImplementedError

class FilterMixin():
    def __init__(self, config):
        self.config = config
        self.state = {}

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def filter(self, data):
        raise NotImplementedError

class MapMixin():
    def __init__(self, config):
        self.config = config

    def process(self, data):
        raise NotImplementedError
