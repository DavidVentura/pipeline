import json
import paho.mqtt.client as mqtt
import queue
import time
from pipeline.mixins.mixins import SourceMixin

class Mqtt(SourceMixin):
    def get_value(self):
        self.run = True
        self.q = queue.Queue()
        self.mqttc = mqtt.Client()
        self.mqttc.connect(self.config['host'], port=int(self.config['port']))

        self.config['topics'] = [topic.strip() for topic in self.config['topics'].split(',')]

        for topic in self.config['topics']:
            self.mqttc.subscribe(topic, qos=0)

        self.mqttc.on_message = self.on_message
        self.mqttc.loop_start()
        while self.run:
            try:
                item = self.q.get(timeout=1)
                if item is not None:
                    yield item
            except queue.Empty:
                time.sleep(1)

        self.mqttc.loop_stop()

    def on_message(self, client, userdata, message):
        # We assume messages will be ascii-encoded strings
        # that represent json.
        msg = message.payload.decode('ascii')
        try:
            j = json.loads(message.payload.decode('ascii'))
        except json.decoder.JSONDecodeError:
            return
        self.q.put({'topic': message.topic, 'data': j})
