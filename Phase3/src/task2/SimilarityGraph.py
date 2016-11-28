import numpy as np
from scipy.spatial import distance
import sys
import operator


def vector_distance(vector1, vector2):
    return distance.euclidean(vector1, vector2)


def sim_of_two_frames(frame1, frame2):
    """
    find similarity between two frames
    :param frame1: 2d array of features
    :param frame2: 2d array of features
    :return: float in range 0 and 1
    """
    sum = 0
    for x in frame1:
        min_distance = sys.maxint
        for y in frame2:
            dist = vector_distance(x, y)
            if dist < min_distance:
                min_distance = dist
        sum += min_distance

    # Converting distance to similarity
    sim = 1.0/(1+sum)
    return sim


def sim_of_frames(frame_arr):
    """

    :rtype: object
    """
    len = frame_arr.shape[1]
    sim_matrix = np.array(len, len)
    sim_matrix.fill(-1)
    for i in range(0, len):
        for j in range(i+1, len):
            sim = sim_of_frames(frame_arr[i], frame_arr[j])
            sim_matrix[i,j] = sim_matrix[j,i] = sim
    return sim_matrix


def knearest_frames(k, sim_arr):
    sim_dict = dict(enumerate(sim_arr))
    sorted_sim = sorted(sim_dict.items(), key=operator.itemgetter(1))
    out_sim = np.array((k,2))
    i = 0
    for x in sorted_sim:
        if x[1] > 0:
            out_sim[i,0] = x[0]
            out_sim[i,1] = x[1]
            i += 1
            if i == k:
                break
    return out_sim

def find_k_nearest_frames(inp_arr):
    """
    Find K most similar frames for each frame in the file
    :param inp_arr:
    :return: 2d array {(vs,fs),(vd,fd),sim(a,b)}
    """

    pass


if __name__ == "__main__":
    """
    Read Input from the user <Dimension Reduced Sift File, K(Integer)>
    Call method find_k_nearest_frames()
    Store to file

    """
    pass