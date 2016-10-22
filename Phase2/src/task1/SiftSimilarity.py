import os.path
import sys
from operator import itemgetter


parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parent)

import numpy as np
from scipy.spatial import distance
from utils.SiftVectorHelper import SiftVectorHelper

class SiftSimilarity:
    def __init__(self, array_1, array_2):
        self.vid_arr_1 = array_1
        self.vid_arr_2 = array_2
        self.k = 30


    #to be modified acc to the cosine function
    def euclidean_motionvector_similarity(self, array_1, array_2):
        i = 0
        euclidean_similarity = 0
        for i in range(min(len(array_1), len(array_2))):
            euclidean_similarity += distance.euclidean(array_1[i][6:], (array_2[i][6:]))

        euclidean_similarity = euclidean_similarity / i
        return euclidean_similarity




    def cosine_motionvector_similarity(self, array_1, array_2):
        measure_similarity = 0
        num_frame_1 = int(array_1[-1][0])
        num_frame_2 = int(array_2[-1][0])
        total_similarity = 0
        result = 0

        sim_arr = []
        step = self.k
        start_1 = 0
        end_1 = step
        start_2 = 0
        best_match = 0


        window = self.extract_window(array_1, start_1, end_1)

        for win in range(step, num_frame_2, 1):
            window_2 = self.extract_window(array_2, start_2, win)
            start_2 +=1

            for a in range(1, step+1):

                cosine_similarity = 0
                frame_1 = []
                frame_2 = []
                for item_1 in window:
                    if item_1[0] == a:
                        frame_1.append(item_1)

                for item_2 in window_2:
                    if item_2[0] == a:
                        frame_2.append(item_2)
                i=1
                for i in range(min(len(frame_1), len(frame_2))):
                    cosine_similarity += distance.cosine(frame_1[i][6:], (frame_2[i][6:]))

                cosine_similarity = cosine_similarity / i
                total_similarity += cosine_similarity


            total_similarity = total_similarity/self.k
            sim_arr.append(total_similarity)

        best_match = max(enumerate(sim_arr), key=itemgetter(1))[0]
        result += best_match * step


        start1 = step
        start2 = best_match + step
        end1 = start1 + step
        end2 = start2 + step

        while (end2 <= num_frame_2):
            sim_total = 0
            window = self.extract_window(array_1, start1, end1)
            window_2 = self.extract_window(array_2, start2, end2)


            for a in range(1, step+1):
                cosine_similarity = 0
                frame_1 = []
                frame_2 = []
                for item_1 in window:
                    if item_1[0] == a+start1:
                        frame_1.append(item_1)


                for item_2 in window_2:
                    if item_2[0] == a+start2:
                        frame_2.append(item_2)


                for i in range(min(len(frame_1), len(frame_2))):
                    cosine_similarity += distance.cosine(frame_1[i][6:], (frame_2[i][6:]))

                if i == 0:
                    cosine_similarity = 0
                else:
                    cosine_similarity = cosine_similarity / i
                sim_total += cosine_similarity

            sim_total /= self.k
            result += sim_total * step
            start1 +=step
            start2 +=step
            end1 +=step
            end2 +=step


        measure_similarity = result/num_frame_1
        print measure_similarity




    def extract_window(self, array, start, end):
        ex_arr = []
        for x in array:
            if(x[0] > start and x[0] <= end):
                ex_arr.append(x)

        return ex_arr


svh = SiftVectorHelper("C:\Users\sjjai\Desktop\Phase2\out_sift.sift", "5R.mp4", "6R.mp4")
array_1, array_2 = svh.parseFile()

svs = SiftSimilarity(array_1, array_2)


#euclidean_distance = svs.euclidean_motionvector_similarity(array_1, array_2)
cosine_distance = svs.cosine_motionvector_similarity(array_1, array_2)

# print "{} ->  {}".format("Euclidean Distance", euclidean_distance)
# print "{} ->  {}".format("Cosine Distance", cosine_distance)
