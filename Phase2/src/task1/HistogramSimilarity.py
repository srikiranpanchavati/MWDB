# TODO write docstring description for each method


import numpy as np
import cv2
import scipy.spatial
import os.path
import sys
from Phase2.src.utils.OverallSimilarityHelper import OverallSimilarityHelper

parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parent)


# from utils.ColorHistogramHelper import *


class HistogramSimilarity:
    def __init__(self):
        pass

    def compute_similarity_correlation(self, hist_video1, hist_video2):
        sum = 0.0
        count = 0
        l1 = len(hist_video1)  # number of frames in first video
        l2 = len(hist_video2)  # number of frames in second video
        first = []
        second = []
        if l1 == l2 or l1 < l2:
            first = hist_video1
            second = hist_video2
        else:
            first = hist_video2
            second = hist_video1
        l1 = len(first)
        l2 = len(second)
        step = int(round(l2 / l1))
        for i, j in zip(range(0, l1), range(0, l2, step)):
            x = first[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                if k < l2:
                    y = second[k]  # list of histogram cells for a frame
                    for p, q in zip(x, y):
                        result = cv2.compareHist(p, q, cv2.cv.CV_COMP_CORREL)
                        sum += result
                        count += 1
        return str(sum / count)

    def compute_similarity_chisquare(self, hist_video1, hist_video2):
        sum = 0.0
        count = 0
        l1 = len(hist_video1)  # number of frames in first video
        l2 = len(hist_video2)  # number of frames in second video
        first = []
        second = []
        if l1 == l2 or l1 < l2:
            first = hist_video1
            second = hist_video2
        else:
            first = hist_video2
            second = hist_video1
        l1 = len(first)
        l2 = len(second)
        step = int(round(l2 / l1))
        for i, j in zip(range(0, l1), range(0, l2, step)):
            x = first[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                if k < l2:
                    y = second[k]  # list of histogram cells for a frame
                    for p, q in zip(x, y):
                        result = cv2.compareHist(p, q, cv2.cv.CV_COMP_CHISQR)
                        sum += result
                        count += 1
        return str(sum / count)

    def compute_similarity_intersect(self, hist_video1, hist_video2):
        sum1 = 0.0
        sum2 = 0.0
        count = 0
        l1 = len(hist_video1)  # number of frames in first video
        l2 = len(hist_video2)  # number of frames in second video
        first = []
        second = []
        if l1 == l2 or l1 < l2:
            first = hist_video1
            second = hist_video2
        else:
            first = hist_video2
            second = hist_video1
        l1 = len(first)
        l2 = len(second)
        step = int(round(l2 / l1))
        for i, j in zip(range(0, l1), range(0, l2, step)):
            x = first[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                if k < l2:
                    y = second[k]  # list of histogram cells for a frame
                    for p, q in zip(x, y):
                        result = cv2.compareHist(p, q, cv2.cv.CV_COMP_INTERSECT)
                        sum1 += result
                        sum2 += sum(p) + sum(q) - result
                        count += 1
        return str(sum1 / sum2)

    def compute_similarity_bhattacharya(self, hist_video1, hist_video2):
        sum = 0.0
        count = 0
        l1 = len(hist_video1)  # number of frames in first video
        l2 = len(hist_video2)  # number of frames in second video
        first = []
        second = []
        if l1 == l2 or l1 < l2:
            first = hist_video1
            second = hist_video2
        else:
            first = hist_video2
            second = hist_video1
        l1 = len(first)
        l2 = len(second)
        step = int(round(l2 / l1))
        for i, j in zip(range(0, l1), range(0, l2, step)):
            x = first[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                if k < l2:
                    y = second[k]  # list of histogram cells for a frame
                    for p, q in zip(x, y):
                        result = cv2.compareHist(p, q, cv2.cv.CV_COMP_BHATTACHARYYA)
                        sum += result
                        count += 1
        return str(sum / count)


    def compute_similarity_euclidean(self, hist_video1, hist_video2):
        sum = 0.0
        count = 0
        l1 = len(hist_video1)  # number of frames in first video
        l2 = len(hist_video2)  # number of frames in second video
        first = []
        second = []
        if l1 == l2 or l1 < l2:
            first = hist_video1
            second = hist_video2
        else:
            first = hist_video2
            second = hist_video1
        l1 = len(first)
        l2 = len(second)
        step = int(round(l2 / l1))
        for i, j in zip(range(0, l1), range(0, l2, step)):
            x = first[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                if k < l2:
                    y = second[k]  # list of histogram cells for a frame
                    for p, q in zip(x, y):
                        result = scipy.spatial.distance.euclidean(p, q)
                        sum += result
                        count += 1
        return str(sum / count)


    def compute_similarity_manhattan(self, hist_video1, hist_video2):
        sum = 0.0
        count = 0
        l1 = len(hist_video1)  # number of frames in first video
        l2 = len(hist_video2)  # number of frames in second video
        first = []
        second = []
        if l1 == l2 or l1 < l2:
            first = hist_video1
            second = hist_video2
        else:
            first = hist_video2
            second = hist_video1
        l1 = len(first)
        l2 = len(second)
        step = int(round(l2 / l1))
        for i, j in zip(range(0, l1), range(0, l2, step)):
            x = first[i]  # list of histogram cells for a frame
            for k in range(j, j + step):
                if k < l2:
                    y = second[k]  # list of histogram cells for a frame
                    for p, q in zip(x, y):
                        result = scipy.spatial.distance.cityblock(p, q)
                        sum += result
                        count += 1
        return str(sum / count)

    def find_correlation_similarity_for_subsequence(self, hist_file_path, video1_name, video2_name, a, b):
        overall_helper_obj = OverallSimilarityHelper(hist_file_path, None, video1_name, video2_name)
        v1_hists, v2_hists = overall_helper_obj.parse_chst_files()
        v2_len = len(v2_hists)
        similarities = {}
        window = b - a
        for i in range(0, v2_len):
            if (i + window) < v2_len:
                sim = self.compute_similarity_correlation(v1_hists[a: (b+1)], v2_hists[i:(i + window + 1)])
                indices = (i, i + window)
                mydict = {sim: indices}
                similarities.update(mydict)
        return sorted(similarities.items(), reverse=True)

    def find_intersection_similarity_for_subsequence(self, hist_file_path, video1_name, video2_name, a, b):
        overall_helper_obj = OverallSimilarityHelper(hist_file_path, None, video1_name, video2_name)
        v1_hists, v2_hists = overall_helper_obj.parse_chst_files()
        v2_len = len(v2_hists)
        similarities = {}
        window = b - a
        for i in range(0, v2_len):
            if (i + window) < v2_len:
                sim = self.compute_similarity_intersect(v1_hists[a: (b+1)], v2_hists[i:(i + window + 1)])
                indices = (i, i + window)
                mydict = {sim: indices}
                similarities.update(mydict)
        return sorted(similarities.items(), reverse=True)


if __name__ == "__main__":
    chst_file_name = raw_input("Enter color histogram file name(absolute path): ")
    video1_name = raw_input("Enter video1 name with extension: ")
    video2_name = raw_input("Enter video2 name with extension: ")
    helper_obj = OverallSimilarityHelper(chst_file_name, None, video1_name, video2_name)
    video1_hists, video2_hists = helper_obj.parse_chst_files()
    similarity_obj = HistogramSimilarity()
    option = raw_input(
        "Enter your choice \n1.Correlation \n2.Chisquare \n3.Intersect \n4.Bhattacharya \n5.Euclidean \n6.Manhattan: ")
    result = 0.0
    if option == "1":
        result = similarity_obj.compute_similarity_correlation(video1_hists, video2_hists)
        print "The histogram similarity based on correlation is "
    elif option == "2":
        result = similarity_obj.compute_similarity_chisquare(video1_hists, video2_hists)
        print "The histogram similarity based on chisquare is "
    elif option == "3":
        result = similarity_obj.compute_similarity_intersect(video1_hists, video2_hists)
        print "The histogram similarity based on intersect is "
    elif option == "4":
        result = similarity_obj.compute_similarity_bhattacharya(video1_hists, video2_hists)
        print "The histogram similarity based on bhattacharya is "
    elif option == "5":
        result = similarity_obj.compute_similarity_euclidean(video1_hists, video2_hists)
        print "The histogram similarity based on euclidean is "
    elif option == "6":
        result = similarity_obj.compute_similarity_manhattan(video1_hists, video2_hists)
        print "The histogram similarity based on manhattan is "
    print result


# #task 3 execution
# similarity_obj = HistogramSimilarity()
# print similarity_obj.find_correlation_similarity_for_subsequence("D:\\Education\\ASU\\MWD\\files\\phase2videos.chst", "6x_SQ_BL_TM_BR_Check.mp4","6x_SQ_BL_TM_BR_Check.mp4", 5, 10)