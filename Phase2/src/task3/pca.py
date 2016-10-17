import cv2 as cv
import numpy as np
from Phase2.src.utils.helper import Helper

class PCA:
    def __init__(self):
        pass

    @staticmethod
    def pca_histogram(hist=None):
        if hist is None:
            return hist

        hist_pts = np.zeros((len(hist), len(hist[0][3])))
        for i in range(0, len(hist)):
            hist_pts[i] = hist[i][3]

        m1 =  np.zeros((1, hist_pts.shape[1]))
        for i in range(hist_pts.shape[1]):
            for j in range(hist_pts.shape[0]):
                m1[0][i] += hist_pts[j][i]
            m1[0][i] /= hist_pts.shape[0]

        b = np.zeros(hist_pts.shape)
        for i in range(hist_pts.shape[0]):
            for j in range(hist_pts.shape[1]):
                b[i][j] = m1[0][j] - hist_pts[i][j]

        covariance_matrix = (np.dot(b.transpose(), b))/(b.shape[0] - 1)
        eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)


if __name__ == "__main__":
    __file_path = raw_input("input file path: ")
    helper = Helper()
    hist = helper.get_histogram(__file_path)
    PCA.pca_histogram(hist)