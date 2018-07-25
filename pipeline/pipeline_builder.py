from configparser import ConfigParser

def build(name):
    parser = ConfigParser()
    parser.read('../config.ini')
    config = parser._sections
    pconfig = config['pipeline.%s' % name]
    pipeline = [plugin.strip() for plugin in pconfig['pipeline'].split('|')]
    del pconfig['pipeline']

    ret = []
    for plugin in pipeline:
        plugin_conf = None
        plugin_name = plugin.split('.')[-1]
        config_section = 'plugin.%s' % plugin_name

        if config_section in config:
            plugin_conf = dict(config[config_section])

        # pipeline overrides of plugin conf
        for key, value in pconfig.items():
            target_plugin_name, target_plugin_key = key.split(".")
            if target_plugin_name == plugin_name.lower():
                plugin_conf[target_plugin_key] = value

        ret.append({'plugin': plugin, 'config': plugin_conf})

    return ret
