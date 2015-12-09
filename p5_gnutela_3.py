import igraph
import random
from igraph import *

gnutella=Graph.Read_GML("redes/gnutella.gml")
total = len(gnutella.vs)
giant1 = len(gnutella.components().giant().vs)
giant2 = giant1
while giant2>giant1/2:
	gnutella.delete_vertices(gnutella.vs.select(_betweenness =  max(gnutella.betweenness()))[0].index)
	giant2 = len(gnutella.components().giant().vs)
print 100-100*len(gnutella.vs)/float(total)