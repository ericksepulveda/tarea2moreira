#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from igraph import *
from p6_helpers import *
DATADIR = "redes/"

def main():
	g = Graph.Read_GML(DATADIR + "roget.gml")
	nodeCount = len(g.vs)
	edgeCount = len(g.es)

	# Average degree
	degrees = g.degree()
	degreeSum = reduce(lambda x,y: x+y, degrees)
	averageDegree = degreeSum/len(degrees)
	
	# Getting data from original graph
	p6magic(g, 'Red Original')

	# Original rewired
	g.rewire(edgeCount*2)
	p6magic(g, 'Red Recableada')

	# Erdös-Renyi
	g = Graph.Erdos_Renyi(nodeCount, m=edgeCount)
	p6magic(g, 'Erdös-Renyi')

	# Barabási-Albert
	g = Graph.Barabasi(nodeCount, m=averageDegree/2)
	p6magic(g, 'Barabási-Albert')

def p6magic(graph, name):
	cores = getCores(graph)
	modularity = getModularity(graph)
	assortativity = graph.assortativity_degree()
	printCores(cores, name)
	print "Modularidad\t" + str(modularity)
	print "Asortatividad\t" + str(assortativity)

if __name__ == "__main__":
  main()