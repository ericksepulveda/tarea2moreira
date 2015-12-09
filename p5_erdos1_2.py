import igraph
import random
from igraph import *

erdos1=Graph.Erdos_Renyi(795, m=852, directed=False, loops=False)
total = len(erdos1.vs)
giant1 = len(erdos1.components().giant().vs)
giant2 = giant1
while giant2>giant1/2:
	erdos1.delete_vertices(erdos1.vs.select(_degree = erdos1.maxdegree())[0].index)
	giant2 = len(erdos1.components().giant().vs)
print 100-100*len(erdos1.vs)/float(total)