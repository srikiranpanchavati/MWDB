# class for calculating the overall similarity
from Phase2.src.utils.OverallSimilarityHelper import OverallSimilarityHelper
import math
import scipy
from scipy import spatial
import csv


class OverallSimilarity:
    """
    overall similarity is defined as the percentage of visually similar frames shared between two video sequences
    The attributes we are considering here are color and sift features
    """

    def __init__(self, video1_hists, video2_hists, video1_sift_vectors, video2_sift_vectors):
        self.video1_hists = video1_hists
        self.video2_hists = video2_hists
        self.video1_sift_vectors = video1_sift_vectors
        self.video2_sift_vectors = video2_sift_vectors

    def find_similarity(self, option):
        len1 = len(self.video1_hists)
        len2 = len(self.video2_hists)
        hist_ratio = int(round(max(len1, len2) / float(min(len1, len2))))
        print hist_ratio
        if len(self.video1_hists) <= len(self.video2_hists):
            small_video_hists = self.video1_hists
            large_video_hists = self.video2_hists
        else:
            small_video_hists = self.video2_hists
            large_video_hists = self.video1_hists

        len1 = len(self.video1_sift_vectors)
        len2 = len(self.video2_sift_vectors)
        sift_ratio = int(round(max(len1, len2) / float(min(len1, len2))))
        print sift_ratio
        if len(self.video1_sift_vectors) <= len(self.video2_sift_vectors):
            small_video_sifts = self.video1_sift_vectors
            large_video_sifts = self.video2_sift_vectors
        else:
            small_video_sifts = self.video2_sift_vectors
            large_video_sifts = self.video1_sift_vectors
        overall_similarity = 0.0
        if option == "1":
            overall_similarity = (self.find_manhattan_hist_distance(small_video_hists, large_video_hists, hist_ratio) +
            self.find_manhattan_sift_distance(small_video_sifts, large_video_sifts, sift_ratio))/float(2)

        elif option == "2":
            overall_similarity = (self.find_minkowski_hist_distance(small_video_hists, large_video_hists, hist_ratio) +
                                  self.find_minkowski_sift_distance(small_video_sifts, large_video_sifts,
                                                                    sift_ratio)) / float(2)

        print "overall similarity = "
        print overall_similarity

    def find_manhattan_hist_distance(self, small_video_hists, large_video_hists, step):
        #print small_video_hists
        #print large_video_hists
        len1 = len(small_video_hists)
        len2 = len(large_video_hists)
        similarity = 0.0
        count = 0
        for i, j in zip(range(0, len1), range(0, len2, step)):
            x = small_video_hists[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                y = large_video_hists[k]  # list of histogram cells for a frame
                if k < len2:
                    for p, q in zip(x, y):
                        similarity += scipy.spatial.distance.cityblock(p, q)
                        count += 1
        print "count= %d" % count
        similarity += (similarity/float(count))

        print "The histogram similarity based on manhattan is "
        print similarity
        return similarity

    def find_manhattan_sift_distance(self, small_video_sifts, large_video_sifts, step):
        len1 = len(small_video_sifts)
        len2 = len(large_video_sifts)
        similarity = 0.0
        count = 0
        for i, j in zip(range(0, len1), range(0, len2, step)):
            x = small_video_sifts[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                y = large_video_sifts[k]  # list of histogram cells for a frame
                if k < len2:
                    for p, q in zip(x, y):
                        similarity += scipy.spatial.distance.cityblock(p, q)
                        count += 1
        print "count= %d" % count
        similarity += (similarity / float(count))

        print "The sift vector similarity based on manhattan is "
        print similarity
        return similarity


    def find_minkowski_hist_distance(self, small_video_hists, large_video_hists, step):
        len1 = len(small_video_hists)
        len2 = len(large_video_hists)
        similarity = 0.0
        count = 0
        for i, j in zip(range(0, len1), range(0, len2, step)):
            x = small_video_hists[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                y = large_video_hists[k]  # list of histogram cells for a frame
                if k < len2:
                    for p, q in zip(x, y):
                        similarity += scipy.spatial.distance.minkowski(p, q, 3)
                        count += 1
        print "count= %d" % count
        similarity += (similarity/float(count))

        print "The histogram similarity based on minkowski is "
        print similarity
        return similarity

    def find_minkowski_sift_distance(self, small_video_sifts, large_video_sifts, step):
        len1 = len(small_video_sifts)
        len2 = len(large_video_sifts)
        similarity = 0.0
        count = 0
        for i, j in zip(range(0, len1), range(0, len2, step)):
            x = small_video_sifts[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                y = large_video_sifts[k]  # list of histogram cells for a frame
                if k < len2:
                    for p, q in zip(x, y):
                        similarity += scipy.spatial.distance.minkowski(p, q, 3)
                        count += 1
        print "count= %d" % count
        similarity += (similarity / float(count))

        print "The sift vector similarity based on minkowski is "
        print similarity
        return similarity

    def find_manhattan_similarity_for_subsequence(self, hist_file_path, sift_file_path, video1_name, video2_name, a, b):
        overall_helper_obj = OverallSimilarityHelper(hist_file_path, sift_file_path, video1_name, video2_name)
        v1_hists, v2_hists = overall_helper_obj.parse_chst_files()
        v1_sifts, v2_sifts = overall_helper_obj.parse_sift_files()
        v2_len = len(v2_hists)
        similarities = {}
        window = b - a
        for i in range(0, v2_len):
            if (i + window) < v2_len:
                overall_sim = ((self.find_manhattan_hist_distance(v1_hists[a: (b+1)], v2_hists[i:(i + window + 1)], 1)+
                               self.find_manhattan_sift_distance(v1_sifts[a: (b + 1)], v2_sifts[i:(i + window + 1)], 1)) / float(2))
                indices = (i, i + window)
                mydict = {overall_sim: indices}
                similarities.update(mydict)
        print sorted(similarities.items())

    def find_minkowski_similarity_for_subsequence(self, hist_file_path, sift_file_path, video1_name, video2_name, a, b):
        overall_helper_obj = OverallSimilarityHelper(hist_file_path, sift_file_path, video1_name, video2_name)
        v1_hists, v2_hists = overall_helper_obj.parse_chst_files()
        v1_sifts, v2_sifts = overall_helper_obj.parse_sift_files()
        v2_len = len(v2_hists)
        similarities = {}
        window = b - a
        for i in range(0, v2_len):
            if (i + window) < v2_len:
                overall_sim = ((self.find_minkowski_hist_distance(v1_hists[a: (b+1)], v2_hists[i:(i + window + 1)], 1)+
                               self.find_minkowski_sift_distance(v1_sifts[a: (b + 1)], v2_sifts[i:(i + window + 1)], 1)) / float(2))
                indices = (i, i + window)
                mydict = {overall_sim: indices}
                similarities.update(mydict)
        print sorted(similarities.items())


def execute():
    chst_file_name = raw_input("Enter color histogram file name(absolute path): ")
    sift_file_name = raw_input("Enter sift vectors file name(absolute path): ")
    video1_name = raw_input("Enter video1 name with extension: ")
    video2_name = raw_input("Enter video2 name with extension: ")
    option = raw_input("Enter your choice \n1.Manhattan \n2.Minkowski : ")
    helper_obj = OverallSimilarityHelper(chst_file_name, sift_file_name, video1_name, video2_name)
    video1_hists, video2_hists = helper_obj.parse_chst_files()
    video1_sift_vectors, video2_sift_vectors = helper_obj.parse_sift_files()
    similarity_obj = OverallSimilarity(video1_hists, video2_hists, video1_sift_vectors, video2_sift_vectors)
    similarity_obj.find_similarity(option)



    #similarity_obj = OverallSimilarity(video1_hists, video2_hists, video1_sift_vectors, video2_sift_vectors)
    #similarity_obj.find_similarity()
    """
    helper_obj = ColorAndSiftHelper2("D:\\Education\\ASU\\MWD\\files\\test.chst", "D:\\Education\\ASU\\MWD\\files\\phase2videos.sift", "6x_SQ_BL_TM_BR_Noise.mp4", "c.mp4")
    video1_hists, video2_hists = helper_obj.parse_chst_files()
    video1_sift_vectors, video2_sift_vectors = helper_obj.parse_sift_files()
    similarity_obj = OverallSimilarity(video1_hists, video2_hists, video1_sift_vectors, video2_sift_vectors)
    similarity_obj.find_similarity()
    """
#execute()  this is for task 3
similarity_obj = OverallSimilarity(None,None,None,None)
similarity_obj.find_manhattan_similarity_for_subsequence("D:\\Education\\ASU\\MWD\\files\\phase2videos.chst", "D:\\Education\\ASU\\MWD\\files\\phase2videos.sift","6x_SQ_BL_TM_BR_Check.mp4","6x_SQ_BL_TM_BR_Noise.mp4", 5, 10)