# Pipeline

attempt at a plugin-based pipeline for data.

The 'plugins' have to be in one of these categories:

* Sources: Should generate some kind of data
* Filters: Should decide if the data from a source should be passed onwards or cancelled.
* Maps: Should map the source data to whatever is wanted in the output.
  * Should take many inputs and only modify those it has to, while passing the rest to the output
* Sinks: Output data from the pipeline to something.


Special? cases:
* 'tee' map: data -> translate(en, es)


# Desired examples

config.ini
```ini
[main]
    grafana_url = http://your_stuff:8086/write?db=%s
    driver = /home/you/chromedriver/chromedriver
    telegram_bot_id = ******************************************
    telegram_chat_id = **

[pipelines]
    [gvb]
    pipeline = [gvb, tee, translate_eng, to_markdown, telegram]
    
    # gvb (item): no input, 1 output
    # tee: 1 input, 2 outputs
    # translate_eng:
    
    [weather]
    pipeline = [weather, to_markdown, telegram]
    
    [printer]
    pipeline = [printer_mqtt, filter_printer_states, to_markdown, telegram]

[plugins]
    [gvb]
    ApiKey = ************************************
    LINES_INTERESTED = [50, 53]
    
    [abn]
    account = 111111111
    card = 111
    pin = 11111
    grafana_db = scripts_data
    
    [weather]
    API_KEY = ******************************
    CITY_ID = 2759794
    #amsterdam
    
    [filter_printer_states]
    progress = [1, 25, 50, 75, 100]
    
    [translate_eng]
    translate_id = 0
```


# Setup
```
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

# Dummy usage
```
Got [Hello world] from source Dummy
Passing [Hello world] to filter Dummy => Passed
Processing [Hello world] in map Dummy => True
Putting [True] in sink Dummy
[From dummy sink] True
```
