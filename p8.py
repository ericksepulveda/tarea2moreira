import igraph
from igraph import *

erdos=Graph.Erdos_Renyi(80, p=0.2, directed=False, loops=False)
b1=erdos.vs.select(lambda vertex: vertex.index < 40)	
b2=erdos.vs.select(lambda vertex: vertex.index >= 40)
c1=erdos.vs.select(lambda vertex: vertex.index < 20 or (vertex.index >= 40 and vertex.index <60))
c2=erdos.vs.select(lambda vertex: (vertex.index >= 20 and vertex.index <40) or vertex.index >= 60)

for i in range(len(erdos.es)):
	erdos.get_edgelist()[i]