import cv2
import os
from Phase2.src.task1.MotionVectorSimilarity import MotionVectorSimilarity
import operator


class SubsequenceSearch:
    def __init__(self, path=None, video=None, feature_path=None, method=None, start=0, end=0, k=0):
        self.directory_path = path
        self.video_name = video
        self.method_name = method
        self.a = start
        self.b = end
        self.k = k
        self.fetures_path = feature_path

    def save_video_sequence(self, video_name=None, start=-1, end=-1, rank=-1):
        if video_name is None:
            video_name = self.video_name
        if start == -1:
            start = self.a
        if end == -1:
            end = self.b
        out_file_name = video_name.split(".")[0]
        if rank == -1:
            out_file_name += "_search_sequence"
        else:
            out_file_name += "_result_" + str(rank)

        video_path = self.directory_path + "\\" + video_name
        video = cv2.VideoCapture(video_path)
        fourcc = cv2.cv.CV_FOURCC(*'XVID')
        out = cv2.VideoWriter(self.directory_path + "\\out\\" + out_file_name + ".avi", fourcc, video.get(cv2.cv.CV_CAP_PROP_FPS),
                              (int(video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)),
                               int(video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))))
        frame_no = 0
        while video.isOpened():
            ret, frame = video.read()
            if ret:
                cv2.imshow("frame", frame)
                cv2.waitKey(100)
                if start <= frame_no <= end:
                    out.write(frame)
            else:
                break
            frame_no += 1


        out.release()
        video.release()
        cv2.destroyAllWindows()

    def find_similar_frames(self):
        # captures all the video files (.mp4) present in the specified directory.
        file_names = []
        for in_file in os.listdir(self.directory_path):
            if in_file.endswith(".mp4") and in_file != self.video_name:
                file_names.append(in_file)

        results = []
        if(self.method_name == "HISTOGRAM_SIM1"):
            for name in file_names:
                pass
        elif(self.method_name == "HISTOGRAM_SIM2"):
            for name in file_names:
                pass
        elif(self.method_name == "SIFT_SIM1"):
            for name in file_names:
                pass
        elif(self.method_name == "SIFT_SIM2"):
            for name in file_names:
                pass
        elif(self.method_name == "MOTION_SIM1"):
            mvsim = MotionVectorSimilarity()
            for name in file_names:
                temp = mvsim.get_motion_manhattan(self.fetures_path, self.video_name, name, self.a, self.b)[0]
                results.append((name, temp[0], temp[1], temp[2]))
        elif(self.method_name == "MOTION_SIM2"):
            for name in file_names:
                pass
        elif(self.method_name == "OVERALL_SIM1"):
            for name in file_names:
                pass
        elif(self.method_name == "OVERALL_SIM2"):
            for name in file_names:
                pass
        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
        for i in range (0, self.k):
            self.save_video_sequence(sorted_results[i][0],sorted_results[i][2], sorted_results[i][3], i+1)
        print sorted_results


if __name__ == "__main__":
    dir_path = "C:\\Users\\Giridhar\\Desktop\\MWDB Project\\P2DemoVideos"#raw_input("Enter input directory path: ")
    vname = "6x_SQ_TL_BR_Check.mp4" #raw_input("Enter video file name: ")
    method_name = "MOTION_SIM1"#raw_input("Enter method name to be used for search: ")
    start_index = 1#raw_input("Enter start frame number: ")
    end_index = 15#raw_input("Enter end frame number: ")
    no_of_sequences = 5#raw_input("Enter number of sequences (K): ")
    feature_file  = "C:\\Users\\Giridhar\\Desktop\\MWDB Project\\MWDB\\Phase2\\sample_data\\input\\motionVector_2r.mvect"#raw_input("Enter feature file path: ")

    ssearch = SubsequenceSearch(dir_path, vname, feature_file, method_name, int(start_index), int(end_index), int(no_of_sequences))
    ssearch.find_similar_frames()