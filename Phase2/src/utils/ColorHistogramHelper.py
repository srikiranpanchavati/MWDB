#Helper function to Extract the Color Histogram features into numpy arrays
'''
This helper was written according to my output during the phase1.
'''

from itertools import izip
import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
import scipy.spatial


class ColorHistogramHelper(object):
    #def __init__(self, in_file, video_file_1, video_file_2):
     #   self.input_file = in_file
      #  self.video_file_name_1 = video_file_1
       # self.video_file_name_2 = video_file_2
        #pass

    
    def parseFiles(self,dir):
        vids = glob.glob(dir + "/*.chst")
        f1 = open(vids[0],"r")
        f2 = open(vids[1],"r")
        count = 0
        hists_video1 = []
        hists_video2 = []
        for x, y in izip(f1,f2):
            l1 = x.split(';')
            l2 = y.split(';')
            h1 = l1[3].strip()
            h2 = l2[3].strip()
            a1 = h1.split('  ')
            array1 = np.array(a1).astype('float32').reshape((len(a1),1))
            a2 = h2.split('  ')
            array2 = np.array(a2).astype('float32').reshape((len(a2),1))
            hists_video1.append(array1)
            hists_video2.append(array2)
        return hists_video1,hists_video2

    


#obj = ColorHistogramHelper()
#obj.parseFiles("/home/nisar/Desktop/dir1")
