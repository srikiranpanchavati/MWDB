File Name: task4.py
Author: Group 15

Usage: Applies personalised_page_rank and personalised_ascos on the graph created by task 2.

Software Requirements:
  1. Windows based environment
  2. Python 2.7.x
  3. numpy packages for Python 2.7
  4. scipy packages for Python 2.7
  5. OpenCV packages for Python 2.7


System Requirements:
For optimum performance, the following system requirements are recommended
  1. 12GB or higher RAM
  2. Dual Core Intel/AMD processor
  3. 2GB or more free space on disk

Setup:
  1. Download and install suitable Python 2.7.x   version compiler
  2. Install numpy and scipy libraries for Python 2.7.x
  3. Alternatively get a python 2.7 implementation that comes pre-installed with these packages like Anacoda

Input for both personlaized page rank :
1. filename : Input path of the graph file to be processed
2. m : Number of most significant frames to be found
3. video_path : Path where the videos are stored (needed to visualize the output)
4. input_reference_frame1: first input reference frame in format <video_name>,<frame_number> (eg: 10mp4,20)
5. input_reference_frame2: second input reference frame in format <video_name>,<frame_number> (eg: 10mp4,20)
6. input_reference_frame2: third input reference frame in format <video_name>,<frame_number> (eg: 10mp4,20)
7. damping factor: percentage of preference to be given to user preferences 

Example:
Enter task1, task2 or exit : task1
Enter absolute path of input graph file: D:\Education\ASU\MWD\SampleData_10.gspc
enter value of m: 5
Enter absolute path of videos : D:\Education\ASU\MWD\P3DemoVideos
Enter first reference video name and frame number (separated by ','): 3.mp4,19
Enter second reference video name and frame number (separated by ','): 3.mp4,24
Enter third reference video name and frame number (separated by ','): 1.mp4,22


Output:
Prints the filename, frame-number and rank value for top m frames.
Visualizes all the frames produced.
stores the frames as .jpeg in personalisedpr_output_frames folder in video_path directory

Input for both personlaized ascos :
1. filename : Input path of the graph file to be processed
2. m : Number of most significant frames to be found
3. video_path : Path where the videos are stored (needed to visualize the output)
4. input_reference_frame1: first input reference frame in format <video_name>,<frame_number> (eg: 10mp4,20)
5. input_reference_frame2: second input reference frame in format <video_name>,<frame_number> (eg: 10mp4,20)
6. input_reference_frame2: third input reference frame in format <video_name>,<frame_number> (eg: 10mp4,20)

Example:
Enter task1, task2 or exit : task2
Enter absolute path of input graph file: D:\Education\ASU\MWD\SampleData_10.gspc
enter value of m: 5
Enter absolute path of videos : D:\Education\ASU\MWD\P3DemoVideos
Enter first reference video name and frame number (separated by ','): 3.mp4,19
Enter second reference video name and frame number (separated by ','): 3.mp4,24
Enter third reference video name and frame number (separated by ','): 1.mp4,22

Output:
Prints the filename, frame-number and rank value for top m frames.
Visualizes all the frames produced.
stores the frames as .jpeg in personalised_ascos_output_frames folder in video_path directory

Run instructions:

1. Run the task4.py file in and IDE like PyCharm or the Python Shell
2. Enter the correct path for filename, video_path, m and three input reference frames and for task1 damping factor
3. The rank output is printed in console along with video name and frame number
4. The output frames are stored in the video folder insider a new folder named 'personalisedpr_output_frames for task1' and 'personalised_ascos_output_frames' for task 2
5. Frames are saved in .jpeg format.
