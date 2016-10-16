import numpy as np


class Helper:
    def __init__(self):
        pass

    def get_histogram(self, path):
        file = open(path, 'r')
        histogram_list = []
        for line in file:
            line_list = []
            hist_data = line.split(";")
            line_list.append(hist_data[0])
            line_list.append(hist_data[1])
            line_list.append(hist_data[2])
            hist_data[3] = hist_data[3].replace("\\n", "").replace(" ", "").replace("[", "").replace("]","")
            line_list.append(map(int, hist_data[3].split(",")))
            histogram_list.append(line_list)

        return histogram_list
