# class to get the motion vectors for two given files and return them as numpy arrays
import numpy as np

class MotionVectorHelper(object):
    def __init__(self, in_file, video_file_1, video_file_2):
        self.input_file = in_file
        self.video_file_name_1 = video_file_1
        self.video_file_name_2 = video_file_2

    '''parse the file for motion vectors of the two given video files and return numpy arrays'''
    def parseFile(self):
        '''open the file'''
        input_file_handle = open(self.input_file, 'r')

        '''empty numpy arrays for both video files'''
        video_array_1 = np.empty(shape=(0,9))
        video_array_2 = np.empty(shape=(0,9))
        
        '''scan the file for the particular videos'''
        # Loop counter
        i = 0
        while True:
            current_line = input_file_handle.readline()
            if not current_line: break
            # count the number of iterations
            i = i + 1
            raw_data_array = current_line.split(';')
            video_file_names = [self.video_file_name_1, self.video_file_name_2]
            if raw_data_array[0] in video_file_names:
                motion_vector = self.parseMotionVectors(raw_data_array[3])
                frame_and_block = raw_data_array[1:3]
                final_list = frame_and_block + motion_vector
                
                '''place the data in the respective numpy arrays'''
                final_list = map(int, final_list)
                if raw_data_array[0] == self.video_file_name_1:
                    video_array_1 = np.vstack([video_array_1, final_list])
                else:
                    video_array_2 = np.vstack([video_array_2, final_list])
            
            current_line = input_file_handle.readline()
            current_line = input_file_handle.readline()
            
        return video_array_1.astype(int), video_array_2.astype(int)
            
        

    def parseMotionVectors(self, input_string):
        '''clean the motion vector'''
        characters = ['\n',' ']
        ''' parse the motion vector'''
        for char in characters:
            output_string = input_string.replace(char, "")
        ''' strip out leading and trailing square brackets'''
        output_string = output_string[1:len(output_string)-2]
        output_string = output_string.split(',')
        return output_string

    
