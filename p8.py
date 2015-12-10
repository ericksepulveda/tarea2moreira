#!/usr/bin/env python
# -*- coding: utf-8 -*-
import igraph
import random
from igraph import *

erdos=Graph.Erdos_Renyi(80, p=0.2, directed=False, loops=False)
b1=erdos.vs.select(lambda vertex: vertex.index < 40)
b2=erdos.vs.select(lambda vertex: vertex.index >= 40)

for i in range(0,len(erdos.vs)):
	erdos.vs[i]["id"] = i
	if i<40:
		erdos.vs[i]["partition"] = "b1"
	else:
		erdos.vs[i]["partition"] = "b2"

c1=erdos.vs.select(lambda vertex: vertex.index < 20 or (vertex.index >= 40 and vertex.index <60))
c2=erdos.vs.select(lambda vertex: (vertex.index >= 20 and vertex.index <40) or vertex.index >= 60)
nuevos = []

for p in range(0,11,1) :
	print p
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
				if rndm<=(p/10):
					nuevos.append((erdos.get_edgelist()[i][0],erdos.get_edgelist()[i][1]))
				else:
					nuevos.append((erdos.get_edgelist()[i][1],erdos.get_edgelist()[i][0]))
			else:
				if rndm>(p/10):
					nuevos.append((erdos.get_edgelist()[i][0],erdos.get_edgelist()[i][1]))
				else:
					nuevos.append((erdos.get_edgelist()[i][1],erdos.get_edgelist()[i][0]))
	erdos.es.delete()
	erdos.add_edges(nuevos)
	erdos=erdos.as_directed()
	erdos.delete_edges(nuevos)

	layout=erdos.layout("kk")
	erdos.vs["label"] = erdos.vs["id"]
	color_dict = {"b1": "blue", "b2": "red"}
	erdos.vs["color"] = [color_dict[partition] for partition in erdos.vs["partition"]]
	plot(erdos,layout=layout)
	
	erdos=erdos.as_undirected()
	
	nuevos = []