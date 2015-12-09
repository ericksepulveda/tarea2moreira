import igraph
import random
from igraph import *

erdos2=Graph.Erdos_Renyi(62, m=159, directed=False, loops=False)
total = len(erdos2.vs)
giant1 = len(erdos2.components().giant().vs)
giant2 = giant1
while giant2>giant1/2:
	erdos2.delete_vertices(erdos2.vs.select(random.randint(0, giant2-1)))
	giant2 = len(erdos2.components().giant().vs)
print 100-100*len(erdos2.vs)/float(total)