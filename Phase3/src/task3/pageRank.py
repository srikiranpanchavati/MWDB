import networkx as nx
import numpy as np
from networkx.exception import NetworkXError
from Phase3.src.utils.Pagerank_helper import Helper
import os
import cv2

class PageRank:
    def calc_pagerank(self, D, weight='weight'):

        alpha=0.85  #damping factor
        tol=1.0e-6  #Tolerance value for convergence


        Stc_graph = nx.stochastic_graph(D, weight=weight)
        N = Stc_graph.number_of_nodes()

        x = dict.fromkeys(Stc_graph, 1.0 / N)
        D_weights = x
        D_nodes = [n for n in Stc_graph if Stc_graph.out_degree(n, weight=weight) == 0.0]

        # power iteration: make up to 300 iterations
        for _ in range(300):
            prev_x = x
            x = dict.fromkeys(prev_x.keys(), 0)
            D_sum = alpha * sum(prev_x[n] for n in D_nodes)
            for n in x:
                for nbr in Stc_graph[n]:
                    x[nbr] += alpha * prev_x[n] * Stc_graph[n][nbr][weight]
                x[n] += D_sum * D_weights[n] + (1.0 - alpha) * D_weights[n]

            err = sum([abs(x[n] - prev_x[n]) for n in x])
            if err < N*tol:
                return x




    #saving the resulting frames
    def get_file_frame(self, str, val, vid_folder):
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
    def load_images(self, output):
        for f in os.listdir(output):
            img = cv2.imread(output + "//" + f)
            if img is not None:
                cv2.imshow(f , img)
                cv2.waitKey(1000)
