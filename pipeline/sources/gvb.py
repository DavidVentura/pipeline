import datetime
import json
import requests

from pipeline.mixins.mixins import SourceMixin

DIVERSIONS_URL = 'https://maps.gvb.nl/api/v1/diversions?language=en'
ACK_IDs = [1923, 1910, 1745]

def parse_date(date):
    return datetime.datetime.strptime(date.split("+")[0], "%Y-%m-%dT%H:%M:%S")

def get_diversions(apikey, lines_interested):
    diversions = []
    HEADERS = {'X-Api-Key': apikey}

    r = requests.get(DIVERSIONS_URL, headers=HEADERS)
    j = r.json()

    for diversion in j['diversions']:
        start = diversion['startsAt']
        end = diversion['endsAt']
        
        start = parse_date(start)
        end = parse_date(end)
        now = datetime.datetime.now()
        if end < now or start > now:
            continue
        lines = [(line['vehicletype'], int(line['publicnumber'])) for line in diversion['affectedLines']]
        if not any([line[1] in lines_interested for line in lines]):
            continue
        if diversion['id'] in ACK_IDs:
            continue
        diversions.append(diversion)
    return diversions

class Gvb(SourceMixin):
    def get_value(self):
        lines = [int(line.strip()) for line in self.config['lines_interested'].split(',')]
        return get_diversions(self.config['apikey'], lines)
