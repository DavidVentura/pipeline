# Pipeline

attempt at a plugin-based pipeline for data.

The 'plugins' have to be in one of these categories:

* Sources: Should generate some kind of data
* Filters: Should decide if the data from a source should be passed onwards or cancelled.
* Maps: Should map the source data to whatever is wanted in the output.
* Sinks: Output data from the pipeline to something.


Special? cases:
* 'tee' map: data -> translate(en, es)


