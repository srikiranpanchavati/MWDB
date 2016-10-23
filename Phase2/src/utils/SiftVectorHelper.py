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

        # n = 9
        # with open(self.input_file) as myfile:
        #     while True:
        #         next_n_lines = list(islice(myfile, n))
        #         if not next_n_lines:
        #             break
        #         line = ''.join(next_n_lines)
        #         line = line.translate(None, '[]\n')
        #         feature = line.split(';')

        with open(self.input_file) as myfile:
            lines = myfile.read().splitlines()

        # print lines[0]

        video_file_names = [self.video_file_name_1, self.video_file_name_2]
        for line in lines:

            temp = line.split(';')
            if temp[0] in video_file_names:
                feature = []
                feature.append(int(temp[1]))
                feature.append(int(temp[2]))
                sift_info = temp[3].translate(None, '[]\n')
                desc = sift_info.split(',')
                for x in desc:
                    feature.append(float(x) if '.' in x else int(x))
                if(temp[0] == video_file_names[0]):
                    video_array_1.append(feature)
                else:
                    video_array_2.append(feature)


        # print len(video_array_1)
        # print len(video_array_2)
        return video_array_1, video_array_2


                # video_file_names = [self.video_file_name_1, self.video_file_name_2]
                # if feature[0] in video_file_names:
                #
                #     frame_block_sift_info = feature[1:7]
                #     frame_block_sift_info =  map(float, frame_block_sift_info)
                #
                #     descriptor = feature[7]
                #     descriptor = ','.join(descriptor.split())
                #     des_list =  [int(x) for x in descriptor.split(',') if x]
                #
                #     des_list = frame_block_sift_info +  des_list
                #     if feature[0] == self.video_file_name_1:
                #         video_array_1.append(des_list)
                #     else:
                #         video_array_2.append(des_list)
                #


                    #des_array = numpy.asarray(des_list)

                    #sift_features.append(des_array)

        # print (video_array_1[0])
        # print (video_array_2[0])
        # #return sift_features
        # return video_array_1, video_array_2

# if __name__ == "__main__":
#     obj = SiftVectorHelper("out.sift", "10R.mp4", "1R.mp4");
#     obj.parseFile()