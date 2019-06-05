from sample_jenkins import *
import json

print(json.dumps(get_all_paths(), indent=4, sort_keys=True))

