# TODO write docstring description for each method
import os.path
import sys

parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parent)

import numpy as np
from scipy.spatial import distance
from Phase2.src.utils.MotionVectorHelper import MotionVectorHelper
from operator import itemgetter

class MotionVectorSimilarity:
    def __init__(self):
       pass

    '''
        Method compares frames in video 1 with frame windows in video 2 using sliding window mechanism
        Adds the distance measure, start frame number, and end frame number
        to a list
        Input Parameters: video_array_1 consisting motion vectors for video 1
                          video_array_2 consisting motion vectors for video 2
                          start_index(a)
                          end_index(b)
        Outputs:
                sorted list of all distances, start indexes and end indexes
        Distance Function: Cheybshev
    '''    
    def chebyshev_motionvector_array(self, video_array_1, video_array_2, start_index, end_index):
        slice_length = end_index - start_index
        start = start_index
        end = start + slice_length
        chebyshev_similarity = 0
        # last frame number
        limit = video_array_2[len(video_array_2) - 1][0]
        
        # slice of video_array_1 to be compared
        if end >= video_array_1[len(video_array_1) - 1][0]:
            array_slice_1 = self.split_window(video_array_1, start, video_array_1[len(video_array_1) - 1][0])
        else:
            array_slice_1 = self.split_window(video_array_1, start, end)

        total_list = []
        
        # compare using windows
        while end <= limit:
            # get the slice for video 2
            array_slice_2 = self.split_window(video_array_2, start, end)
            # get the distance measure
            for i in range(min(len(array_slice_1), len(array_slice_2))):            
                chebyshev_similarity += distance.chebyshev(array_slice_1[i], array_slice_2[i])
            chebyshev_similarity = chebyshev_similarity / min(len(array_slice_1), len(array_slice_2))
        
            # add distance, start, end to list
            distance_list = [chebyshev_similarity, start, end]
            total_list.append(distance_list)
                        
            start = start + 1
            end = end + 1

        sorted_list = sorted(total_list, key = itemgetter(0))

        return sorted_list

    '''
        Method compares frames in video 1 with frame windows in video 2 using sliding window mechanism
        Adds the distance measure, start frame number, and end frame number
        to a list
        Input Parameters: video_array_1 consisting motion vectors for video 1
                          video_array_2 consisting motion vectors for video 2
                          start_index(a)
                          end_index(b)
        Outputs:
                sorted list of all distances, start indexes and end indexes
        Distance Function: Manhattan
    '''    
    def manhattan_motionvector_array(self, video_array_1, video_array_2, start_index, end_index):
        slice_length = end_index - start_index
        start = start_index
        end = start + slice_length
        manhattan_similarity = 0
        # last frame number
        limit = video_array_2[len(video_array_2) - 1][0]
        
        # slice of video_array_1 to be compared
        if end >= video_array_1[len(video_array_1) - 1][0]:
            array_slice_1 = self.split_window(video_array_1, start, video_array_1[len(video_array_1) - 1][0])
        else:
            array_slice_1 = self.split_window(video_array_1, start, end)

        total_list = []
        
        # compare using windows
        while end <= limit:
            # get the slice for video 2
            array_slice_2 = self.split_window(video_array_2, start, end)
            # get the distance measure
            for i in range(min(len(array_slice_1), len(array_slice_2))):            
                manhattan_similarity += distance.cityblock(array_slice_1[i], array_slice_2[i])
            manhattan_similarity = manhattan_similarity / min(len(array_slice_1), len(array_slice_2))
        
            # add distance, start, end to list
            distance_list = [manhattan_similarity, start, end]
            total_list.append(distance_list)
                        
            start = start + 1
            end = end + 1

        # sort
        sorted_list = sorted(total_list, key = itemgetter(0))

        return sorted_list

    '''
        Overloaded manhattan distance function for TASK 1
        
        Method compares frames in video 1 with frame windows in video 2 using sliding window mechanism
        Adds the distance measure, start frame number, and end frame number
        to a list
        Input Parameters: video_array_1 consisting motion vectors for video 1
                          video_array_2 consisting motion vectors for video 2
        Outputs:
                sorted list of all distances, start indexes and end indexes
                Average Distance Metric
        Distance Function: Manhattan    
    '''
    def manhattan_motionvector_similarity(self, video_array_1, video_array_2): 
        slice_length = 10
        start = 0
        end = start + slice_length
        manhattan_similarity = 0
        # last frame number
        limit = video_array_2[len(video_array_2) - 1][0]
        
        # slice of video_array_1 to be compared
        if end >= video_array_1[len(video_array_1) - 1][0]:
            array_slice_1 = self.split_window(video_array_1, start, video_array_1[len(video_array_1) - 1][0])
        else:
            array_slice_1 = self.split_window(video_array_1, start, end)

        total_list = []
        
        # compare using windows
        while end <= limit:
            # get the slice for video 2
            array_slice_2 = self.split_window(video_array_2, start, end)
            # get the distance measure
            for i in range(min(len(array_slice_1), len(array_slice_2))):            
                manhattan_similarity += distance.cityblock(array_slice_1[i], array_slice_2[i])
            manhattan_similarity = manhattan_similarity / min(len(array_slice_1), len(array_slice_2))
        
            # add distance, start, end to list
            distance_list = [manhattan_similarity, start, end]
            total_list.append(distance_list)
                        
            start = start + 1
            end = end + 1

        # sort 
        sorted_list = sorted(total_list, key = itemgetter(0))

        # now find the manhattan distance between the videos once you've found the best frame
        frame_start = sorted_list[0][1]
        iterations = 1
        frame_end = min(len(array_slice_1), len(array_slice_2))        

        i = 0
        j = 0
        manhattan_similarity = 0
        while i < len(array_2) and j < len(array_1):
            if video_array_2[i][0] >= frame_start:
                manhattan_similarity += distance.cityblock(array_1[j], array_2[i])
                j += 1
            i += 1
        final_similarity = manhattan_similarity / j

        return final_similarity, sorted_list
    
    '''
        Overloaded chebyshev distance function for TASK 1
        
        Method compares frames in video 1 with frame windows in video 2 using sliding window mechanism
        Adds the distance measure, start frame number, and end frame number
        to a list
        Input Parameters: video_array_1 consisting motion vectors for video 1
                          video_array_2 consisting motion vectors for video 2
        Outputs:
                sorted list of all distances, start indexes and end indexes
                Average Distance Metric
        Distance Function: Chebyshev    
    '''
    def chebyshev_motionvector_similarity(self, video_array_1, video_array_2):
        slice_length = 10
        start = 0
        end = start + slice_length
        chebyshev_similarity = 0
        # last frame number
        limit = video_array_2[len(video_array_2) - 1][0]
        
        # slice of video_array_1 to be compared
        if end >= video_array_1[len(video_array_1) - 1][0]:
            array_slice_1 = self.split_window(video_array_1, start, video_array_1[len(video_array_1) - 1][0])
        else:
            array_slice_1 = self.split_window(video_array_1, start, end)

        total_list = []
        
        # compare using windows
        while end <= limit:
            # get slice for video 2
            array_slice_2 = self.split_window(video_array_2, start, end)
            # get the distance measure
            for i in range(min(len(array_slice_1), len(array_slice_2))):            
                chebyshev_similarity += distance.chebyshev(array_slice_1[i], array_slice_2[i])
            chebyshev_similarity = chebyshev_similarity / min(len(array_slice_1), len(array_slice_2))
        
            # add distance, start, end to list
            distance_list = [chebyshev_similarity, start, end]
            total_list.append(distance_list)
                        
            start = start + 1
            end = end + 1

        sorted_list = sorted(total_list, key = itemgetter(0))

        # now find the chebyshev distance between the videos once you've found the best frame
        frame_start = sorted_list[0][1]
        iterations = 1
        frame_end = min(len(array_slice_1), len(array_slice_2))

        i = 0
        j = 0
        while i < len(array_2) and j < len(array_1):
            if video_array_2[i][0] >= frame_start:
                chebyshev_similarity += distance.chebyshev(array_1[j], array_2[i])
                j += 1
            i += 1
        final_similarity = chebyshev_similarity / j

        return final_similarity, sorted_list
        
    '''
        Input: input_video_array - array containing all video motion vectors
        Output: partial array containing only the start and end frame numbers
        Returns: partial array
    '''
    def split_window(self, input_video_array, start, end):
        # empty numpy array
        window_slice = []
        i = 0
        # splits by including the start and end frame numbers
        for i in range(len(input_video_array)):
            if input_video_array[i][0] > start and input_video_array[i][0] <= end:
                window_slice.append(input_video_array[i])
                i += 1
        return window_slice

    def get_motion_manhattan(self, in_file, video_file_name_1, video_file_name_2, start_index, end_index):
        mv = MotionVectorHelper(in_file, video_file_name_1, video_file_name_2)
        array_1, array_2 = mv.parseFile()
        return_list = self.manhattan_motionvector_array(array_1, array_2, start_index, end_index)
        return return_list

    def get_motion_chebyshev(self, in_file, video_file_name_1, video_file_name_2, start_index, end_index):
        mv = MotionVectorHelper(in_file, video_file_name_1, video_file_name_2)
        array_1, array_2 = mv.parseFile()
        return_list = self.chebyshev_motionvector_array(array_1, array_2, start_index, end_index)
        return return_list

if __name__ == "__main__":
    in_file = raw_input("Enter the absolute path for .mvect file:")
    video_file_name_1 = raw_input("Enter the file name for the first video(with extension):")
    video_file_name_2 = raw_input("Enter the file name for the second video(with extension):")

    mv = MotionVectorHelper(in_file, video_file_name_1, video_file_name_2)
    array_1, array_2 = mv.parseFile()

    ms = MotionVectorSimilarity()
    similarity, sorted_list = ms.chebyshev_motionvector_similarity(array_1, array_2)
    print "Average Chebyshev Distance between %s and %s" %(video_file_name_1, video_file_name_2) 
    print similarity

    msi = MotionVectorSimilarity()
    similarity, sorted_list = ms.manhattan_motionvector_similarity(array_1, array_2)
    print "Average Manhattan Distance between %s and %s" %(video_file_name_1, video_file_name_2) 
    print similarity








