from pipeline.mixins.mixins import SinkMixin

class Dummy(SinkMixin):
    def __init__(self):
        super().__init__()

    def put_value(self, data):
        print('[From dummy sink] %s' % data)
