#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from igraph import *
from p6_helpers import *
DATADIR = "redes/"

def main():
	g = Graph.Read_GML(DATADIR + "correos.gml")
	nodeCount = len(g.vs)
	edgeCount = len(g.es)

	# Average degree
	degrees = g.degree()
	degreeSum = reduce(lambda x,y: x+y, degrees)
	averageDegree = degreeSum/len(degrees)
	
	# Getting data from original graph
	cores = getCores(g)
	modularity = getModularity(g)
	assortativity = g.assortativity_degree()
	printCores(cores, 'Red Original')
	print "Modularidad\t" + str(modularity)
	print "Asortatividad\t" + str(assortativity)

	# Original rewired
	g.rewire(edgeCount*2)
	cores = getCores(g)
	modularity = getModularity(g)
	assortativity = g.assortativity_degree()
	printCores(cores, 'Red Recableada')
	print "Modularidad\t" + str(modularity)
	print "Asortatividad\t" + str(assortativity)

if __name__ == "__main__":
  main()