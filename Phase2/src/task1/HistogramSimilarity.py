# TODO write docstring description for each method

import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
import scipy.spatial
import os.path
import sys
parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parent)
from utils.ColorHistogramHelper import *


class HistogramSimilarity:
	def __init__(self):
		pass

	def compute_similarity_correlation(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		for x, y in izip(hist_video1,hist_video2):
			result = cv2.compareHist(x,y,cv2.cv.CV_COMP_CORREL)
			sum += result
			count += 1
		print "The similarity based on correlation is " + str(sum/count)

	
	def compute_similarity_chisquare(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		for x, y in izip(hist_video1,hist_video2):
			result = cv2.compareHist(x,y,cv2.cv.CV_COMP_CORREL)
			sum += result
			count += 1
		print "The similarity based on chisquare is " + str(sum/count)


	def compute_similarity_intersect(self,hist_video1,hist_video2):

		sum = 0.0
		count = 0
		for x, y in izip(hist_video1,hist_video2):
			result = cv2.compareHist(x,y,cv2.cv.CV_COMP_INTERSECT)
			sum += result
			count += 1
		print "The similarity based on intersect is " + str(sum/count)


	def compute_similarity_bhattacharya(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		for x, y in izip(hist_video1,hist_video2):
			result = cv2.compareHist(x,y,cv2.cv.CV_COMP_BHATTACHARYYA)
			sum += result
			count += 1
		print "The similarity based on bhattacharya is " + str(sum/count)
	

	def compute_similarity_euclidean(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		for x, y in izip(hist_video1,hist_video2):
			result = scipy.spatial.distance.euclidean(x,y)
			sum += result
			count += 1
		print "The similarity based on euclidean is " + str(sum/count)


	def compute_similarity_manhattan(self,hist_video1,hist_video2):
		sum = 0.0
		count = 0
		for x, y in izip(hist_video1,hist_video2):
			result = scipy.spatial.distance.cityblock(x,y)
			sum += result
			count += 1
		print "The similarity based on manhattan is " + str(sum/count)




helper = ColorHistogramHelper()
hist_video1,hist_video2 = helper.parseFiles("/home/nisar/Desktop/dir1")

obj = HistogramSimilarity()
obj.compute_similarity_correlation(hist_video1,hist_video2)
obj.compute_similarity_chisquare(hist_video1,hist_video2)
obj.compute_similarity_intersect(hist_video1,hist_video2)
obj.compute_similarity_bhattacharya(hist_video1,hist_video2)
obj.compute_similarity_euclidean(hist_video1,hist_video2)
obj.compute_similarity_manhattan(hist_video1,hist_video2)






'''
These functions can be used when we want to just pass the directory with videos.
These were written earlier when the helper was not written

def compute_similarity_correlation(self,dir):
		vids = glob.glob(dir + "/*.mp4")
		vidcap1 = cv2.VideoCapture(vids[0])
		vidcap2 = cv2.VideoCapture(vids[1])
		success1,image1 = vidcap1.read()
		count = 0
		success1 = True
		success2,image2 = vidcap2.read()
		count2 = 0
		success2 = True
		sum = 0.0
		while success1 == True and success2 == True:
			success1,image1 = vidcap1.read()
			success2,image2 = vidcap2.read()
			hist1 = cv2.calcHist([image1],[0],None,[256],[0,256])
			hist2 = cv2.calcHist([image2],[0],None,[256],[0,256])
			result = cv2.compareHist(hist1,hist2,cv2.cv.CV_COMP_CORREL)
			sum += result
			count += 1
		print "The similarity based on correlation is " + str(sum/count) + "\n"

def compute_similarity_chisquare(self,dir):
		vids = glob.glob(dir + "/*.mp4")
		vidcap1 = cv2.VideoCapture(vids[0])
		vidcap2 = cv2.VideoCapture(vids[1])
		success1,image1 = vidcap1.read()
		count = 0
		success1 = True
		success2,image2 = vidcap2.read()
		count2 = 0
		success2 = True
		sum = 0.0
		while success1 == True and success2 == True:
			success1,image1 = vidcap1.read()
			success2,image2 = vidcap2.read()
			hist1 = cv2.calcHist([image1],[0],None,[256],[0,256])
			hist2 = cv2.calcHist([image2],[0],None,[256],[0,256])
			result = cv2.compareHist(hist1,hist2,cv2.cv.CV_COMP_CHISQR)
			sum += result
			count += 1
		print "The similarity based on chisquare is " + str(sum/count) + "\n"

def compute_similarity_intersect(self,dir):
		vids = glob.glob(dir + "/*.mp4")
		vidcap1 = cv2.VideoCapture(vids[0])
		vidcap2 = cv2.VideoCapture(vids[1])
		success1,image1 = vidcap1.read()
		count = 0
		success1 = True
		success2,image2 = vidcap2.read()
		count2 = 0
		success2 = True
		sum = 0.0
		while success1 == True and success2 == True:
			success1,image1 = vidcap1.read()
			success2,image2 = vidcap2.read()
			hist1 = cv2.calcHist([image1],[0],None,[256],[0,256])
			hist2 = cv2.calcHist([image2],[0],None,[256],[0,256])
			result = cv2.compareHist(hist1,hist2,cv2.cv.CV_COMP_INTERSECT)
			sum += result
			count += 1
		print "The similarity based on intersect is " + str(sum/count) + "\n"

def compute_similarity_bhattacharya(self,dir):
		vids = glob.glob(dir + "/*.mp4")
		vidcap1 = cv2.VideoCapture(vids[0])
		vidcap2 = cv2.VideoCapture(vids[1])
		success1,image1 = vidcap1.read()
		count = 0
		success1 = True
		success2,image2 = vidcap2.read()
		count2 = 0
		success2 = True
		sum = 0.0
		while success1 == True and success2 == True:
			success1,image1 = vidcap1.read()
			success2,image2 = vidcap2.read()
			hist1 = cv2.calcHist([image1],[0],None,[256],[0,256])
			hist2 = cv2.calcHist([image2],[0],None,[256],[0,256])
			result = cv2.compareHist(hist1,hist2,cv2.cv.CV_COMP_BHATTACHARYYA)
			sum += result
			count += 1
		print "The similarity based on bhattacharya is " + str(sum/count) + "\n"

def compute_similarity_manhattan(self,dir):
		vids = glob.glob(dir + "/*.mp4")
		vidcap1 = cv2.VideoCapture(vids[0])
		vidcap2 = cv2.VideoCapture(vids[1])
		success1,image1 = vidcap1.read()
		count = 0
		success1 = True
		success2,image2 = vidcap2.read()
		count2 = 0
		success2 = True
		sum = 0.0
		while success1 == True and success2 == True:
			success1,image1 = vidcap1.read()
			success2,image2 = vidcap2.read()
			hist1 = cv2.calcHist([image1],[0],None,[256],[0,256])
			hist2 = cv2.calcHist([image2],[0],None,[256],[0,256])
			result = scipy.spatial.distance.cityblock(hist1,hist2)
			sum += result
			count += 1
		print "The similarity based on manhattan is " + str(sum/count) + "\n"

def compute_similarity_euclidean(self,dir):
		vids = glob.glob(dir + "/*.mp4")
		vidcap1 = cv2.VideoCapture(vids[0])
		vidcap2 = cv2.VideoCapture(vids[1])
		success1,image1 = vidcap1.read()
		count = 0
		success1 = True
		success2,image2 = vidcap2.read()
		count2 = 0
		success2 = True
		sum = 0.0
		while success1 == True and success2 == True:
			success1,image1 = vidcap1.read()
			success2,image2 = vidcap2.read()
			hist1 = cv2.calcHist([image1],[0],None,[256],[0,256])
			hist2 = cv2.calcHist([image2],[0],None,[256],[0,256])
			result = scipy.spatial.distance.euclidean(hist1,hist2)
			sum += result
			count += 1
		print "The similarity based on euclidean is " + str(sum/count) + "\n"


'''

