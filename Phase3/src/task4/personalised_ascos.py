from Phase3.src.task3.ascos import Ascos


def personalized_ascos(videos_path, path, frame_input, m):
    ascos = Ascos()
    graph, vertices, frame_indices = ascos.generate_adjacency_matrix(path, True, frame_input)
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
            ascos.visualise(info[0], info[1], videos_path, True)