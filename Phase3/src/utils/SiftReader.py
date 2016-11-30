"""
    Helper function to Extract the Sift features in numpy arrays
    written_by: @aditya
    rev: 1
    Input: Exact location of the sift feature file
    Output: np array containing the sift features video_file_name, video_number, frame_number, cell_number, x, y
            np array containing the 128 length sift descriptors

            {<i, j, l, x, y>, [dim1,...,dimd]},

"""

import numpy as np


class SiftReader(object):
    def __init__(self, in_file):
        self.input_file = in_file

    def parse_file(self):
        with open(self.input_file) as my_file:
            lines = my_file.read().splitlines()

        """
            sift_points will contain <i, j, l, x, y>
            sift_descriptor will contain [scale, orientation, desc1,...,desc128]
        """
        # empty numpy array
        sift_points_database = []
        # empty numpy array
        sift_descriptors_database = []

        """
            temp[0] contains file name
            temp[1] contains frame number
            temp[2] contains cell number
            temp[3] contains descriptor string
        """

        for line in lines:
            point = []
            descriptor = []
            temp = line.split(';')
            # append video_file_name
            point.append(str(temp[0]))
            # append frame number
            point.append(int(temp[1]))
            # append video cell number
            point.append(int(temp[2]))

            sift_info = temp[3].translate(None, '[]\n')
            """
                sift_info contains descriptor string
                sift_features[0] : x
                sift_features[1] : y
            """
            sift_features = sift_info.split(',')
            # add x value
            point.append(int(sift_features[0]))
            # add y value
            point.append(int(sift_features[1]))
            # add the points to the final database
            sift_points_database.append(point)
            # construct the descriptor
            sift_descriptor = [float(i) for i in sift_features[2:]]
            for x in sift_descriptor:
                descriptor.append(x)
            # add the descriptors to the final database
            sift_descriptors_database.append(descriptor)

        sift_points_database = np.array(sift_points_database)
        sift_descriptors_database = np.array(sift_descriptors_database)

        return sift_points_database, sift_descriptors_database
