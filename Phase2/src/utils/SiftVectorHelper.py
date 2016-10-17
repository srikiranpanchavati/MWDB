#Helper function to Extract the Sift features in numpy arrays

import numpy
from itertools import islice

class SiftVectorHelper(object):
    def __init__(self, in_file, video_file_1, video_file_2):
        self.input_file = in_file
        self.video_file_name_1 = video_file_1
        self.video_file_name_2 = video_file_2

    def parseFile(self):
        sift_features = []

        video_array_1 = []
        video_array_2 = []

        n = 9
        with open(self.input_file) as myfile:
            while True:
                next_n_lines = list(islice(myfile, n))
                if not next_n_lines:
                    break
                line = ''.join(next_n_lines)
                line = line.translate(None, '[]\n')
                feature = line.split(';')

                video_file_names = [self.video_file_name_1, self.video_file_name_2]
                if feature[0] in video_file_names:

                    frame_block_sift_info = feature[1:7]
                    frame_block_sift_info =  map(float, frame_block_sift_info)

                    descriptor = feature[7]
                    descriptor = ','.join(descriptor.split())
                    des_list =  [int(x) for x in descriptor.split(',') if x]

                    des_list = frame_block_sift_info +  des_list
                    if feature[0] == self.video_file_name_1:
                        video_array_1.append(des_list)
                    else:
                        video_array_2.append(des_list)
                    #des_array = numpy.asarray(des_list)

                    #sift_features.append(des_array)

        # print len(video_array_1)
        # print  len(video_array_2)
        #return sift_features
        return video_array_1, video_array_2
#
# if __name__ == "__main__":
#     obj = SiftHelper("sift.sift", "10R.mp4", "1R.mp4");
#     obj.parseFile()