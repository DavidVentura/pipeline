from pipeline.mixins.mixins import SourceMixin

class Dummy(SourceMixin):
    def get_value(self):
        yield 'Hello'
        yield 'Hello2'
        yield 'Hello'
        yield 'Hello4'
        yield 'Hello'
        yield 'World'
