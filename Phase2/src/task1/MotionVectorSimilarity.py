# TODO write docstring description for each method
import os.path
import sys

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

import numpy as np
from scipy.spatial import distance
from utils.helper import FileIO

class MotionVectorSimilarity:
    def __init__(self, videoFile1, videoFile2):
        self.v1 = videoFile1
        self.v2 = videoFile2

    def euclidean_motionvector_similarity(self, array_1, array_2):
        euclidean_similarity = distance.euclidean(array_1, array_2)
        return euclidean_similarity

    def cosine_motionvector_similarity(self, array_1, array_2):
        cosine_similarity = distance.cosine(array_1, array_2)
        return cosine_similarity

mv = MotionVectorSimilarity("1R.mp4", "2R.mp4")
file_operator = FileIO("sift_vectors.txt", mv.v1, mv.v2)
file_operator.vectorizeInput()
