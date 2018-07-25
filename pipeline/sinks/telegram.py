import requests

from pipeline.mixins.mixins import SinkMixin

class Telegram(SinkMixin):
    def put_value(self, data):
        parse_mode = 'markdown'
        if 'parse_mode' in self.config:
            parse_mode = self.config['parse_mode']

        params = {'chat_id': self.config['chat_id'],
                  'text': data,
                  'parse_mode': parse_mode}

        if parse_mode == 'text':
            del params['parse_mode']

        url = "https://api.telegram.org/bot{bot_id}/sendMessage".format(**self.config)
        try:
            r = requests.get(url, params=params)
            if r.status_code != 200:
                print("Got %s" % data)
                print(self.config)
                print(url)
                print(r.text)
        except Exception as e:
            print(e)
