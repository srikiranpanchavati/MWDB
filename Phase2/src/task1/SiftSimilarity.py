# TODO write docstring description for each method
import os.path
import sys



parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parent)

import numpy as np
from scipy.spatial import distance
from Phase2.src.utils.SiftVectorHelper import SiftVectorHelper
from Phase2.src.utils.OverallSimilarityHelper import OverallSimilarityHelper
from operator import itemgetter

class SiftSimilarity:
    def __init__(self):
       pass


    '''
        Overloaded manhattan distance function for TASK 1
        Input: array_1, array_2
    '''
    def manhattan_siftvector_similarity_2(self, small_video_sifts, large_video_sifts, step):
        len1 = len(small_video_sifts)
        len2 = len(large_video_sifts)
        similarity = 0.0
        count = 0
        for i, j in zip(range(0, len1), range(0, len2, step)):
            x = small_video_sifts[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                if k < len2:
                    y = large_video_sifts[k]  # list of histogram cells for a frame
                    for p, q in zip(x, y):
                        similarity += distance.cityblock(p, q)
                        count += 1
        # print "count= %d" % count
        similarity += (similarity / float(count))

        # print "The sift vector similarity based on manhattan is "
        # print similarity
        return similarity

    def process(self, video1_sifts, video2_sifts):
        len1 = len(video1_sifts)
        len2 = len(video2_sifts)
        sift_ratio = int(round(max(len1, len2) / float(min(len1, len2))))

        # print sift_ratio
        if len(video1_sifts) <= len(video2_sifts):
            small_video_sifts = video1_sifts
            large_video_sifts = video2_sifts
        else:
            small_video_sifts = video1_sifts
            large_video_sifts = video2_sifts
        return small_video_sifts, large_video_sifts, sift_ratio

    def chebyshev_siftvector_similarity_2(self, small_video_sifts, large_video_sifts, step):
        len1 = len(small_video_sifts)
        len2 = len(large_video_sifts)
        similarity = 0.0
        count = 0
        for i, j in zip(range(0, len1), range(0, len2, step)):
            x = small_video_sifts[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                if k < len2:
                    y = large_video_sifts[k]  # list of histogram cells for a frame
                    for p, q in zip(x, y):
                        similarity += distance.chebyshev(p, q)
                        count += 1
        # print "count= %d" % count
        similarity += (similarity / float(count))

        # print "The sift vector similarity based on manhattan is "
        # print similarity
        return similarity
        
    def find_manhattan_similarity_for_subsequence(self, sift_file_path, video1_name, video2_name, a, b):
        overall_helper_obj = OverallSimilarityHelper(None, sift_file_path, video1_name, video2_name)
        v1_hists, v2_hists = overall_helper_obj.parse_sift_files()
        v2_len = len(v2_hists)
        similarities = {}
        window = b - a
        for i in range(0, v2_len):
            if (i + window) < v2_len:
                overall_sim = self.manhattan_siftvector_similarity_2(v1_hists[a: (b+1)], v2_hists[i:(i + window + 1)], 1)
                indices = (i, i + window)
                mydict = {overall_sim: indices}
                similarities.update(mydict)
        return sorted(similarities.items())

    def find_chebyshev_similarity_for_subsequence(self, sift_file_path, video1_name, video2_name, a, b):
        overall_helper_obj = OverallSimilarityHelper(None, sift_file_path, video1_name, video2_name)
        v1_hists, v2_hists = overall_helper_obj.parse_sift_files()
        v2_len = len(v2_hists)
        similarities = {}
        window = b - a
        for i in range(0, v2_len):
            if (i + window) < v2_len:
                overall_sim = self.chebyshev_siftvector_similarity_2(v1_hists[a: (b+1)], v2_hists[i:(i + window + 1)], 1)
                indices = (i, i + window)
                mydict = {overall_sim: indices}
                similarities.update(mydict)
        return sorted(similarities.items())

if __name__ == "__main__":
    in_file = raw_input("Enter the absolute path for .sift file:")
    video_file_name_1 = raw_input("Enter the file name for the first video(with extension):")
    video_file_name_2 = raw_input("Enter the file name for the second video(with extension):")
    option = raw_input("Enter your choice \n1.chebyshev \n2.manhattan:")
    sv = SiftVectorHelper(in_file, video_file_name_1, video_file_name_2)
    video_array_1, video_array_2 = sv.parseFile()
    ms = SiftSimilarity()
    similarity = 0.0
    ovsim_obj = OverallSimilarityHelper(None, in_file, video_file_name_1, video_file_name_2)
    video_array_1, video_array_2 = ovsim_obj.parse_sift_files()
    v1_sifts, v2_sifts, ratio = ms.process(video_array_1, video_array_2)
    if option == "1":
        similarity = ms.chebyshev_siftvector_similarity_2(v1_sifts, v2_sifts, ratio)
    else:
        similarity = ms.manhattan_siftvector_similarity_2(v1_sifts, v2_sifts, ratio)
    print "Similarity"
    print similarity








