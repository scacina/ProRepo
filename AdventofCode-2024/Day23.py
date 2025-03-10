import collections
import functools
# Global variable
import networkx as nx
from itertools import combinations
G_INPUTFILENAME = "Day23.txt"




def create_bidirectional_graph(edges):
    """
    Create a bidirectional graph from a list of edges.

    Parameters:
    edges (list of tuples): List of tuples where each tuple represents an edge (start_node, end_node).

    Returns:
    nx.Graph: A bidirectional graph.
    """
    # Create an empty graph
    graph = nx.Graph()

    # Add edges to the graph
    graph.add_edges_from(edges)

    return graph

def findtriangle(graphin: nx.Graph):
    res = set()
    snodes = set(graphin.nodes())
    for anode in snodes:
        for nb1 in graphin.neighbors(anode):
            for nb2 in graphin.neighbors(nb1):
                if anode in graphin.neighbors(nb2) and len(set([anode, nb1, nb2])) == 3 and 't' in ([anode[0], nb1[0], nb2[0]]):
                    res.add("".join(sorted([anode, nb1, nb2])))
    return len(res)



def find_trianglesandpassword(graph):
    clique = max(nx.find_cliques(graph), key = len)
    clique.sort()
    lsstr = ",".join(clique)
    return lsstr


def solvepart2(matrix):
    # Step 1: Prepare the grid with sequences
    res = 0
    print("part 2 ended", res)
    return res

def solvepart1(matrix):
    res = 0
    edges = []
    for edge in matrix:
        edges.append(edge.split("-"))

    gr = create_bidirectional_graph(edges)

    print(findtriangle(gr))
    res = find_trianglesandpassword(gr)
    print(res)
    return res

# main...
def main():
    array = []
    with open(G_INPUTFILENAME) as f:
        for line in f:  # read rest of lines
            line = line.strip()
            line = line.strip("\n")
            line = line.strip("\r")
            line = line.strip()
            if line:
                array.append(line)
    solvepart1(array)
    solvepart2(array)


if __name__ == "__main__":
    main()
