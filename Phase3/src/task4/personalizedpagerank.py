import networkx as nx
import numpy as np
import operator
import cv2
import os


def find_personalized_page_rank(graph, damping_factor=0.85, personalized_vector=None):
    # method used to calculate personalized page rank algorithm to output the most significant frames
    # generated graph is converted to transition probability matrix
    M = nx.to_numpy_matrix(graph)
    outlinks_list = list(graph.out_degree_iter())
    nodes_list = graph.nodes()
    len_of_matrix = len(M)
    for i in range(len_of_matrix):
        curr_sum = M[i].sum()
        no_of_outlinks = outlinks_list[i][1]
        if curr_sum != 0:
            for j in range(len_of_matrix):
                M[i, j] = np.round(float(M.item(i, j) * damping_factor) / float(curr_sum * no_of_outlinks), 4)
    M = M.T
    no_of_seeds = len(personalized_vector)
    for i in personalized_vector:
        if i in nodes_list:
            get_index = nodes_list.index(i)
            #print get_index
            for j in range(len_of_matrix):
                M[get_index, j] = M.item(get_index, j) + (1 - damping_factor) / float(no_of_seeds)
    #print M
    V = np.matrix(np.repeat(1.0 / len_of_matrix, len_of_matrix)).T
    iterations = 0
    prev = V
    while iterations < 300:
        curr = M * V
        if np.array_equal(curr, prev):
            break
        iterations += 1
    rank_vector = curr
    rank_dict = {}
    for i in range(len_of_matrix):
        rank_dict[nodes_list[i]] = rank_vector.item(i, 0)
    sorted_ranks = sorted(rank_dict.items(), key=operator.itemgetter(1), reverse=True)
    #print sorted_ranks
    return sorted_ranks


def visualize(ranks, videos_path, m):
    if m > len(ranks):
        print "invalid m value"
    else:
        rank_list = list(ranks)
        for i in range(m):
            print "................................"
            video_name = (rank_list[i][0]).split(".mp4")[0] + ".mp4"
            frame_number = (rank_list[i][0]).split(".mp4")[1]
            print "Video name: " + video_name
            print "Frame number: " + frame_number
            print "Rank: " + str(rank_list[i][1])
            out_dir = videos_path + "//" + "output_frames"

            if not os.path.exists(out_dir):
                os.makedirs(out_dir)

            full_filename = videos_path + "\\" + video_name
            save_name = out_dir + "//" + video_name + "_" + frame_number + ".jpeg"
            capture = cv2.VideoCapture(full_filename)
            frame = None
            count = 1
            while capture.isOpened():
                is_read, frame = capture.read()
                if not is_read:
                    break
                if count == int(frame_number):
                    break
                count += 1

            cv2.imshow(video_name + "_" + frame_number + ".jpeg", frame)
            cv2.imwrite(save_name, frame)
            cv2.waitKey(1000)
            capture.release()
            cv2.destroyAllWindows()