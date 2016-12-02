from Phase3.src.utils.Pagerank_helper import Helper
from Phase3.src.task3.pageRank import PageRank
from Phase3.src.task3.ascos import Ascos

if __name__ == "__main__":
    __task = raw_input("Enter task1, task2 or exit : ")
    while __task.lower() != "exit":
        if __task.lower() == "task1":
            filename = raw_input("Enter input path of the graph file: ")
            m = raw_input("Enter the number of most significant frames to be found: ")
            vid_folder = raw_input("Enter path where the videos are stored: ")

            m = int(m)

            print "Processing... "
            h = Helper()

            graph = h.parse_data_from_file(filename)

            pageRank = PageRank()

            pr = pageRank.calc_pagerank(graph)

            #pr = nx.pagerank(graph)
            sorted_pr = sorted(pr.iteritems(), key=lambda x:-x[1])[:m]
            print "Pagerank in sorted order:  "
            for x in sorted_pr:
                pageRank.get_file_frame(x[0], x[1], vid_folder)

            output = vid_folder + "//" + "output_frames"
            pageRank.load_images(output)

        else:
            path = raw_input("Enter input graph file: ")
            m = int(raw_input("enter value of m: "))
            videos_path = raw_input("Enter videos location absolute path: ")

            ascos = Ascos()
            graph, vertices, frame_indices = ascos.generate_adjacency_matrix(path, False)
            page_rank = ascos.ascos_similarity(graph, frame_indices)
            if m > len(page_rank):
                print "invalid m value"
            else:
                frames = []
                for i in range(int(m)):
                    frames.append(vertices[page_rank[i][0]])

                cnt = 0
                for info in frames:
                    print "Video name: " + info[0]
                    print "Frame number: " + str(info[1])
                    print "Rank: " + str(page_rank[cnt][1])
                    print ("-------------------------------")
                    cnt += 1
                    ascos.visualise(info[0], info[1], videos_path, False)

        __task = raw_input("Enter task1, task2 or exit : ")