import numpy as np


class VideoSearchHelper(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def parse_lsh(self):
        file_name = self.input_file

        with open(file_name) as my_file:
            lines = my_file.read().splitlines()

        """
            line[0] contains layer number
            line[1] contains bucket number
            line[2] contains file name
            line[3] contains frame number
            line[4] contains cell number
            line[5] contains x-coordinate
            line[6] contains y-coordinate
        """
        lsh_database = []
        for line in lines:
            nd_row = []
            data = line.split(",")
            nd_row.append(int(data[0]))
            nd_row.append(int(data[1]))
            nd_row.append(str(data[2]))
            nd_row.append(int(data[3]))
            nd_row.append(int(data[4]))
            nd_row.append(int(data[5]))
            nd_row.append(int(data[6]))
            # append to the np array
            lsh_database.append(nd_row)

        return np.array(lsh_database)
