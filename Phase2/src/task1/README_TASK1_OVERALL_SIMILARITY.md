File Name: OverallSimilarity.py
Author: Group 15

Usage: Gives the overall similarity measure between two videos based on color histogram similarity and sift vectors similarity by using Manhattan and Minkowski distance metrics.

Software Requirements:
  1. Windows based environment
  2. Python 2.7.x
  3. numpy packages for Python 2.7
  4. scipy packages for Python 2.7


System Requirements:
For optimum performance, the following system requirements are recommended
  1. 12GB or higher RAM
  2. Dual Core Intel/AMD processor
  3. 2GB or more free space on disk

Setup:
  1. Download and install suitable Python 2.7.x   version compiler
  2. Install numpy and scipy libraries for Python 2.7.x
  3. Alternatively get a python 2.7 implementation that comes pre-installed with these packages like
  Anacoda

  Input:
    1. chst_file_name(phase2videodemos.chst) : Name with path of input file containing the color histogram features for the given videos
	2. sift_file_name(phase2videodemos.sift) : Name with path of input file containing the sift vector features for the given videos
    3. video_file_name_1(v_i) : Name of the first video being compared together with extension
    4. video_file_name_2(v_j) : Name of the second video file being compared together with extension
	5. option : Choice of execution 1.Manhattan 2.Minkowski

Output:
  Outputs the overall similarity between two videos using manhattan and minkowski distance metrics, as a numerical value. Lower value indicates higher similarity between the videos.

  Running instructions:
    1. Run the OverallSimilarity.py file in and IDE like PyCharm or the Python Shell
    2. Enter the correct path for histogram file and sift vector file, correct video names when prompted
    3. The output will be printed to the console
