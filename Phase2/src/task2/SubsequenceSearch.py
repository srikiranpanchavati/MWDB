import cv2


class SubsequenceSearch:
    def __init__(self, path=None, video=None, method=None, start=0, end=0, k=0):
        self.directory_path = path
        self.video_name = video
        self.method_name = method
        self.a = start
        self.b = end
        self.k = k

    def save_video_sequence(self, video_name=None, start=-1, end=-1, order=-1):
        if video_name is None:
            video_name = self.video_name
        if start == -1:
            start = self.a
        if end == -1:
            end = self.b
        out_file_name = video_name.split(".")[0]
        if order == -1:
            out_file_name += "_search_sequence"
        else:
            out_file_name += "_result_" + str(order)

        video_path = self.directory_path + "\\" + video_name
        video = cv2.VideoCapture(video_path)
        fourcc = cv2.cv.CV_FOURCC(*'X264')
        out = cv2.VideoWriter(out_file_name + '.mp4', fourcc, 20.0, (640, 480))
        frame_no = 0
        while video.isOpened():
            ret, frame = video.read()
            if ret:
                if start <= frame_no <= end:
                    out.write(frame)
            else:
                break
            frame_no += 1


        out.release()
        video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    dir_path = raw_input("Enter input directory path: ")
    vname = raw_input("Enter video file name: ")
    method_name = raw_input("Enter method name to be used for search: ")
    start_index = raw_input("Enter start frame number: ")
    end_index = raw_input("Enter end frame number: ")
    no_of_sequences = raw_input("Enter number of sequences (K): ")

    ssearch = SubsequenceSearch(dir_path, vname, method_name, int(start_index), int(end_index), int(no_of_sequences))
    ssearch.save_video_sequence()