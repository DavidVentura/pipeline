from pipeline.mixins.mixins import FilterMixin

class Dummy(FilterMixin):
    def filter(self, data):
        return 'World' in data
