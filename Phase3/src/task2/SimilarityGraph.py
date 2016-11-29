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
    total_dist = 0
    for x in frame1:
        min_distance = sys.maxint
        for y in frame2:
            dist = vector_distance(x, y)
            if dist < min_distance:
                min_distance = dist
        total_dist += min_distance

    # Converting distance to similarity
    sim = 1.0 / (1 + total_dist)
    return sim


# def sim_of_frames(frame_arr):
#     """
#
#     :param frame_arr:
#     :rtype: object
#     """
#     length = frame_arr.shape[1]
#     sim_matrix = np.array(length, length)
#     sim_matrix.fill(-1)
#     for i in range(0, length):
#         for j in range(0, length):
#             if i != j:
#                 sim = sim_of_two_frames(frame_arr[i], frame_arr[j])
#                 sim_matrix[i, j] = sim
    return sim_matrix


def similar_frames(index, frame_arr, k):
    length = frame_arr.shape[1]
    sim_list = []
    frame = frame_arr[index]
    for j in range(0, length):
        if index != j:
            sim = sim_of_two_frames(frame, frame_arr[j])
            sim_list.append(sim)
        else:
            sim_list.append(-1)

    return k_nearest_frames(sim_list, k)


def k_nearest_frames(K, sim_arr):
    sim_dict = dict(enumerate(sim_arr))
    sorted_sim = sorted(sim_dict.items(), key=operator.itemgetter(1))
    out_sim = np.array((K, 2))
    i = 0
    for x in sorted_sim:
        if x[1] > 0:
            out_sim[i, 0] = x[0]
            out_sim[i, 1] = x[1]
            i += 1
            if i == K:
                break
    return out_sim


def k_similar_frames(feature_arr, k, out_file_name):
    length = feature_arr.shape[1]
    frame_arr = feature_arr[:, -1]
    file_writer = open(out_file_name, 'w')
    for i in range(0, length):
        sim_arr = similar_frames(i, frame_arr, k)
        for j in range(0, k):
            str = feature_arr[i, 0] + ", "
            str += feature_arr[j, 0] + ", "
            str += sim_arr[i, j]
            file_writer.writelines(str)


# def k_frames_similarity(feature_arr, k, out_file_name):
#     """
#     Find K most similar frames for each frame in the file
#     :param feature_arr:
#     :rtype: object
#     :param inp_arr:
#     :return: 2d array {(vs,fs),(vd,fd),sim(a,b)}
#     """
#     sim_matrix = sim_of_frames(feature_arr[:, -1])
#     file_writer = open(out_file_name, 'w')
#     sim = k_nearest_frames(k, sim_matrix)
#     for i in range(0, len(sim)):
#         for j in range(0, len(sim[0])):
#             str = feature_arr[i, 0] + ", "
#             str += feature_arr[j, 0] + ", "
#             str += sim[i, j]
#             file_writer.writelines(str)


def read_file(inp_path):
    video_features = {}
    for line in open(inp_path):
        feature_list = line.split(",")
        key = (feature_list[0], feature_list[1])
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
    for key, value in video_features:
        vf_list.append([key, value])
    return np.asarray(vf_list)


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
    out_file = get_file_name(inp_file_path).split(".")[0] + "_" + str(k) + ".gspc"
    print(out_file)
    video_features = read_file(inp_file_path)
    k_similar_frames(video_features, k, out_file)
