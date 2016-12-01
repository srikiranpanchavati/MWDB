import math
import numpy as np
import collections
import operator
import cv2
import os


class Ascos:
    def generate_adjacency_matrix(self, input_path, isPersonalised, input_frames=None):
        input_data = []
        vertices = []
        cnt = 0
        for line in open(input_path):
            data = line.replace("\n","").split(",")
            v0 = (data[0], int(data[1]))
            v1 = (data[2], int(data[3]))
            sim = float(data[4])

            row = []
            if v0 not in vertices:
                vertices.append(v0)
                cnt += 1

            if v1 not in vertices:
                vertices.append(v1)
                cnt += 1

            input_data.append([vertices.index(v0), vertices.index(v1), sim])

        graph = [[0 for i in range(cnt)] for j in range(cnt)]

        for row in input_data:
            graph[row[0]][row[1]] = row[2]
        # graph = np.transpose(graph)

        if isPersonalised:
            frame_indices = [vertices.index(input_frames[0]), vertices.index(input_frames[1]), vertices.index(input_frames[2])]
            self.personalise_graph(graph, frame_indices)

        return graph, vertices

    def personalise_graph(self, graph, frame_indices):
        for i in frame_indices:
            graph[i] = [x + (0.15 / 3) for x in graph[i]]

    def has_converged(self, prev_matrix, curr_matrix, iterator):
        if iterator >= 300:
            print iterator
            return True
        return np.array_equal(prev_matrix, curr_matrix)

    def get_in_neighbours(self,graph, in_neighbours_dict, length):
        transpose_matrix = np.transpose(graph)
        for i in range(length):
            for x in range(length):
                if 0 < transpose_matrix[i][x] < 1:
                    in_neighbours_dict[i].append(x)

    def calculate_similarity(self, prev_matrix, curr_matrix,in_neighbours_dict, i, j):
        if i == j:
            curr_matrix[i][j] = 1
            return

        w_i_all = 0.0
        for n in prev_matrix[i]:
            if n >= 0:
                w_i_all += n

        in_neighbours = in_neighbours_dict[i]
        for k in in_neighbours:
            if prev_matrix[i][k] >= 0 and w_i_all != 0:
                curr_matrix[i][j] += (prev_matrix[i][k] / w_i_all)*(1 - math.exp(-1 * prev_matrix[i][k]))*prev_matrix[k][j]
                curr_matrix[i][j] = round(curr_matrix[i][j], 4)

    def ascos_similarity(self, graph):
        length = len(graph)
        prev_matrix = []
        curr_matrix = graph
        in_neighbours_dict = collections.defaultdict(list)
        self.get_in_neighbours(graph, in_neighbours_dict, length)
        iterator = 0
        while not self.has_converged(prev_matrix, curr_matrix, iterator):
            iterator += 1
            prev_matrix = curr_matrix
            for i in range(length):
                for j in range(length):
                    self.calculate_similarity(prev_matrix, curr_matrix, in_neighbours_dict, i, j)

        page_rank = collections.defaultdict(float)
        for j in range(length):
            for i in range(length):
                page_rank[j] += curr_matrix[i][j]

            page_rank[j] /= length

        page_rank = sorted(page_rank.items(), key=operator.itemgetter(1), reverse=True)
        return page_rank

    def visualise(self, video_name, frame_number, videos_path, is_personalised):
        if is_personalised:
            out_dir = videos_path + "//" + "personalised_ascos_output_frames"
        else:
            out_dir = videos_path + "//" + "ascos_output_frames"

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        capture = cv2.VideoCapture(os.path.join(videos_path, video_name))
        frame = None
        count = 1
        while capture.isOpened():
            is_read, frame = capture.read()
            if not is_read:
                break
            if count == frame_number:
                break
            count += 1

        write_loc = out_dir + "//"+ video_name + "_frame_" + str(frame_number) + ".jpeg"
        cv2.imshow(video_name + "_frame_" + str(frame_number), frame)
        cv2.imwrite(write_loc, frame)
        cv2.waitKey(1000)
        capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    path = raw_input("Enter input graph file: ")
    m = int(raw_input("enter value of m: "))
    videos_path = raw_input("Enter videos location absolute path: ")

    ascos = Ascos()
    graph, vertices = ascos.generate_adjacency_matrix(path, False)
    page_rank = ascos.ascos_similarity(graph)
    if m > len(page_rank):
        print "invalid m value"
    else:
        frames = []
        for i in range(int(m)):
            frames.append(vertices[page_rank[i][0]])
        print(frames)
        cnt = 0
        for info in frames:
            print "Video name: " + info[0]
            print "Frame number: " + str(info[1])
            print "Rank: " + str(page_rank[cnt][1])
            print ("-------------------------------")
            cnt += 1
            ascos.visualise(info[0], info[1], videos_path, False)
