import numpy as np
from Phase2.src.utils.helper import Helper
import cv2
import collections
import operator
from sklearn.preprocessing import StandardScaler
from Phase2.src.task3.pca import PCA


class KmeansReduction:
    def __init__(self, features, d):
        self.dimensions = d
        self.features = features

    @property
    def dimensions(self):
        return self.dimensions

    @dimensions.setter
    def dimensions(self, d):
        self.dimensions = d

    @property
    def features(self):
        return self.features

    @features.setter
    def features(self, f):
        self.features = f

    def reduce_dimensions(self):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        ret, label, center = cv2.kmeans(np.float32(self.features), self.dimensions, criteria, 10,
                                        cv2.KMEANS_RANDOM_CENTERS)
        scores = collections.Counter(label.ravel())
        sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
        new_features = np.dot(self.features, np.transpose(center))
        return new_features, sorted_scores, center


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

    __new_features, __feature_scores, __center  = KmeansReduction(__input_features, int(__new_dimensions)).reduce_dimensions()
    __new_hist_data = PCA.replace_original_features(__formatted_input_data,__new_features)
    __file_name = __out_file + __ext
    __file_stream = open(__file_name, "a")

    for data in __new_hist_data:
        data[3] = "[" + ",".join(str(x) for x in data[3]) + "]"
        write_data = ";".join(str(x) for x in data)
        __file_stream.write("%s\n" % write_data)
