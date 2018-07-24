from pipeline.mixins.mixins import FilterMixin

class Dummy(FilterMixin):
    def filter(self, data):
        return '2world' in data
