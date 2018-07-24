from pipeline.mixins.mixins import MapMixin

class Dummy(MapMixin):
    def process(self, data):
        return 'world' in data
