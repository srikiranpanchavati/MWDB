"""
    Helper function to apply pca on SIFT features
    written_by: @aditya
    rev: 1
    Input: Exact location of the sift feature file
    Output: SIFT feature file containing the reduced dimensionality SIFT features

            {<i, j, l, x, y>, [dim1,...,dimd]},

"""

from Phase3.src.utils.SiftReader import SiftReader
from Phase3.src.utils.SiftWriter import SiftWriter
from sklearn.decomposition import PCA as sklearnPCA
from sklearn import preprocessing
import numpy as np


class PCA:
    def __init__(self, in_file, n_dimensions):
        self.in_file = in_file
        self.n_dimensions = int(n_dimensions)
        # parse the file
        sv = SiftReader(in_file)
        self.sift_points, non_standard_sift_descriptors = sv.parse_file()
        # standardize sift features..
        scaler = preprocessing.StandardScaler().fit(non_standard_sift_descriptors)
        self.sift_descriptors = scaler.transform(non_standard_sift_descriptors)

    def get_pca_reduced_features(self):
        input_features = self.sift_descriptors
        d = self.n_dimensions
        if input_features is None or d is None:
            return input_features

        m1 = np.mean(input_features, axis=0)
        b = input_features - m1

        covariance_matrix = (np.dot(b.transpose(), b)) / (b.shape[0] - 1)
        eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)

        feature_scores = []
        new_features = input_features
        if d < eigen_values.size:
            eigen_tuples = sorted(enumerate(eigen_values), key=lambda x: x[1], reverse=True)
            indices_needed = []
            sum_eval = np.sum(eigen_values)

            for i in range(0, d):
                feature_scores.append((eigen_tuples[i][0], eigen_vectors[eigen_tuples[i][0]]))
                indices_needed.append(eigen_tuples[i][0])

            new_ev = eigen_vectors[indices_needed]
            new_features = np.dot(input_features, np.transpose(new_ev))

        return self.sift_points, new_features, feature_scores

if __name__ == "__main__":
    __file_path = raw_input("input file path: ")
    __new_dimensions = raw_input("Enter value of d: ")
    __out_file = __file_path.rpartition('.')[0] + "_" + str(__new_dimensions)
    __out_file_ext = ".spc"

    # apply pca..
    pca_handler = PCA(__file_path, __new_dimensions)
    __sift_points, __reduced_dimensions, __feature_scores = pca_handler.get_pca_reduced_features()

    # print("Scores for each PC dimension as per the original index:")
    # print(__feature_scores)

    # write the sift reduced sift features to the output file..
    __file_name = __out_file + __out_file_ext
    sw = SiftWriter(__file_name)
    sw.write_to_file(__sift_points, __reduced_dimensions)
    score_file = __out_file + ".score"
    fs = open(score_file, "w")
    fs.writelines(str(__feature_scores))
