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

def getModularity(graph):
	return graph.community_fastgreedy().as_clustering().modularity