#!/usr/bin/env python3
from mypipeline import Pipeline
import pipeline_builder

pipeline = pipeline_builder.build('gvb')
p = Pipeline(pipeline)
