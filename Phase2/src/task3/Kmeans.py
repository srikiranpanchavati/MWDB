import cv2 as cv
import numpy as np


class Kmeans:
    def __init__(self):
        pass

    def kmeans_hist(self, hist=None):
        if hist is None:
            return hist

        hist_pts = np.zeros((len(hist), hist[0][3].size))
        for i in range(0, len(hist)):
            hist_pts[i] = hist[i][3]