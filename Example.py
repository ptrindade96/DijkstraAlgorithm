# Import the module containing the Dijkstra Algorithm
from Dijkstra import Graph
from Dijkstra import edges_from_file

# Define a list containing the Graph edges. Edges are tuples in the form:
# (start_node,end_node,cost)
edges = [   ("A","2",10),
            ("2","3",5),
            ("3","5",2),
            ("2","5",4),
            ("A","3",6)     ]

# Another possibility is to import the edges from a file, in a specific format.
# An example file with edges is presented named Edges.txt. You can create your
# own file with edges, as long as it follows the same format, and just replace
# the name in the function below with the name of your file.
edges = edges_from_file("Edges.txt")
print edges

# Create the graph
g = Graph(edges)

###### Obtain the costs from a node to all others
###############################################################################
source_node = "A"
g.dijkstra_all(source_node)

###### Obtain the shortest path from a node to another
###############################################################################
source_node = "A"
goal_node = "5"
cost,path = g.dijkstra(source_node,goal_node)

# Present the results
string = ""
for p in path:
    string = string + repr(p) + " -> "
string = string[:-3]
print "....  Shortest path from " + str(source_node) + " to " + str(goal_node) + "  ...."
print "Cost = " + repr(cost) + "\t" + string
