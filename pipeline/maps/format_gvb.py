import datetime
from pipeline.mixins.mixins import MapMixin

def parse_date(date):
    return datetime.datetime.strptime(date.split("+")[0], "%Y-%m-%dT%H:%M:%S")

def format_diversion(diversion):
    ret = ""
    start = parse_date(diversion['startsAt']).strftime('%d/%m %H:%M')
    end = parse_date(diversion['endsAt']).strftime('%d/%m %H:%M')
    ret += "Start: %s -- End: %s\n" % (start, end)
    ret += "*%s*\n" % diversion['title']
    ret += "*Cause*: %s\n" % diversion['cause']
    ret += "*Effect*: %s\n" % diversion['effect']
    ret += "\n"
    ret += diversion['description']
    return ret


class FormatGvb(MapMixin):
    def process(self, data):
        return format_diversion(data)
