import numpy as np
from scipy.spatial import distance
import sys
import operator
import ntpath


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

def kframes_similarity(feature_arr, k, out_file_name):
    """
    Find K most similar frames for each frame in the file
    :param inp_arr:
    :return: 2d array {(vs,fs),(vd,fd),sim(a,b)}
    """
    sim_matrix = sim_of_frames(feature_arr[:,-1])
    knearest_frames(k, sim_matrix)


def read_file(inp_path):
    video_features = {}
    for line in open(inp_path):
        feature_list = line.split(",")
        key  = (feature_list[0], feature_list[1])
        if key not in video_features:
            video_features[key] = []
        features = video_features[key]
        feature = []
        feature.append(float(feature_list[2]))
        feature.append(float(feature_list[3]))
        feature.append(float(feature_list[4]))
        sift_info = feature_list[5].translate(None, '[]')
        desc = sift_info.split()
        for f in desc:
            feature.append(float(f))
        features.append(feature)
    vf_list = []
    for key,value in video_features:
        vf_list.append([key,value])
    print(vf_list)
    return vf_list

# def read_file(inp_path):
#     video_features = {}
#     for line in open(inp_path):
#         feature_list = line.split(",")
#         video_key = feature_list[0]
#         frame_key = feature_list[1].strip()
#         if video_key not in video_features:
#             video_features[video_key] = {}
#         frame_features = video_features[video_key]
#         if frame_key not in frame_features:
#             frame_features[frame_key] = []
#         features = frame_features[frame_key]
#         feature = []
#         feature.append(float(feature_list[2]))
#         feature.append(float(feature_list[3]))
#         feature.append(float(feature_list[4]))
#         sift_info = feature_list[5].translate(None, '[]')
#         desc = sift_info.split()
#         for f in desc:
#             feature.append(float(f))
#         features.append(feature)
#     print(video_features)

def get_file_name(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

if __name__ == "__main__":
    """
    Read Input from the user <Dimension Reduced Sift File, K(Integer)>
    Call method find_k_nearest_frames()
    Store to file

    """
    inp_file_path = raw_input("Enter Sift file path:")
    k = int(raw_input("Enter K value:"))
    out_file = get_file_name(inp_file_path).split(".")[0] +"_"+str(k)+".gspc"
    print(out_file)
    video_features = read_file(inp_file_path)
    kframes_similarity(video_features, k, out_file)