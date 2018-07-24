import requests

from pipeline.mixins.mixins import SinkMixin

class Telegram(SinkMixin):
    def put_value(self, data):
        url = "https://api.telegram.org/bot{bot_id}/sendMessage".format(**self.config)
        requests.get(url, params={'chat_id': self.config['chat_id'], 'text': data})
