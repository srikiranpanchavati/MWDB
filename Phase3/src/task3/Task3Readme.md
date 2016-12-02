File Name: Task3.py
Author: Group 15

Usage: Applies pagerank and ascos on the graph

Software Requirements:
  1. Windows based environment
  2. Python 2.7.x
  3. numpy packages for Python 2.7
  4. scipy packages for Python 2.7
  5. OpenCV packages for Python 2.7
  6. NetworkX packages for Python 2.7


System Requirements:
For optimum performance, the following system requirements are recommended
  1. 12GB or higher RAM
  2. Dual Core Intel/AMD processor
  3. 2GB or more free space on disk

Setup:
  1. Download and install suitable Python 2.7.x   version compiler
  2. Install numpy and scipy libraries for Python 2.7.x
  3. Alternatively get a python 2.7 implementation that comes pre-installed with these packages like Anacoda

Page Rank:
Input:
1. Enter task 1, task2 or exit: enter task2 here
2. filename : Input path of the graph file to be processed
3. m : Number of most significant frames to be found
4. vid_folder : Path where the videos are stored (needed to visualize the output)

Output:
Prints the filename, frame-number and Pagerank value for top m frames.
Visualizes all the frames produced.
stored in the video folder insider a new folder named 'output_frames'

ASCOS
Input:
1. Enter task 1, task2 or exit: enter task2 here
2. filename : Input path of the graph file to be processed
3. m : Number of most significant frames to be found
4. vid_folder : Path where the videos are stored (needed to visualize the output)

Output:
Prints the filename, frame-number and Pagerank value for top m frames.
Visualizes all the frames produced.
stored in the video folder insider a new folder named 'ascos_output_frames'

Execution Instructions
1. Run the pageRank.py file in and IDE like PyCharm or the Python Shell
2. enter task to be executed (task1 or task2) or enter exit to finish
3. Enter the correct path for filename, vid_folder and m
4. The pagerank output is printed in console
5. The output frames are stored in the video folder insider a new folder named 'output_frames' for page rank
6. The output frames are stored in the video folder insider a new folder named 'output_frames' for ascos
7. Frames are saved in .jpeg format.