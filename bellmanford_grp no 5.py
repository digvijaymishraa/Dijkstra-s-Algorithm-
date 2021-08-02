import time

tic = time.perf_counter()

def bellmanFord(edges, source, N):


	distance = [100000000] * N
	distance[source] = 0

	
	for k in range(N - 1):

		for (u, v, w) in points:
			if distance[u] + w < distance[v]:
				distance[v] = distance[u] + w

	for i in range(1, N, 1):
        
		print("The distance of vertex", i, "from the source is", distance[i], end='.\n')

toc = time.perf_counter()
# vertices given 0=A , 1=B , 2=C ,3=D 
#(starting point ,stop point ,weight(distance between start stop point))
points = [(0, 1, 7), (0, 2, 12), (1, 2, 3),(2, 1, 3), (1, 3, 10),(2, 3, 4)]
N = 4                    #(total number of number of vertices)
source = 0               #starting point
bellmanFord(points, source, N)

print(f'calculation took {1000000*(toc-tic)} micro seconds ')  