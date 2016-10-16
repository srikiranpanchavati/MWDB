# TODO write docstring description for each method
import os.path
import sys

parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parent)

import numpy as np
from scipy.spatial import distance
from utils.MotionVectorHelper import MotionVectorHelper

class MotionVectorSimilarity:
    def __init__(self):
       pass

    # alter this function
    def euclidean_motionvector_similarity(self, array_1, array_2):
        euclidean_similarity = distance.euclidean(array_1, array_2)
        return euclidean_similarity

    # alter this function
    def cosine_motionvector_similarity(self, array_1, array_2):
        cosine_similarity = distance.cosine(array_1, array_2)
        return cosine_similarity

mv = MotionVectorHelper("motionVector_10r.mvect", "10R.mp4", "1R.mp4")
array_1, array_2 = mv.parseFile()

ms = MotionVectorSimilarity()
euclidean_distance = ms.euclidean_motionvector_similarity(array_1, array_2)
cosine_distance = ms.cosine_motionvector_similarity(array_1, array_2)

print "Euclidean Distance"
print euclidean_distance
print "Cosine Distance"
print cosine_distance



