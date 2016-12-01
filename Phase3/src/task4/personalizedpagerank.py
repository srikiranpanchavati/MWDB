import networkx as nx
import numpy as np
import operator


def find_personalized_page_rank(graph, damping_factor=0.85, personalized_vector=None):
    M = nx.to_numpy_matrix(graph)
    print M
    outlinks_list = list(graph.out_degree_iter())
    nodes_list = graph.nodes()
    print outlinks_list
    len_of_matrix = len(M)
    for i in range(len_of_matrix):
        curr_sum = M[i].sum()
        no_of_outlinks = outlinks_list[i][1]
        if curr_sum != 0:
            for j in range(len_of_matrix):
                M[i, j] = np.round(float(M.item(i, j)) * damping_factor / float(curr_sum * no_of_outlinks), 4)
    print M
    M = M.T
    print M
    no_of_seeds = len(personalized_vector)
    for i in personalized_vector:
        if i in nodes_list:
            get_index = nodes_list.index(i)
            print get_index
            for j in range(len_of_matrix):
                M[get_index, j] = M.item(get_index, j) + (1 - damping_factor) / float(no_of_seeds * len_of_matrix)
    print M
    V = np.matrix(np.repeat(1.0 / len_of_matrix, len_of_matrix)).T
    print V
    print M
    print M * V
    iterations = 1
    while sum(abs(M * V - V)) > 0.001:
        iterations += 1
        V = M * V
    print iterations
    rank_vector = M * V
    rank_dict = {}
    for i in range(len_of_matrix):
        rank_dict[nodes_list[i]] = rank_vector.item(i, 0)
    sorted_ranks = sorted(rank_dict.items(), key=operator.itemgetter(1), reverse=True)
    print sorted_ranks
    return sorted_ranks


def visualize(ranks, videos_path, m):
    if m > len(ranks):
        print "invalid m value"
    else:
        rank_list = list(ranks)
        for i in range(m):
            print "................................"
            #print rank_list[i]
            videoname = (rank_list[i][0]).split(".mp4")[0] + ".mp4"
            framenumber = (rank_list[i][0]).split(".mp4")[1]
            print "Video name: " + videoname
            print "Frame number: " + framenumber
            print "Rank: " + str(rank_list[i][1])