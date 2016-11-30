import networkx as nx
import numpy as np
from networkx.exception import NetworkXError
from Phase3.src.utils.Pagerank_helper import Helper
import os
import cv2


def google_matrix(G, alpha=0.85, personalization=None,
                  nodelist=None, weight='weight', dangling=None):



    if nodelist is None:
        nodelist = list(G)

    M = nx.to_numpy_matrix(G, nodelist=nodelist, weight=weight)
    N = len(G)
    if N == 0:
        return M

    # Personalization vector
    if personalization is None:
        p = np.repeat(1.0 / N, N)
    else:
        missing = set(nodelist) - set(personalization)
        if missing:
            raise NetworkXError('Personalization vector dictionary '
                                'must have a value for every node. '
                                'Missing nodes %s' % missing)
        p = np.array([personalization[n] for n in nodelist], dtype=float)
        p /= p.sum()

    # Dangling nodes
    if dangling is None:
        dangling_weights = p
    else:
        missing = set(nodelist) - set(dangling)
        if missing:
            raise NetworkXError('Dangling node dictionary '
                                'must have a value for every node. '
                                'Missing nodes %s' % missing)
        # Convert the dangling dictionary into an array in nodelist order
        dangling_weights = np.array([dangling[n] for n in nodelist],
                                    dtype=float)
        dangling_weights /= dangling_weights.sum()
    dangling_nodes = np.where(M.sum(axis=1) == 0)[0]

    # Assign dangling_weights to any dangling nodes (nodes with no out links)
    for node in dangling_nodes:
        M[node] = dangling_weights

    M /= M.sum(axis=1)  # Normalize rows to sum to 1

    return alpha * M + (1 - alpha) * p


def pagerank_numpy(G, alpha=0.85, personalization=None, weight='weight',
                   dangling=None):

    if len(G) == 0:
        return {}
    M = google_matrix(G, alpha, personalization=personalization,
                      weight=weight, dangling=dangling)
    # use numpy LAPACK solver
    eigenvalues, eigenvectors = np.linalg.eig(M.T)
    ind = np.argmax(eigenvalues)
    # eigenvector of largest eigenvalue is at ind, normalized
    largest = np.array(eigenvectors[:, ind]).flatten().real
    norm = float(largest.sum())
    return dict(zip(G, map(float, largest / norm)))



#saving the resulting frames
def get_file_frame(str, val):
    file = str.split(".mp4")[0][3:] + ".mp4"
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
        success,image = vidcap.read()
        if count == int(frame_num):
            cv2.imwrite(save_name, image)     # save frame as JPEG file
        count += 1


# load saved images
def load_images(output):
    for f in os.listdir(output):
        img = cv2.imread(output + "//" + f)
        if img is not None:
            cv2.imshow(f , img)
            cv2.waitKey(1000)




if __name__ == '__main__':

        filename = "C:\Users\sjjai\Desktop\Phase3\sample_input.gspc"  #raw_input("Enter input path of the graph file: ")
        vid_folder = "C:\Users\sjjai\Desktop\Phase3\P2DemoVideos"  #raw_input("Enter path where the videos are stored: ")
        m = 5   #raw_input("Enter the number of most significant frames to be found: ")

        h = Helper()
        print "Processing... "
        graph = h.parse_data_from_file(filename)
        pr = pagerank_numpy(graph, alpha=0.8)

        sorted_pr = sorted(pr.iteritems(), key=lambda x:-x[1])[:m]
        print "Pagerank in sorted order:  "
        for x in sorted_pr:
            get_file_frame(x[0], x[1])

        output = vid_folder + "//" + "output_frames"
        load_images(output)

