import cv2
import os
from Phase2.src.task1.MotionVectorSimilarity import MotionVectorSimilarity
from Phase2.src.task1.OverallSimilarity import OverallSimilarity
from Phase2.src.task1.SiftSimilarity import SiftSimilarity
from Phase2.src.task1.HistogramSimilarity import HistogramSimilarity

# This task takes an input video range compares with remaining videos in the database and returns k most similar
# video ranges in the given database and saves it to a specific folder to visualise
class SubsequenceSearch:

    # Constructor to subsequence search to initalize required data.
    def __init__(self, path=None, video=None, feature_path=None, feature_path2=None, method=None, start=0, end=0, k=0):
        self.directory_path = path
        self.video_name = video
        self.method_name = method
        self.a = start
        self.b = end
        self.k = k
        self.fetures_path = feature_path
        self.fetures_path2 = feature_path2
        self.out_path = os.path.join(self.directory_path, self.video_name.split(".")[0])
        if not os.path.exists(self.out_path):
            os.makedirs(self.out_path)

    # takes a video and range and writes sub video to a specific directory
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
            out_file_name = str(rank) + "_" + out_file_name  + "_result_"

        video_path = self.directory_path + "\\" + video_name

        video = cv2.VideoCapture(video_path)
        fourcc = cv2.cv.CV_FOURCC(*'XVID')
        out = cv2.VideoWriter(self.out_path + "\\" + out_file_name + ".avi", fourcc, video.get(cv2.cv.CV_CAP_PROP_FPS),
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

    # Calculates similarity between the input range of frames and and all videos in the database.
    def find_similar_frames(self):
        file_names = []
        for in_file in os.listdir(self.directory_path):
            if in_file.endswith(".mp4") and in_file != self.video_name:
                file_names.append(in_file)

        results = []
        sorted_results = []
        if(self.method_name == "HISTOGRAM_SIM1"):
            hist_sim = HistogramSimilarity()
            for name in file_names:
                temp = hist_sim.find_correlation_similarity_for_subsequence(self.fetures_path, self.video_name, name, self.a, self.b)[0]
                results.append((name, temp[0], temp[1][0], temp[1][1]))
            sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
        elif(self.method_name == "HISTOGRAM_SIM2"):
            hist_sim = HistogramSimilarity()
            for name in file_names:
                temp = hist_sim.find_intersection_similarity_for_subsequence(self.fetures_path, self.video_name, name, self.a, self.b)[0]
                results.append((name, temp[0], temp[1][0], temp[1][1]))
            sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
        elif(self.method_name == "SIFT_SIM1"):
            sift_sim1 = SiftSimilarity()
            for name in file_names:
                temp = sift_sim1.get_sift_chebyshev(self.fetures_path, self.video_name, name, self.a, self.b)[0]
                results.append((name, temp[0], temp[1], temp[2]))
            sorted_results = sorted(results, key=lambda x: x[1])
        elif(self.method_name == "SIFT_SIM2"):
            sift_sim1 = SiftSimilarity()
            for name in file_names:
                temp = sift_sim1.get_sift_manhattan(self.fetures_path, self.video_name, name, self.a, self.b)[0]
                results.append((name, temp[0], temp[1], temp[2]))
            sorted_results = sorted(results, key=lambda x: x[1])
        elif(self.method_name == "MOTION_SIM1"):
            mvsim = MotionVectorSimilarity()
            for name in file_names:
                temp = mvsim.get_motion_manhattan(self.fetures_path, self.video_name, name, self.a, self.b)[0]
                results.append((name, temp[0], temp[1], temp[2]))
            sorted_results = sorted(results, key=lambda x: x[1])
        elif(self.method_name == "MOTION_SIM2"):
            mvsim = MotionVectorSimilarity()
            for name in file_names:
                temp = mvsim.get_motion_chebyshev(self.fetures_path, self.video_name, name, self.a, self.b)[0]
                results.append((name, temp[0], temp[1], temp[2]))
            sorted_results = sorted(results, key=lambda x: x[1])
        elif(self.method_name == "OVERALL_SIM1"):
            overall_sim = OverallSimilarity(None, None, None, None)
            for name in file_names:
                temp = overall_sim.find_manhattan_similarity_for_subsequence(self.fetures_path, self.fetures_path2, self.video_name, name, self.a, self.b)[0]
                results.append((name, temp[0], temp[1][0], temp[1][1]))
            sorted_results = sorted(results, key=lambda x: x[1])
            print sorted_results
        elif(self.method_name == "OVERALL_SIM2"):
            overall_sim = OverallSimilarity(None, None, None, None)
            for name in file_names:
                temp = overall_sim.find_minkowski_similarity_for_subsequence(self.fetures_path, self.fetures_path2, self.video_name, name, self.a, self.b)[0]
                results.append((name, temp[0], temp[1][0], temp[1][1]))
            sorted_results = sorted(results, key=lambda x: x[1])
            print sorted_results

        for i in range (0, self.k):
            self.save_video_sequence(sorted_results[i][0],sorted_results[i][2], sorted_results[i][3], i+1)
        print sorted_results


if __name__ == "__main__":
    dir_path = "C:\\Users\\Giridhar\\Desktop\\MWDB Project\\P2DemoVideos"#raw_input("Enter input directory path: ")
    vname = "6x_TR_BL_TR_Noise.mp4" #raw_input("Enter video file name: ")
    method_name = "HISTOGRAM_SIM2"#raw_input("Enter method name to be used for search: ")
    start_index = 1#raw_input("Enter start frame number: ")
    end_index = 15#raw_input("Enter end frame number: ")
    no_of_sequences = 5#raw_input("Enter number of sequences (K): ")
    feature_file  = "C:\\Users\\Giridhar\\Desktop\\MWDB Project\\sift1.sift"#raw_input("Enter feature file path: ")
    feature_file2 = None
    if "OVERALL" in method_name:
        feature_file2 = "D:\\Education\\ASU\\MWD\\files\\phase2videos.sift"  # raw_input("Enter feature file path: ")

    ssearch = SubsequenceSearch(dir_path, vname, feature_file, feature_file2, method_name, int(start_index), int(end_index), int(no_of_sequences))
    ssearch.save_video_sequence(None, start_index, end_index)
    ssearch.find_similar_frames()