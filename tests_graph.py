from graph import Graph
from copy import deepcopy

###################################################

g = Graph()
g.set_n(1)
g.add_edge(('loop', 'loop'))
assert 1, g.get_m()
g.add_edge(('loop', 'loop'))
assert 1, g.get_m()

g.add_edge(('loop', 'hulahoop'))
assert 2, g.get_n()
assert {'loop': 1, 'hulahoop': 2}, g.get_v_name_to_idx()


###################################################
# Copy
gg = Graph(kwargs={
    'original_graph': deepcopy(g)
}
)
assert [
    gg.get_v_name_to_idx(),
    gg.get_n(),
    gg.get_m(),
    gg.get_v_idx_to_name(),
    gg.get_edges(),
    gg.get_adj(),
    gg.get_oriented()],  \
[{'loop': 1, 'hulahoop': 2}, 3, 2, {1: 'loop', 2: 'hulahoop'}, [(1, 1), (1, 2)], [], False]


###################################################
# Create
gg = Graph(kwargs={
    'oriented': True,
    'edges': [
        ('What are you doing?', 'I am reading an interesting book. I love read.'),
        ('I am reading an interesting book. I love read.', 'How long have you been reading this?'),
        ( 'How long have you been reading this?', 'I have been reading it for two days.'),
        ('How many pages have you read?' , '30' ),
        ( 'Where is your brother?', 'He is playing soccer.'),
        ( 'He is playing soccer.', 'Does he often play soccer?'),
        ( 'Does he often play soccer?', 'Two times a week. '),
        ( 'Two times a week. ', 'I want to talk to him.'),
        ( 'I want to talk to him.', 'he has been already playing for two hours. I think, he will come soon.'),
        ( 'I like learning foreign languages. Now I am learning  irregular English verbs.', 'How many verbs has you  already learned?'),
        ( 'How many verbs has you  already learned?', '40'),
        ( '40', 'How long have you been studying English?'),
        ( 'How long have you been studying English?', 'I have been studying English since last summer.')
    ]
})
assert [
    (0, 3), (3, 4), (4, 5),
    (6, 7), (8, 9), (9, 10),
    (10, 11), (11, 12),
    (12, 13), (14, 15),
    (15, 16), (16, 17), (17, 18)
], gg.get_edges()
assert 19, gg.get_n()

assert True, gg.add_vertex('Some phrases')
assert 20, gg.get_n()
assert 13, gg.get_m()
gg.delete_vertex(0)
assert 12, gg.get_m()
gg.delete_vertex(0)
assert 12, gg.get_m()
gg.delete_edge((8, 9))
assert [
    (3, 4), (4, 5), (6, 7),
    (9, 10), (10, 11), (11, 12),
    (12, 13), (14, 15), (15, 16),
    (16, 17), (17, 18)
], gg.get_edges()


