from pipeline.mixins.mixins import FilterMixin

class Dummy(FilterMixin):
    def __init__(self):
        super().__init__()

    def filter(self, data):
        return '2world' in data
