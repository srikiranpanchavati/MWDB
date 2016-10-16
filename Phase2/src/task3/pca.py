import cv2 as cv
import numpy as np


class PCA:
    def __init__(self):
        pass

    @staticmethod
    def pca_histogram(hist=None):
        if hist is None:
            return hist

        hist_pts = np.zeros((len(hist), hist[0][3].size))
        for i in range(0, len(hist)):
            hist_pts[i] = hist[i][3]
        mean, eigen_vectors = cv.PCACompute(hist_pts, np.mean(hist_pts, axis=0).reshape(1, -1))
        print("Mean:")
        print(mean)
        print("Eigen Vectors:")
        print(eigen_vectors)
