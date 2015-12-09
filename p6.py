import sys
from igraph import *
DATADIR = "redes/"

g = Graph.Read_GML(DATADIR + "roget.gml")

cores = {}

cores[1] = dict([("graph", g.k_core(1))])
cores[1]["vcount"] = len(cores[1]["graph"].vs)
cores[1]["ecount"] = len(cores[1]["graph"].es)

i = 1

while cores[i]["vcount"] > 0:
	i+=1
	cores[i] = dict([("graph", g.k_core(i))])
	cores[i]["vcount"] = len(cores[i]["graph"].vs)
	cores[i]["ecount"] = len(cores[i]["graph"].es)

del cores[i]

for i in range(len(cores)):
	print 