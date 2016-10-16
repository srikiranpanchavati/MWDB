import cv2
import os


class VideoFeatures(object):
    # Constructor
    def __init__(self, task, in_dir, resolution, bin_size, file_stream):
        self.__task = task
        self.__dir = in_dir
        self.__resolution = resolution
        self.__bin_size = bin_size
        self.__file_stream = file_stream
        self.__frame_count = 1
        self.__cell_count = 1
        self.__in_file_name = ""

    # read video from current project and data folder.
    def read_video_files(self):
        # captures all the video files (.mp4) present in the specified directory.
        for in_file in os.listdir(self.__dir):
            if in_file.endswith(".mp4"):
                self.__in_file_name = in_file

                # Capture video from specified location
                __capture = cv2.VideoCapture(os.path.join(self.__dir, in_file))

                self.__extract_features(__capture)

    # extract video features like color histogram, SIFT features and motion vectors of the given input video.
    def __extract_features(self, capture):
        # frame number count
        self.__frame_count = 1
        # isOpened checks if the video was successfully captured.
        while capture.isOpened():

            # reads each frame and returns true and frame if video is read, Otherwise false and None.
            __is_read, __frame = capture.read()

            # if frames are completed read() returns false.
            if not __is_read:
                break

            # Calculate histogram
            if self.__task == "task1":
                self.__divide_into_blocks(__frame)
            elif self.__task == "task2":
                key_points, descriptors = self.__extract_sift(__frame)
                self.__divide_into_blocks(__frame, key_points, descriptors)
            else:
                cv2.imshow("frame", __frame)

            self.__frame_count += 1

        capture.release()
        cv2.destroyAllWindows()

    # Divides the given frame into r x r cell
    # where r is the resolution provided by the user.
    def __divide_into_blocks(self, frame, key_points=None, descriptors=None):
        __frame_height = len(frame)
        __frame_width = len(frame[0])
        __row_start = 0
        __row_end = __frame_height / self.__resolution
        self.__cell_count = 1

        # Loop to divide each frame into r x r cells.
        for i in range(self.__resolution):
            __col_start = 0
            __col_end = __frame_width / self.__resolution
            for j in range(self.__resolution):
                # Conditions to divide the frame into r x r cells.
                if i == self.__resolution - 1 and j == self.__resolution - 1:
                    __row_end = __frame_height
                    __col_end = __frame_width
                elif i == self.__resolution - 1:
                    __row_end = __frame_height
                elif j == self.__resolution - 1:
                    __col_end = __frame_width

                # Conditions to check which task has to be performed on cell.
                if self.__task == "task1":
                    cell = frame[__row_start: __row_end, __col_start: __col_end]
                    self.__create_color_histogram(cell)
                elif self.__task == "task2":
                    self.__create_sift_features(__row_start, __row_end, __col_start, __col_end, key_points, descriptors)

                self.__cell_count += 1
                __col_start = __col_end
                __col_end = __col_start + __frame_width / self.__resolution
            __row_start = __row_end
            __row_end = __row_start + __frame_height / self.__resolution

    # Calculate histogram for each logically divided cell from the original frame.
    def __create_color_histogram(self, cell):
        # Calculates histogram and return a matrix of size hist_size x 1
        # Where hist_size is then number of bins provided by the user as input.
        __histogram_matrix = cv2.calcHist([cell], [0], None, [self.__bin_size], [0, 256])
        __histogram = [int(__histogram_matrix[i][0]) for i in range(len(__histogram_matrix))]

        # Formatted data that will be added to the .chst file.
        __data = "%s; %d; %d; %s \n\n"\
                 % (self.__in_file_name, self.__frame_count, self.__cell_count, __histogram)

        self.__file_stream.write(__data)

    # Extracts SIFT features for the complete frame.
    def __extract_sift(self, frame):
        __sift = cv2.SIFT()
        return __sift.detectAndCompute(frame, None)

    # divides the SIFT features into their corresponding logical blocks.
    def __create_sift_features(self, row_start, row_end, col_start, col_end, key_points, descriptors):
        for i in range(len(key_points)):
            if key_points[i] is not None and \
               row_start <= round(key_points[i].pt[0]) <= row_end and \
               col_start <= round(key_points[i].pt[1]) <= col_end:
                    __data = "%s; %s; %s; [ %s; %s; %s; %s; %s ];\n\n"\
                             % (self.__in_file_name, self.__frame_count, self.__cell_count,
                                int(round(key_points[i].pt[0])), int(round(key_points[i].pt[1])),
                                round(key_points[i].size/2, 4), round(key_points[0].angle, 4), descriptors[i].astype(int))

                    self.__file_stream.write(__data)

# main function
if __name__ == "__main__":
    # Takes task, input directory, output file, resolution and number of bins as input from the user.
    # to Exit from the application enter exit

    __task = raw_input("Enter task (task1, task2) or (exit) to exit : ")
    while __task.lower() != "exit":
        if __task.lower() == "task1" or __task.lower() == "task2":
            # Input values common to all tasks.
            __in_dir = raw_input("Enter input directory path: ")
            __out_file = raw_input("Enter output file name without extension: ")
            __resolution = __bin_size = 1
            __ext = __print_format = ""

            try:
                __resolution = int(raw_input("Enter resolution: "))
            except ValueError:
                print "Not a number"

            if __resolution < 1:
                print "invalid resoultion."
                __task = raw_input("Enter task (task1, task2) or (exit) to exit : ")
                continue

            # Input values specific to each task.
            if __task.lower() == "task1":
                try:
                    __bin_size = int(raw_input("Enter histogram size (a value greater than 0): "))
                    if __bin_size < 1 or __bin_size > 256:
                        print "Invalid bin size."
                        __task = raw_input("Enter task (task1, task2) or (exit) to exit : ")
                        continue
                except ValueError:
                    print "Not a number"
                __ext = ".chst"
                __print_format = "Histogram output format: FileName; Frame number; Cell number; [%d - bin histogram]\n\n"\
                                 % __bin_size
            else:
                __ext = ".sift"
                __print_format = ""

            #  Open/create(if not available) output file.
            __file_name = __out_file + __ext
            __file_stream = open(__file_name, "a")
            __file_stream.write(__print_format)
            print "Processing..."

            # Extract Video features.
            video_features = VideoFeatures(__task.lower(), __in_dir, __resolution, __bin_size, __file_stream)
            video_features.read_video_files()

            # close file stream.
            __file_stream.close()

            print "Done!"
        else:
            print "Invalid input for task."
        __task = raw_input("Enter task (task1, task2) or (exit) to exit : ")
