from Phase3.src.task3.ascos import Ascos

if __name__ == "__main__":
    path = raw_input("Enter input graph file: ")
    m = int(raw_input("enter value of m: "))
    videos_path = raw_input("Enter videos location absolute path: ")
    input_frame1 = raw_input("Enter first reference video name and frame number (separated by ','): ").split(",")
    input_frame2 = raw_input("Enter second reference video name and frame number (separated by ','): ").split(",")
    input_frame3 = raw_input("Enter third reference video name and frame number (separated by ','): ").split(",")

    frame_input = [(input_frame1[0], int(input_frame1[1])),
                   (input_frame2[0], int(input_frame2[1])),
                   (input_frame3[0], int(input_frame3[1]))]

    ascos = Ascos()
    graph, vertices = ascos.generate_adjacency_matrix(path, True, frame_input)
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
            ascos.visualise(info[0], info[1], videos_path)


