import networkx as nx


def helper(graph_file):
    # method used to construct transition probability matrix
    G = nx.DiGraph()
    for line in open(graph_file):
        parameters = line.split(',')
        print parameters
        src = parameters[0] + parameters[1]
        dest = parameters[2] + parameters[3]
        sim = parameters[4]
        print src, dest, sim
        G.add_edge(src, dest, weight=sim)
    return G

#helper("D:\\Education\\ASU\\MWD\\phase3\\samples\\sample.txt")
