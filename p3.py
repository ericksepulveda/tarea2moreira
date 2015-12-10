import igraph
from igraph import *

g=Graph()
g.add_vertices(6)
g.add_edges([(0,1),(0,2),(1,2),(2,3),(3,4),(3,5),(4,5)])
g.vs["id"]=[0,1,2,3,4,5]
layout=g.layout("kk")
g.vs["label"]=g.vs["id"]
plot(g,layout=layout)