# TODO write docstring description for each method

import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
import scipy.spatial


class HistogramSimilarity:
    def __init__(self):
        pass

	def compute_similarity_correlation(dir):
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

	def compute_similarity_chisquare(dir):
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



	def compute_similarity_intersect(dir):
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




	def compute_similarity_bhattacharya(dir):
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
			result = cv2.compareHist(hist1,hist2,cv2.cv.CV_COMP_BHATTACHARYA)
			sum += result
			count += 1
		print "The similarity based on bhattacharya is " + str(sum/count) + "\n"


	def compute_similarity_euclidean(dir):
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

	def compute_similarity_manhattan(dir):
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
