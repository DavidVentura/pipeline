from pipeline.mixins.mixins import FilterMixin

class Dummy(FilterMixin):
    count = 0
    def filter(self, data):
        self.state['count'] += 1
        return 'Hello%d' % self.state['count'] in data

    def get_state(self):
        return self.state

    def set_state(self, state):
        if 'count' not in state:
            state['count'] = 0
        self.state = state
