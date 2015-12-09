#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from igraph import *
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
	cores = getCores(g)
	printCores(cores, 'Red Original')

	# Original rewired
	g.rewire(edgeCount*2)
	cores = getCores(g)
	printCores(cores, 'Red Recableada')

	# Erdös-Renyi
	g = Graph.Erdos_Renyi(nodeCount, m=edgeCount)
	cores = getCores(g)
	printCores(cores, 'Erdös-Renyi')

	# Barabási-Albert
	g = Graph.Barabasi(nodeCount, m=averageDegree/2)
	cores = getCores(g)
	printCores(cores, 'Barabási-Albert')

def printCores(cores, title):
	print title
	print "k-core\t\tnodos\taristas"
	for i in range(len(cores)):
		print str(i) + "-core: \t" + str(cores[i]["vcount"]) + "\t" + str(cores[i]["ecount"])

def getData(core):
	core = dict([("graph", core)])
	core["vcount"] = len(core["graph"].vs)
	core["ecount"] = len(core["graph"].es)
	return core

def getCores(graph):
	cores = {}
	cores[0] = getData(graph.k_core(0))
	i = 0
	while cores[i]["vcount"] > 0:
		i+=1
		cores[i] = getData(graph.k_core(i))
	del cores[i]
	return cores

if __name__ == "__main__":
  main()