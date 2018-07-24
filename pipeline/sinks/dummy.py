from pipeline.mixins.mixins import SinkMixin

class Dummy(SinkMixin):
    def put_value(self, data):
        print('[From dummy sink] %s' % data)
