from numpy import *
from scipy import linalg as LA
from igraph import *

def main():
	adjacency = [[0,1,1,0,0,0], 
							[1,0,1,0,0,0], 
							[1,1,0,1,0,0], 
							[0,0,1,0,1,1], 
							[0,0,0,1,0,1], 
							[0,0,0,1,1,0]]
	edges = edgesFromMatrix(adjacency)

	degrees = [[0 for i in range(6)] for i in range(6)]
	for i in range(6):
		degrees[i][i] = reduce(lambda x,y: x+y, adjacency[i])

	adjacency = mat(adjacency)
	degrees = mat(degrees)

	laplace = degrees-adjacency

	e_vals, e_vecs = LA.eig(laplace)

	e_vecs = e_vecs.swapaxes(0,1) # e_vecs[i] will now take column i

	smallest = e_vals[0]
	fiedler = e_vals[0]

	for i in range(1, len(e_vals)):
		if e_vals[i] < smallest:
			fiedler = smallest
			smallest = e_vals[i]
		elif e_vals[i] < fiedler:
			fiedler = e_vals[i]

	index = findIndex(e_vals, fiedler)
	fiedler_vector = e_vecs[index]
	
	print "Valor de Fiedler\t" + str(fiedler)
	print "Vector asociado\t" + str(fiedler_vector)

	g = Graph(edges)
	for i in range(len(g.vs)):
		if fiedler_vector[i] <= 0:
			g.vs[i]["color"] = "blue"
	layout = g.layout("kk")
	plot(g, layout=layout)

def findIndex(arr, value):
	for i in range(len(arr)):
		if arr[i] == value:
			return i
	return -1

def edgesFromMatrix(matrix):
	edges = []
	for i in range(len(matrix)):
		for j in range(i+1, len(matrix)):
			if matrix[i][j] == 1:
				edges.append([i,j])
	return edges

if __name__ == "__main__":
  main()