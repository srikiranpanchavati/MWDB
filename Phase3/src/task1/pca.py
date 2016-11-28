import numpy as np
from src.utils.Task1Helper import Helper
from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import IncrementalPCA

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
        # eigen vectors contains the reduced vector space..
        eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)

        feature_scores = []

        if d < eigen_values.size:
            # sort the eigen values after enumerating them based on key 1
            eigen_tuples = []
            for x in range(len(eigen_values)):
                # unsorted eigen values with original indexes
                eigen_tuples.append((x, eigen_values[x]))

            # sorted eigen values with original indexes
            sorted_eigen_tuples = sorted(eigen_tuples, key=lambda x: x[1], reverse=True)

            indices_needed = []
            sum_eval = np.sum(eigen_values)

            for i in range(0, d):
                feature_scores.append((sorted_eigen_tuples[i][0], (sorted_eigen_tuples[i][1]/sum_eval)*100))
                indices_needed.append(sorted_eigen_tuples[i][0])

            # project the input space to the PC co-ordinates
            new_features = np.dot(input_features, np.transpose(eigen_vectors))

            reduced_values = []
            # select the d dimensions and place into new_features
            for i in range(len(sorted_eigen_tuples)):
                if i in indices_needed:
                    reduced_values = np.append(reduced_values, new_features[:, i])

            reduced_values = np.reshape(reduced_values, (int(d), len(new_features)))

            # final_reduced_features has the first d dimensions from the sorted array..
            final_reduced_features = reduced_values.T

            print(np.shape(final_reduced_features))

        return feature_scores, final_reduced_features, eigen_vectors, sorted_eigen_tuples


if __name__ == "__main__":
    __file_path = raw_input("input file path: ")
    __new_dimensions = raw_input("Enter value of d: ")
    __out_file = __file_path.rpartition('.')[0] + "_" + str(__new_dimensions)
    __ext = ""

    if __file_path.endswith(".chst"):
        __ext = ".cpca"
    elif __file_path.endswith(".sift"):
        __ext = ".spca"
    elif __file_path.endswith(".mvect"):
        __ext = ".mpca"

    helper = Helper()

    __formatted_input_data = helper.parse_data_from_file(__file_path)
    __input_features = [data[3] for data in __formatted_input_data]
    if not __file_path.endswith(".chst"):
        __input_features = StandardScaler().fit_transform(__input_features)

    # get the eigen values, vectors and feature scores
    __feature_scores, __new_features, eigen_vectors, sorted_eigen_values = \
        PCA.pca_transform(__input_features, int(__new_dimensions))

    # replace the input features with reduced dimensions in the input matrix
    __new_hist_data = PCA.replace_original_features(__formatted_input_data,__new_features)

    __file_name = __out_file + __ext
    __file_stream = open(__file_name, "a")

    for data in __new_hist_data:
        data[3] = "[" + ",".join(str(x) for x in data[3]) + "]"
        write_data = ";".join(str(x) for x in data)
        __file_stream.write("%s\n" % write_data)

