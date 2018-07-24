from configparser import ConfigParser

def build(name):
    parser = ConfigParser()
    parser.read('../config.ini')
    config = parser._sections
    pconfig = config['pipeline.%s' % name]
    pipeline = [plugin.strip() for plugin in pconfig['pipeline'].split('|')]
    ret = []
    for plugin in pipeline:
        plugin_conf = None
        plugin_name = plugin.split('.')[-1]
        config_section = 'plugin.%s' % plugin_name
        if config_section in config:
            plugin_conf = dict(config[config_section])
        ret.append({'plugin': plugin, 'config': plugin_conf})
    return ret
