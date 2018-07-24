from pipeline.mixins.mixins import SourceMixin

class Dummy(SourceMixin):
    def get_value(self):
        yield 'Hello'
        yield 'World'
