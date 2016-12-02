import networkx as nx


def helper(graph_file):
    # method used to construct directed graph
    G = nx.DiGraph()
    for line in open(graph_file):
        parameters = line.split(',')
        src = parameters[0] + parameters[1]
        dest = parameters[2] + parameters[3]
        sim = parameters[4]
        G.add_edge(src, dest, weight=sim)
    return G