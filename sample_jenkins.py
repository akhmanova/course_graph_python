import jenkins
from graph import Graph
import json

def get_all_paths():
    server = jenkins.Jenkins('http://localhost:8080')
    version = server.get_version()
    jobs = server.get_jobs(folder_depth=10)
    temp_jobs = []
    list_adj = []
    list_jobs = []
    reverse_list = []
    for job in jobs:
        name = job['name']
        url = job['url']

        prev = ''
        temp_list = []
        for i in range(len(url)):
            if url[i] is '/':
                temp_name = ''
                i += 1
                while i < len(url) and url[i] != '/':
                    temp_name += url[i]
                    i += 1
                if len(temp_name) > 0:
                    temp_list.append(temp_name)
        if len(temp_list) > 3:
            list_adj.append((temp_list[-3], temp_list[-1]))
            reverse_list.append((temp_list[-3], temp_list[-1]))
            if temp_list[-3] not in list_jobs:
                list_jobs.append(temp_list[-3])
            if temp_list[-1] not in list_jobs:
                list_jobs.append(temp_list[-1])
    jen_graph = Graph()
    v_name = {}
    v_idx = {}
    for i, j in enumerate(reverse_list):
        v_name[j] = i
        v_idx[i] = j
    jen_graph.set_v_name_to_idx(v_name)
    jen_graph.set_v_idx_to_name(v_idx)
    for i in list_adj:
        jen_graph.add_edge(i)

    reverse_graph = Graph()
    reverse_graph.set_v_name_to_idx(v_name)
    for i in reverse_list:
        reverse_graph.add_edge(i)

    result_path = {}
    for i in list_jobs:
        result_path[i] = reverse_graph.find_path(i)
    print('REVERSE', reverse_list)
    print(reverse_graph.get_v_idx_to_name())
    return result_path


def get_cur_path(path):
    all_paths = get_all_paths()
    result = []
    if path in all_paths:
        result = all_paths[path]
    return result

