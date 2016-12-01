import numpy as np
from src.utils.VideoSearchHelper import VideoSearchHelper


class VideoSearch(object):
    def __init__(self, lsh_database, n_objects):
        self.lsh_database = lsh_database
        self.n_objects = n_objects
        self.unique_sifts = 0
        self.total_sifts = 0
        self.data_size = 0

    def get_similar_videos(self, input_object):
        video_name, frame_number, x1, y1, x2, y2 = self.parse_query(input_object)
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        # retrieve all points
        # possible query points
        query_neighbours = []
        for rows in self.lsh_database:
            x_value = int(rows[5])
            y_value = int(rows[6])
            if str(rows[2]) != str(video_name) and x_min <= x_value <= x_max and y_min <= y_value <= y_max:
                query_neighbours.append(rows)

        # get the unique sift vectors
        unique_neighbours = np.delete(query_neighbours, [0, 1, 4, 5, 6], axis=1)

        new_array = np.ascontiguousarray(unique_neighbours).view(np.dtype((np.void,unique_neighbours.dtype.itemsize * unique_neighbours.shape[1])))
        _, idx = np.unique(new_array, return_index=True)
        uniques = unique_neighbours[idx]

        self.unique_sifts = len(uniques)

        # get the overall sift vectors
        self.total_sifts = len(query_neighbours)
        self.data_size = np.array(query_neighbours).nbytes

        # visualize the results..
        data = [row for row in uniques[:int(self.n_objects)]]

        return data


    def get_access_size(self):
        return self.data_size

    def get_unique_sifts(self):
        return self.unique_sifts

    def get_total_sifts(self):
        return self.total_sifts

    # method takes in the input query string and decomposes it into individual constituents
    @staticmethod
    def parse_query(input_query_string):
        data = input_query_string.split(",")
        video_name = str(data[0])
        frame_number = int(data[1])
        x1 = int(data[2])
        y1 = int(data[3])
        x2 = int(data[4])
        y2 = int(data[5])
        return video_name, frame_number, x1, y1, x2, y2


if __name__ == "__main__":
    __file_path = raw_input("input file path: ")
    __n = raw_input("Enter number of similar videos for retrieval: ")
    __query_object = raw_input("Enter the object as <i, j, x1, y1, x2, y2>")

    # apply pca..
    lsh_handler = VideoSearchHelper(__file_path)
    __lsh_database = lsh_handler.parse_lsh()

    video_searcher = VideoSearch(__lsh_database, __n)
    video_searcher.get_similar_videos(__query_object)
