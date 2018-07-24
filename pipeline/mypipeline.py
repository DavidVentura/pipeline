#!/usr/bin/env python3
from pipeline.mixins.mixins import SourceMixin
from pipeline.mixins.mixins import SinkMixin
from pipeline.mixins.mixins import FilterMixin
from pipeline.mixins.mixins import MapMixin

def get_class_from_name(name):
    modulename = ".".join(name.split('.')[:-1])
    classname = name.split('.')[-1]
    module = __import__(modulename, fromlist=[classname])
    _class = getattr(module, classname)
    return _class

class Pipeline():
    def __init__(self, plugin_list):
        data = None
        pipeline_config = {}

        source = plugin_list[0]
        _class = get_class_from_name(source['plugin'])
        classname = _class.__name__
        config = source['config']
        _source = _class(config)

        plugin_list = plugin_list[1:]
        for entry in _source.get_value():
            data = entry
            print("Got [%s] from source %s" % (data, classname))
            
            for p in plugin_list:
                _class = get_class_from_name(p['plugin'])
                classname = _class.__name__
                config = p['config']
                instance = _class(config)

                # Sink -> Filter -> Map -> Source

                if isinstance(instance, SinkMixin):
                    print("Putting [%s] in sink %s" % (data, classname))
                    instance.put_value(data)

                if isinstance(instance, FilterMixin):
                    result = instance.filter(data)
                    print("Passing [%s] to filter %s => %s" % (data, classname, "Filtered" if result else "Passed"))
                    if result:
                        print("Filtering out!")
                        break

                if isinstance(instance, MapMixin):
                    _data = data
                    data = instance.process(data)
                    print("Processing [%s] in map %s => %s" % (_data, classname, data))
