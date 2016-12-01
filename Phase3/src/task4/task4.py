from personalizedpagerank_helper import helper
from personalizedpagerank import find_personalized_page_rank, visualize
from personalised_ascos import personalized_ascos

# main function for task 4 for taking inputs and calling personalized page rank and ASCOS measures
if __name__ == "__main__":

    __task = raw_input("Enter task1, task2 or exit : ")
    while __task.lower() != "exit":
        if __task.lower() == "task1" or __task.lower() == "task2":
            # Reading input values for personalized page rank algorithm and personalized ASCOS measures
            path = raw_input("Enter absolute path of input graph file: ")
            m = int(raw_input("enter value of m: "))
            videos_path = raw_input("Enter absolute path of videos : ")
            input_frame1 = raw_input("Enter first reference video name and frame number (separated by ','): ").split(
                ",")
            input_frame2 = raw_input("Enter second reference video name and frame number (separated by ','): ").split(
                ",")
            input_frame3 = raw_input("Enter third reference video name and frame number (separated by ','): ").split(
                ",")
            if __task.lower() == "task1":
                __personalized_vector = [input_frame1[0] + input_frame1[1], input_frame2[0] + input_frame2[1], input_frame3[0] + input_frame3[1]]
                __damping_factor = float(raw_input("Enter damping factor: "))
                # call helper function to construct a directed graph
                __graph = helper(path)
                # call function to calculate personalized page ranks
                __ranks = find_personalized_page_rank(__graph, __damping_factor, __personalized_vector)
                # call function to visualize the output frames
                visualize(__ranks, videos_path, m)
            else:
                frame_input = [(input_frame1[0], int(input_frame1[1])),
                               (input_frame2[0], int(input_frame2[1])),
                               (input_frame3[0], int(input_frame3[1]))]
                personalized_ascos(videos_path, path, frame_input, m)
        else:
            print("Invalid input")
        __task = raw_input("Enter task1, task2 or exit : ")
