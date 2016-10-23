# TODO write docstring description for each method

import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
import scipy.spatial
import os.path
import sys
import fractions
parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parent)
#from utils.ColorHistogramHelper import *
from utils.ColorAndSiftHelper import *



class HistogramSimilarity:
	def __init__(self):
		pass

	def compute_similarity_correlation(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		l1 = len(hist_video1) # number of frames in first video
		l2 = len(hist_video2) # number of frames in second video
		first = []
		second = []
		if l1 == l2 or l1 < l2:
			first = hist_video1
			second = hist_video2
		else:
			first = hist_video2
			second = hist_video1
		l1 = len(first)
		l2 = len(second)
		step = int(round(l2/l1))
		for i,j in zip(range(0,l1),range(0,l2,step)):
			x = first[i] # list of histogram cells for a frame
			for k in range(j,j+step):
				y = second[k] # list of histogram cells for a frame
				for p,q in zip(x,y):
					result = cv2.compareHist(p,q,cv2.cv.CV_COMP_CORREL)
					sum += result
					count += 1
		print "The histogram similarity based on correlation is " + str(sum/count)


	def compute_similarity_chisquare(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		l1 = len(hist_video1) # number of frames in first video
		l2 = len(hist_video2) # number of frames in second video
		first = []
		second = []
		if l1 == l2 or l1 < l2:
			first = hist_video1
			second = hist_video2
		else:
			first = hist_video2
			second = hist_video1
		l1 = len(first)
		l2 = len(second)
		step = int(round(l2/l1))
		for i,j in zip(range(0,l1),range(0,l2,step)):
			x = first[i] # list of histogram cells for a frame
			for k in range(j,j+step):
				y = second[k] # list of histogram cells for a frame
				for p,q in zip(x,y):
					result = cv2.compareHist(p,q,cv2.cv.CV_COMP_CHISQR)
					sum += result
					count += 1
		print "The histogram similarity based on chisquare is " + str(sum/count)


	def compute_similarity_intersect(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		l1 = len(hist_video1) # number of frames in first video
		l2 = len(hist_video2) # number of frames in second video
		first = []
		second = []
		if l1 == l2 or l1 < l2:
			first = hist_video1
			second = hist_video2
		else:
			first = hist_video2
			second = hist_video1
		l1 = len(first)
		l2 = len(second)
		step = int(round(l2/l1))
		for i,j in zip(range(0,l1),range(0,l2,step)):
			x = first[i] # list of histogram cells for a frame
			for k in range(j,j+step):
				y = second[k] # list of histogram cells for a frame
				for p,q in zip(x,y):
					result = cv2.compareHist(p,q,cv2.cv.CV_COMP_INTERSECT)
					sum += result
					count += 1
		print "The histogram similarity based on intersect is " + str(sum/count)
	
	def compute_similarity_bhattacharya(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		l1 = len(hist_video1) # number of frames in first video
		l2 = len(hist_video2) # number of frames in second video
		first = []
		second = []
		if l1 == l2 or l1 < l2:
			first = hist_video1
			second = hist_video2
		else:
			first = hist_video2
			second = hist_video1
		l1 = len(first)
		l2 = len(second)
		step = int(round(l2/l1))
		for i,j in zip(range(0,l1),range(0,l2,step)):
			x = first[i] # list of histogram cells for a frame
			for k in range(j,j+step):
				y = second[k] # list of histogram cells for a frame
				for p,q in zip(x,y):
					result = cv2.compareHist(p,q,cv2.cv.CV_COMP_BHATTACHARYYA)
					sum += result
					count += 1
		print "The histogram similarity based on bhattacharya is " + str(sum/count)

	def compute_similarity_euclidean(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		l1 = len(hist_video1) # number of frames in first video
		l2 = len(hist_video2) # number of frames in second video
		first = []
		second = []
		if l1 == l2 or l1 < l2:
			first = hist_video1
			second = hist_video2
		else:
			first = hist_video2
			second = hist_video1
		l1 = len(first)
		l2 = len(second)
		step = int(round(l2/l1))
		for i,j in zip(range(0,l1),range(0,l2,step)):
			x = first[i] # list of histogram cells for a frame
			for k in range(j,j+step):
				y = second[k] # list of histogram cells for a frame
				for p,q in zip(x,y):
					result = scipy.spatial.distance.euclidean(p,q)
					sum += result
					count += 1
		print "The histogram similarity based on euclidean is " + str(sum/count)

	def compute_similarity_manhattan(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		l1 = len(hist_video1) # number of frames in first video
		l2 = len(hist_video2) # number of frames in second video
		first = []
		second = []
		if l1 == l2 or l1 < l2:
			first = hist_video1
			second = hist_video2
		else:
			first = hist_video2
			second = hist_video1
		l1 = len(first)
		l2 = len(second)
		step = int(round(l2/l1))
		for i,j in zip(range(0,l1),range(0,l2,step)):
			x = first[i] # list of histogram cells for a frame
			for k in range(j,j+step):
				y = second[k] # list of histogram cells for a frame
				for p,q in zip(x,y):
					result = scipy.spatial.distance.cityblock(p,q)
					sum += result
					count += 1
		print "The histogram similarity based on manhattan is " + str(sum/count)

	def extractHistograms(self,list1):
		l = []
		final_list = [] # This is a list of lists of histograms
		prev = 1
		for line in list1:
			frame_number = int(line[0])
			cell_number = line[1]
			hist_str = line[2][1:-1]
			hist = hist_str.split(",")
			len_of_hist = len(hist)
			histogram = np.array(hist).astype('float32').reshape((len(hist),1))
			#	print "Frame Number : " + str(frame_number),
			#	print "Cell Number : " + str(cell_number),
			#	print "Hist : " + str(hist_str)
			if frame_number == prev:
				l.append(histogram)
			else:
				final_list.append(l)
				l = []
				l.append(histogram)
				prev = frame_number
		final_list.append(l)
		return final_list


helper = ColorAndSiftHelper("/home/nisar/MWDB/Phase2/src/utils/hist.chst", "sift_file_name", "6x_SQ_BL_TM_BR_Check.mp4", "6x_SQ_BL_TM_BR_Noise.mp4")
list1,list2 = helper.parse_chst_files()
obj = HistogramSimilarity()
hist_video1 = obj.extractHistograms(list1)
hist_video2 = obj.extractHistograms(list2)
obj.compute_similarity_correlation(hist_video1,hist_video2)
obj.compute_similarity_chisquare(hist_video1,hist_video2)
obj.compute_similarity_intersect(hist_video1,hist_video2)
obj.compute_similarity_bhattacharya(hist_video1,hist_video2)
obj.compute_similarity_euclidean(hist_video1,hist_video2)
obj.compute_similarity_manhattan(hist_video1,hist_video2)

