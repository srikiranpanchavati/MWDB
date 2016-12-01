import networkx as nx
import numpy as np
from networkx.exception import NetworkXError
from Phase3.src.utils.Pagerank_helper import Helper
import os
import cv2


def calc_pagerank(D, weight='weight'):

    alpha=0.85
    tol=1.0e-6


    W = nx.stochastic_graph(D, weight=weight)
    N = W.number_of_nodes()

    x = dict.fromkeys(W, 1.0 / N)
    dangling_weights = x
    dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0]

    # power iteration: make up to 300 iterations
    for _ in range(300):
        xlast = x
        x = dict.fromkeys(xlast.keys(), 0)
        danglesum = alpha * sum(xlast[n] for n in dangling_nodes)
        for n in x:
            for nbr in W[n]:
                x[nbr] += alpha * xlast[n] * W[n][nbr][weight]
            x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * dangling_weights[n]

        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < N*tol:
            return x




#saving the resulting frames
def get_file_frame(str, val):
    file = str.split(".mp4")[0] + ".mp4"
    frame_num = str.split(".mp4")[1]

    print '{} {}'.format("File:", file)
    print '{} {}'.format("Frame number:", frame_num)
    print '{} {}'.format("Pagerank:", val)

    print "--------------------------"

    out_dir = vid_folder + "//" + "output_frames"

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    full_filename = vid_folder + "\\" + file
    save_name = out_dir + "//" + file + "_" + frame_num + ".jpeg"

    vidcap = cv2.VideoCapture(full_filename)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        if count == int(frame_num):
            cv2.imwrite(save_name, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count += 1


# load saved images
def load_images(output):
    for f in os.listdir(output):
        img = cv2.imread(output + "//" + f)
        if img is not None:
            cv2.imshow(f , img)
            cv2.waitKey(1000)




if __name__ == '__main__':

        filename = raw_input("Enter input path of the graph file: ")
        m = raw_input("Enter the number of most significant frames to be found: ")
        vid_folder = raw_input("Enter path where the videos are stored: ")

        m = int(m)

        print "Processing... "
        h = Helper()

        graph = h.parse_data_from_file(filename)

        pr = calc_pagerank(graph)

        #pr = nx.pagerank(graph)
        sorted_pr = sorted(pr.iteritems(), key=lambda x:-x[1])[:m]
        print "Pagerank in sorted order:  "
        for x in sorted_pr:
            get_file_frame(x[0], x[1])

        output = vid_folder + "//" + "output_frames"
        load_images(output)

