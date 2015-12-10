import sys
from igraph import *
DATADIR = "redes/"

g = Graph.Read_GML(DATADIR + "redchica.gml")

for i in range(len(g.vs)):
	g.vs[i]["label"] = "n: v" + str(i+1) + "\n"

	default = len(sys.argv) < 2
	if default or 'degree' in sys.argv:
		degree = g.vs[i].degree()
		g.vs[i]["label"] += "d: " + str(degree) + "\n"	
	if default or 'betweenness' in sys.argv:
		betweenness = g.vs[i].betweenness()	
		g.vs[i]["label"] += "b: " + str(betweenness) + "\n"
	if default or 'pagerank' in sys.argv:
		pagerank = round(g.vs[i].pagerank(), 2)
		g.vs[i]["label"] += "p: " + str(pagerank)

g.es["width"] = 1

g.vs["label_color"] = "blue"
g.vs["label_size"] = 20
g.vs["label_dist"] = 0
g.vs["color"] = "white"
g.vs["size"] = 100 if len(sys.argv) < 3 and len(sys.argv) > 1 else 120

layout = g.layout("kk")

plot(g, layout = layout, margin = 75)