from pipeline.mixins.mixins import MapMixin

class Dummy(MapMixin):
    def __init__(self):
        super().__init__()

    def process(self, data):
        return 'world' in data
