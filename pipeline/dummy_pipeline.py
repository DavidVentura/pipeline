#!/usr/bin/env python3
from mypipeline import Pipeline
p = Pipeline(['sources.dummy.Dummy', 'filters.dummy.Dummy', 'maps.dummy.Dummy', 'sinks.dummy.Dummy'])
