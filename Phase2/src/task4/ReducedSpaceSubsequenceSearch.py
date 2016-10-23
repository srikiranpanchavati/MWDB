from Phase2.src.task2.SubsequenceSearch import SubsequenceSearch


def reducedSpaceSearch():
    dir_path = "G:\\CSE515\\P2DemoVideos"#raw_input("Enter input directory path: ")
    vname = "6x_SQ_TL_BR_Check.mp4" #raw_input("Enter video file name: ")
    method_name = "MOTION_SIM2"#raw_input("Enter method name to be used for search: ")
    start_index = 1#raw_input("Enter start frame number: ")
    end_index = 15#raw_input("Enter end frame number: ")
    no_of_sequences = 5#raw_input("Enter number of sequences (K): ")
    feature_file  = "G:\\CSE515\\GitRepo\\MWDB\\Phase2\\sample_data\\input\\motionVector_2r.mvect"#raw_input("Enter feature file path: ")

    ssearch = SubsequenceSearch(dir_path, vname, feature_file, method_name, int(start_index), int(end_index), int(no_of_sequences))
    ssearch.save_video_sequence(None, start_index, end_index)
    ssearch.find_similar_frames()

if __name__ == "__main__":
    reducedSpaceSearch()