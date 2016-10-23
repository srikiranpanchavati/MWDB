# TODO write docstring description for each method
import os.path
import sys

parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parent)

import numpy as np
from scipy.spatial import distance
from utils.MotionVectorHelper import MotionVectorHelper
from operator import itemgetter

class MotionVectorSimilarity:
    def __init__(self):
       pass

    # alter this function
    def euclidean_motionvector_similarity(self, array_1, array_2):
        i = 0
        euclidean_similarity = 0
        for i in range(min(len(array_1), len(array_2))):            
            euclidean_similarity += distance.euclidean(array_1[i,:], array_2[i,:])

        euclidean_similarity = euclidean_similarity / i
        
        return euclidean_similarity

    # alter this function
    def cosine_motionvector_similarity(self, array_1, array_2):
        i = 0
        cosine_similarity = 0
        for i in range(min(len(array_1), len(array_2))):            
            cosine_similarity += distance.cosine(array_1[i,:], array_2[i,:])

        cosine_similarity = cosine_similarity / i
        return cosine_similarity

    '''
        Method compares frames in video 1 with frame windows in video 2
        Add the distance measure, start frame number, and end frame number
        to a min heap
        compare the second set of frames to the index next to the root of min heap
    '''
    # video_array_1 and 2 containg the complete motion vectors for videos
    # split the videos into frames using helper function
    def cosine_motionvector_distance(self, video_array_1, video_array_2): 
        slice_length = 10
        start = 0
        end = start + slice_length
        cosine_similarity = 0
        # last frame number
        limit = video_array_2[len(video_array_2) - 1, 0]
        
        # slice of video_array_1 to be compared
        if end >= video_array_1[len(video_array_1) - 1, 0]:
            array_slice_1 = self.split_window(video_array_1, start, video_array_1[len(video_array_1) - 1, 0])
        else:
            array_slice_1 = self.split_window(video_array_1, start, end)

        # cast the array to integer
        array_slice_1 = array_slice_1.astype(int)
        print array_slice_1

        total_list = []
        
        # compare using windows
        while end <= limit:
            # process
            array_slice_2 = self.split_window(video_array_2, start, end)
            # get the distance measure
            for i in range(min(len(array_slice_1), len(array_slice_2))):            
                cosine_similarity += distance.cosine(array_slice_1[i,:], array_slice_2[i,:])
            cosine_similarity = cosine_similarity / min(len(array_slice_1), len(array_slice_2))
            print "Cosine Distance"
            print cosine_similarity
            print start
            print end
            # add distance, start, end to max heap
            distance_list = [cosine_similarity, start, end]
            total_list.append(distance_list)
                        
            start = start + 1
            end = end + 1

        sorted_list = sorted(total_list, key = itemgetter(0))

        # now find the cosine distance between the videos once you've found the first frame
        frame_start = sorted_list[0][1]
        iterations = 1
        frame_end = min(len(array_slice_1), len(array_slice_2))
        for i in range(min(len(array_1), len(array_2))):
            if video_array_1[i,0] > frame_start and video_array_2[i,0] > frame_start:
                cosine_similarity += distance.cosine(array_1[i,:], array_2[i,:])
                iterations += 1
        final_similarity = cosine_similarity / iterations

        return final_similarity, sorted_list
        
    '''
        Input: input_video_array - array containing all video motion vectors
        Output: partial array containing only the start and end frame numbers
        Returns: partial array
    '''
    def split_window(self, input_video_array, start, end):
        # empty numpy array
        window_slice = np.empty(shape=(0,9))
        i = 0
        # splits by including the start and end frame numbers
        for i in range(len(input_video_array)):
            if input_video_array[i][0] > start and input_video_array[i][0] <= end:
                window_slice = np.vstack([window_slice, input_video_array[i,:]])
                i += 1
        return window_slice.astype(int)           
            
    
mv = MotionVectorHelper("motionVector_10r.mvect", "10R.mp4", "1R.mp4")
array_1, array_2 = mv.parseFile()

ms = MotionVectorSimilarity()

ms.cosine_motionvector_distance(array_1, array_2)




