import requests

from pipeline.mixins.mixins import SinkMixin

class Telegram(SinkMixin):
    def put_value(self, data):
        url = "https://api.telegram.org/bot{bot_id}/sendMessage".format(**self.config)
        try:
            r = requests.get(url, params={'chat_id': self.config['chat_id'], 'text': data, 'parse_mode': 'markdown'})
        except Exception as e:
            print(e)
