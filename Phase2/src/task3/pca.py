import numpy as np
from Phase2.src.utils.Task3Helper import Helper
from sklearn.preprocessing import StandardScaler


class PCA:
    def __init__(self):
        pass

    # extracts only the feature list from the input data list
    @staticmethod
    def parse_features(input_data):
        feature_data = np.zeros((len(input_data), len(input_data[0][3])))
        for i in range(0, len(input_data)):
            feature_data[i] = input_data[i][3]
        return feature_data

    # replaces original feature vectors with reduced feature in the list
    @staticmethod
    def replace_original_features(input_data, new_features):
        for i in range(0, len(input_data)):
                input_data[i][3] = new_features[i]
        return input_data

    # performs PCA transformation on the original features and returns score and reduced feature vector list
    @staticmethod
    def pca_transform(input_features=None, d=None):
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
                feature_scores.append((eigen_tuples[i][0], (eigen_tuples[i][1]/sum_eval)*100))
                indices_needed.append(eigen_tuples[i][0])

            new_ev = eigen_vectors[indices_needed]
            new_features = np.dot(input_features, np.transpose(new_ev))

        return feature_scores, new_features


if __name__ == "__main__":
    __file_path = raw_input("input file path: ")
    __new_dimensions = raw_input("Enter value of d: ")
    __out_file = raw_input("enter output file name without extension: ")
    __ext = ""

    if __file_path.endswith(".chst"):
        __ext = ".ckm"
    elif __file_path.endswith(".sift"):
        __ext = ".skm"
    elif __file_path.endswith(".mvect"):
        __ext = ".mkm"

    helper = Helper()

    __formatted_input_data = helper.parse_data_from_file(__file_path)
    __input_features = [data[3] for data in __formatted_input_data]
    if not __file_path.endswith(".chst"):
        __input_features = StandardScaler().fit_transform(__input_features)

    __feature_scores, __new_features = PCA.pca_transform(__input_features, int(__new_dimensions))
    __new_hist_data = PCA.replace_original_features(__formatted_input_data,__new_features)
    __file_name = __out_file + __ext
    __file_stream = open(__file_name, "a")

    for data in __new_hist_data:
        data[3] = "[" + ",".join(str(x) for x in data[3]) + "]"
        write_data = ";".join(str(x) for x in data)
        __file_stream.write("%s\n" % write_data)

