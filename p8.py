import igraph
import random
from igraph import *

erdos=Graph.Erdos_Renyi(80, p=0.2, directed=False, loops=False)
b1=erdos.vs.select(lambda vertex: vertex.index < 40)
b2=erdos.vs.select(lambda vertex: vertex.index >= 40)
c1=erdos.vs.select(lambda vertex: vertex.index < 20 or (vertex.index >= 40 and vertex.index <60))
c2=erdos.vs.select(lambda vertex: (vertex.index >= 20 and vertex.index <40) or vertex.index >= 60)
nuevos = []
p=0.1
for i in range(len(erdos.es)):
	rndm=random.randint(0,1)
	if len(b1.select(lambda vertex: vertex.index == erdos.get_edgelist()[i][0])) and len(b1.select(lambda vertex: vertex.index == erdos.get_edgelist()[i][1])):
		if rndm>0.5:
			nuevos.append((erdos.get_edgelist()[i][0],erdos.get_edgelist()[i][1]))
		else:
			nuevos.append((erdos.get_edgelist()[i][1],erdos.get_edgelist()[i][0]))
	elif len(b2.select(lambda vertex: vertex.index == erdos.get_edgelist()[i][0])) and len(b2.select(lambda vertex: vertex.index == erdos.get_edgelist()[i][1])):
		if rndm>0.5:
			nuevos.append((erdos.get_edgelist()[i][0],erdos.get_edgelist()[i][1]))
		else:
			nuevos.append((erdos.get_edgelist()[i][1],erdos.get_edgelist()[i][0]))
	else:
		if len(b1.select(lambda vertex: vertex.index == erdos.get_edgelist()[i][0])):
			if rndm>=p:
				nuevos.append((erdos.get_edgelist()[i][0],erdos.get_edgelist()[i][1]))
			else:
				nuevos.append((erdos.get_edgelist()[i][1],erdos.get_edgelist()[i][0]))
		else:
			if rndm<p:
				nuevos.append((erdos.get_edgelist()[i][0],erdos.get_edgelist()[i][1]))
			else:
				nuevos.append((erdos.get_edgelist()[i][1],erdos.get_edgelist()[i][0]))
summary(erdos)

erdos.es.delete()
summary(erdos)

erdos.add_edges(nuevos)
summary(erdos)

erdos=erdos.as_directed()
summary(erdos)

erdos.delete_edges(nuevos)
summary(erdos)
layout=erdos.layout("kk")
plot(erdos,layout=layout)