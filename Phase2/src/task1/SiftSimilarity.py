import os.path
import sys

parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parent)

import numpy as np
from scipy.spatial import distance
from utils.SiftVectorHelper import SiftVectorHelper

class SiftSimilarity:
    def __init__(self):
       pass

    # alter this function
    def euclidean_motionvector_similarity(self, array_1, array_2):
        # euclidean_similarity = distance.euclidean(array_1, array_2)
        # return euclidean_similarity
        print "Calc Eucledian"

    # alter this function
    def cosine_motionvector_similarity(self, array_1, array_2):
        # cosine_similarity = distance.cosine(array_1, array_2)
        # return cosine_similarity
        print "Calc Cosine"

svh = SiftVectorHelper("C:\Users\sjjai\Desktop\Phase2\out_sift.sift", "10R.mp4", "1R.mp4")
array_1, array_2 = svh.parseFile()

svs = SiftSimilarity()
euclidean_distance = svs.euclidean_motionvector_similarity(array_1, array_2)
cosine_distance = svs.cosine_motionvector_similarity(array_1, array_2)

print "Euclidean Distance"
print euclidean_distance
print "Cosine Distance"
print cosine_distance