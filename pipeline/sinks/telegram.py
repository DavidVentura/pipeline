import requests

from pipeline.mixins.mixins import SinkMixin

class Telegram(SinkMixin):
    def put_value(self, data):
        url = "https://api.telegram.org/bot{bot_id}/sendMessage".format(**self.config)
        try:
            #r = requests.get(url, params={'chat_id': self.config['chat_id'], 'text': data, 'parse_mode': 'markdown'})
            r = requests.get(url, params={'chat_id': self.config['chat_id'], 'text': data})
            if r.status_code != 200:
                print("Got %s" % data)
                print(self.config)
                print(url)
                print(r.text)
        except Exception as e:
            print(e)
