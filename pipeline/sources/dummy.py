from pipeline.mixins.mixins import SourceMixin

class Dummy(SourceMixin):
    def __init__(self):
        super().__init__()

    def get_value(self):
        return 'Hello world'
