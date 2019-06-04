from graph import Graph

g = Graph(n=2, m=2, adj=[(0, 1), (1,0)])
print(g.get_n())
g.set_n(3)
print( g.get_n())
print (g.set_n(3))
print (g.set_m(2))
print (g.set_edges([(0, 4), (1,0), (2, 3)]))
print( g.get_n())
print( g.get_m())
print (len((0, 1)))
print( g.get_n())
print( g.get_m())
print (g.get_v_idx_to_name())
print(g.delete_edge((1, 0)))
print(g.get_edges())