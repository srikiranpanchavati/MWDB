File Name: VideoSearch.py
Author: Group 15

Usage: This task deals with implementing a similarity based video object search such that frames with similar video objects are extracted. This task uses the results of the previous tasks. 

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

Input:
1. filename : Input path of the LSH file to be processed.
2. n : Number of similar video frames to be retrieved. 
3. video_path : Path where the videos are stored (needed to visualize the output)
3. query_object : The query object to be found in the as <i, j, x1, y1, x2, y2>

Output:
Prints the number of unique sift vectors considered, total number of vectors processed and the size of data processed (in bytes).
Visualizes all the resulting frames produced.

1. Run the pageRank.py file in and IDE like PyCharm or the Python Shell
2. Enter the correct path for filename, vid_folder and m
3. The pagerank output is printed in console
4. The output frames are stored in the video folder insider a new folder named 'output_frames'
5. Frames are saved in .jpeg format.