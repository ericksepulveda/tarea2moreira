import igraph
import random
from igraph import *

delfines=Graph.Read_GML("redes/delfines.gml")
total = len(delfines.vs)
giant1 = len(delfines.components().giant().vs)
giant2 = giant1
while giant2>giant1/2:
	delfines.delete_vertices(delfines.vs.select(_betweenness =  max(delfines.betweenness()))[0].index)
	giant2 = len(delfines.components().giant().vs)
print 100-100*len(delfines.vs)/float(total)