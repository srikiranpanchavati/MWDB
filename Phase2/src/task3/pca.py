import numpy as np
from Phase2.src.utils.helper import Helper


class PCA:
    def __init__(self):
        pass

    @staticmethod
    def pca_histogram(hist=None, d=None):
        if hist is None or d is None:
            return hist

        hist_pts = np.zeros((len(hist), len(hist[0][3])))
        for i in range(0, len(hist)):
            hist_pts[i] = hist[i][3]

        m1 = np.mean(hist_pts, axis=0)
        b = hist_pts - m1

        covariance_matrix = (np.dot(b.transpose(), b)) / (b.shape[0] - 1)
        eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
        if d < eigen_values.size:
            eigen_tuples = sorted(enumerate(eigen_values), key=lambda x: x[1], reverse=True)
            indices_to_remove = []
            for i in range(d, eigen_values.size):
                indices_to_remove.append(eigen_tuples[i][0])
            new_pts = np.delete(hist_pts, indices_to_remove, 1)
            for i in range(0, len(hist)):
                hist[i][3] = new_pts[i]
        return hist


if __name__ == "__main__":
    __file_path = raw_input("input file path: ")
    helper = Helper()
    hist = helper.get_histogram(__file_path)
    PCA.pca_histogram(hist, 7)
