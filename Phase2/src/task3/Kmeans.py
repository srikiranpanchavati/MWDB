import numpy as np
from Phase2.src.utils.helper import Helper
import cv2
import collections
import operator


class KmeansReduction:
    def __init__(self, in_file, features, d):
        self.dimensions = d
        self.features = features
        self.in_file = in_file

    @property
    def in_file(self):
        return self.in_file

    @in_file.setter
    def in_file(self, value):
        self.in_file = value

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
        new_feature = np.dot(self.features, np.transpose(center))
        return new_feature[0], sorted_scores, center


if __name__ == "__main__":
    file_path = raw_input("input file path: ")
    dimensions = input("Number of dimensions to retain: ")
    helper = Helper()
    hist = helper.get_histogram(file_path)
    hist_pts = np.zeros((len(hist), len(hist[0][3])))
    for i in range(0, len(hist)):
        hist_pts[i] = hist[i][3]
    dr = KmeansReduction(hist, hist_pts, dimensions)
    dr.reduce_dimensions()
