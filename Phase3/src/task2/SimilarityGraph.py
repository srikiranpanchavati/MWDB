import numpy as np
from scipy.spatial import distance
import sys
import operator
import ntpath


def vector_distance(vector1, vector2):
    return distance.euclidean(vector1, vector2)


def sim_of_two_frames(frame1, frame2):
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


def similar_frames(index, frame_arr, k):
    length = frame_arr.shape[0]
    sim_list = []
    frame = frame_arr[index]
    for j in range(0, length):
        if index != j:
            sim = sim_of_two_frames(frame, frame_arr[j])
            sim_list.append(sim)
        else:
            sim_list.append(-1)

    return k_nearest_frames(sim_list, k)


def k_nearest_frames(sim_arr, K):
    sim_dict = dict(enumerate(sim_arr))
    sorted_sim = sorted(sim_dict.items(), key=operator.itemgetter(1), reverse=True)
    out_sim = np.zeros((K, 2))
    i = 0
    for x in sorted_sim:
        out_sim[i, 0] = x[0]
        out_sim[i, 1] = x[1]
        i += 1
        if i == K:
            break
    return out_sim


def k_similar_frames(feature_arr, k, out_file_name):
    length = feature_arr.shape[0]
    frame_arr = np.asarray(feature_arr[:, 1])
    file_writer = open(out_file_name, 'w')
    for i in range(0, length):
        sim_arr = similar_frames(i, frame_arr, k)
        for j in range(0, k):
            line = str(feature_arr[i, 0]) + ", "
            line += str(feature_arr[sim_arr[j, 0], 0]) + ", "
            line += str(sim_arr[j, 1])+'\n'
            file_writer.write(line)
    file_writer.close()


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
        vf_list.append([(key, value), video_features[(key, value)]])
    return np.asarray(vf_list)


def get_file_name(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


if __name__ == "__main__":
    inp_file_path = raw_input("Enter Sift file path:")
    k = int(raw_input("Enter K value:"))
    out_file = get_file_name(inp_file_path).split(".")[0] + "_" + str(k) + ".gspc"
    print(out_file)
    video_features = read_file(inp_file_path)
    k_similar_frames(video_features, k, out_file)
