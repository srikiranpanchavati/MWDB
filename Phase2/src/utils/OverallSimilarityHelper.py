# Helper function to Extract the Color Histogram and SIFT features into numpy arrays
import numpy as np
from itertools import islice
import csv


class OverallSimilarityHelper(object):
    def __init__(self, chst_file_name, sift_file_name, video1_name, video2_name):
        self.chst_file_name = chst_file_name
        self.sift_file_name = sift_file_name
        self.video1_name = video1_name
        self.video2_name = video2_name

    def parse_chst_files(self):
        video1_hists = []
        video2_hists = []
        f = open(self.chst_file_name, "r")
        for line in f:
            if line.startswith(self.video1_name):
                temp_line = line.strip(self.video1_name).strip(";").strip()
                video1_hists.append(temp_line.split(';'))
            if line.startswith(self.video2_name):
                temp_line = line.strip(self.video2_name).strip(";").strip()
                video2_hists.append(temp_line.split(';'))
        return self.extractHistograms(video1_hists), self.extractHistograms(video2_hists)

    def parse_sift_files(self):
        video1_sifts = []
        video2_sifts = []
        f = open(self.sift_file_name, "r")
        for line in f:
            if line.startswith(self.video1_name):
                temp_line = line.strip(self.video1_name).strip(";").strip()
                video1_sifts.append(temp_line.split(';'))
            if line.startswith(self.video2_name):
                temp_line = line.strip(self.video2_name).strip(";").strip()
                video2_sifts.append(temp_line.split(';'))
        return self.extractHistograms(video1_sifts), self.extractHistograms(video2_sifts)

    def extractHistograms(self, list1):
        l = []
        final_list = []  # This is a list of lists of histograms
        prev = 1
        for line in list1:
            frame_number = int(line[0])
            cell_number = line[1]
            hist_str = line[2][1:-1]
            hist = hist_str.split(",")
            len_of_hist = len(hist)
            histogram = np.array(hist).astype('float32').reshape((len(hist), 1))
            #print "Frame Number : " + str(frame_number),
            #print "Cell Number : " + str(cell_number),
            #print "Hist : " + str(hist_str)
            if frame_number == prev:
                l.append(histogram)
            else:
                final_list.append(l)
                l = []
                l.append(histogram)
                prev = frame_number
        final_list.append(l)
        #print final_list
        return final_list


def execute():
    helper_obj = OverallSimilarityHelper("D:\\Education\\ASU\\MWD\\files\\test.chst", "D:\\Education\\ASU\\MWD\\files\\test.sift", "6x_SQ_BL_TM_BR_Check.mp4", "6x_SQ_BL_TM_BR_Noise.mp4")
    v1, v2 = helper_obj.parse_chst_files()
    v1_sift, v2_sift = helper_obj.parse_sift_files()
    with open("D:\\Education\\ASU\\MWD\\files\\output.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(v1_sift)


execute()