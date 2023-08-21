<<<<<<< HEAD
#!/usr/local/bin/python3
import sys

# file reading
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
file2 = open(sys.argv[2], 'w')

#----------------------------------
#declare of class Graph
#Citation: https://www.pythonpool.com/kruskals-algorithm-python/ 
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []     #list of edges and weights goes here

    # conencts vertices u and v with weight w, adds to graph
    def addEdge(self, u, v, w, l):
        self.graph.append([u, v, w, l])     

    # Search function to find set of an element 
    def discover(self, p, x):
        if p[x] == x:   # parent list
            return x
        else:
            return self.discover(p, p[x])

    # union by rank 
    # connects smaller rank tree to the root of high rank tree
    def uni(self, p, r, x, y):
        if r[x] == r[y]:
            p[y] = x
            r[x] += 1
        elif r[x] > r[y]:
            p[y] = x
        elif r[x] < r[y]:
            p[x] = y

    # Kruskal algorithm
    def kruskal_algo(self):
        res, p, r = ([] for i in range(3))    # result, parent, rank
        i, res_index = 0, 0
        # sort edges first by increasing weights
        self.graph = sorted(self.graph, key=lambda item: item[2])
        # create length V sets of elements, append it to parent list
        # and fill in zeros for the rank
        for item in range(self.vertices):
            r.append(0)
            p.append(item)
        #run a loop until our index is out of bounds with the length 
        # of V-vertices. Choose smallest edge and increment counter i
        while res_index < self.vertices - 1:
            # make graph using edges, weights, and labels
            u, v, w, l = self.graph[i]
            y = self.discover(p, v-1)
            i += 1
            x = self.discover(p, u-1)
            
            # if the edges are equal (cycle), disregard the edge
            # else append to result list
            if x == y:
                continue
            else:
                res.append([u, v, w, l])
                res_index += 1
                self.uni(p, r, x, y)
        # return list res
        return res

#----------------------------------

# counter for line number, index start at -1
line_num = -1

# create a graph from reading the first
# number of line 1, i = number of vertices
for i in Lines:
    G = Graph(int(i))
    break

# add edges and weights for the rest of the file
for i in Lines:
    x = i.split()
    if line_num >= 1:
        G.addEdge(int(x[0]), int(x[1]), int(x[2]), line_num)
    line_num+=1

# call the kruskal algo and you're done
res = G.kruskal_algo()
total_weight = 0

# from the list res, print lables, edges, weights, and total weight in outfile
for u, v, w, l in res:
    total_weight += w
    file2.write("%4d: (%d, %d) %.1f\n" % (l, u, v, w))
file2.write("Total Weight = %.2f" % total_weight)

# close files
file1.close()
file2.close()
=======
#!/usr/local/bin/python3
import sys

# file reading
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
file2 = open(sys.argv[2], 'w')

#----------------------------------
#declare of class Graph
#Citation: https://www.pythonpool.com/kruskals-algorithm-python/ 
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []     #list of edges and weights goes here

    # conencts vertices u and v with weight w, adds to graph
    def addEdge(self, u, v, w, l):
        self.graph.append([u, v, w, l])     

    # Search function to find set of an element 
    def discover(self, p, x):
        if p[x] == x:   # parent list
            return x
        else:
            return self.discover(p, p[x])

    # union by rank 
    # connects smaller rank tree to the root of high rank tree
    def uni(self, p, r, x, y):
        if r[x] == r[y]:
            p[y] = x
            r[x] += 1
        elif r[x] > r[y]:
            p[y] = x
        elif r[x] < r[y]:
            p[x] = y

    # Kruskal algorithm
    def kruskal_algo(self):
        res, p, r = ([] for i in range(3))    # result, parent, rank
        i, res_index = 0, 0
        # sort edges first by increasing weights
        self.graph = sorted(self.graph, key=lambda item: item[2])
        # create length V sets of elements, append it to parent list
        # and fill in zeros for the rank
        for item in range(self.vertices):
            r.append(0)
            p.append(item)
        #run a loop until our index is out of bounds with the length 
        # of V-vertices. Choose smallest edge and increment counter i
        while res_index < self.vertices - 1:
            # make graph using edges, weights, and labels
            u, v, w, l = self.graph[i]
            y = self.discover(p, v-1)
            i += 1
            x = self.discover(p, u-1)
            
            # if the edges are equal (cycle), disregard the edge
            # else append to result list
            if x == y:
                continue
            else:
                res.append([u, v, w, l])
                res_index += 1
                self.uni(p, r, x, y)
        # return list res
        return res

#----------------------------------

# counter for line number, index start at -1
line_num = -1

# create a graph from reading the first
# number of line 1, i = number of vertices
for i in Lines:
    G = Graph(int(i))
    break

# add edges and weights for the rest of the file
for i in Lines:
    x = i.split()
    if line_num >= 1:
        G.addEdge(int(x[0]), int(x[1]), int(x[2]), line_num)
    line_num+=1

# call the kruskal algo and you're done
res = G.kruskal_algo()
total_weight = 0

# from the list res, print lables, edges, weights, and total weight in outfile
for u, v, w, l in res:
    total_weight += w
    file2.write("%4d: (%d, %d) %.1f\n" % (l, u, v, w))
file2.write("Total Weight = %.2f" % total_weight)

# close files
file1.close()
file2.close()
>>>>>>> 081999db5a546f9d44599753086b6ed7a31d7a38
