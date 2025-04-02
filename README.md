# A Client for Data360 API

## Purpose of this library

Allow to easily use Data360 API programmatically. 

This is very usefull in some contexts like: 
- managing and versionning meta-models, configurations, etc. 
- managing content from IT side (ex: Data quality testing, metadata development, harvesting scripts, etc.)
- etc. 

## Note on Model: loose or not

Currently there is a "model.py" module and a "loose-model.py" module.  
The loose-model is just creating objects with the parameters as they're retrived from the API when calling the "GET" method.  
It's only useful to keep type-hints, but it has many downsides such as type validation, autocompletion, etc. 
In an ideal world, we would use "model.py" which provide immutable dataclasses together with mappings methods to map from and to the Json logic. 
Though reverse engineering this takes a lot of time as model is generic, and not always consistent, so in the meantime, we just started by trusting Precisely's API. 
