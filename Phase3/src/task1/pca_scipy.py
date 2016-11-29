"""
    Helper function to apply pca on SIFT features
    written_by: @aditya
    rev: 1
    Input: Exact location of the sift feature file
    Output: SIFT feature file containing the reduced dimensionality SIFT features

            {<i, j, l, x, y>, [dim1,...,dimd]},

"""

from src.utils.SiftReader import SiftReader
from src.utils.SiftWriter import SiftWriter
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
import numpy as np

class PCA:
    def __init__(self, in_file, n_dimensions):
        self.in_file = in_file
        self.n_dimensions = int(n_dimensions)
        # parse the file
        sv = SiftReader(in_file)
        self.sift_points, non_standard_sift_descriptors = sv.parse_file()
        # mean removal and standard scaling
        scaler = StandardScaler()
        scaler.fit(non_standard_sift_descriptors)
        # nd array containing
        self.sift_descriptors = scaler.transform(non_standard_sift_descriptors)

    def get_reduced_dimensions(self):
        pca = sklearnPCA(n_components=self.n_dimensions)
        # array returned after fitting the input data to
        pca.fit(self.sift_descriptors)

        sift_points = self.sift_points
        transformed_features = pca.transform(self.sift_descriptors)

        # have to figure out how to get the scores...
        '''
        print(type(transformed_features))
        feature_scores = pca.score_samples(self.sift_descriptors)
        print(type(feature_scores))
        '''
        transformed_features = np.around(transformed_features, 3)

        return sift_points, transformed_features


if __name__ == "__main__":
    __file_path = raw_input("input file path: ")
    __new_dimensions = raw_input("Enter value of d: ")
    __out_file = __file_path.rpartition('.')[0] + "_" + str(__new_dimensions)
    __out_file_ext = ".spc"

    # apply pca..
    pca_handler = PCA(__file_path, __new_dimensions)
    __sift_points, __reduced_dimensions = pca_handler.get_reduced_dimensions()

    # write the sift reduced sift features to the output file..
    __file_name = __out_file + __out_file_ext
    sw = SiftWriter(__file_name)
    sw.write_to_file(__sift_points, __reduced_dimensions)

