from sample_jenkins import *
import json

print(json.dumps(get_all_paths(), indent=4, sort_keys=True))

print(get_all_paths())
assert ['test_prod', 'test_prod_serv_1'], get_cur_path('test_prod_serv_1')
assert ['dev', 'server1'], get_cur_path('server1')
assert ['dev'], get_cur_path('dev')