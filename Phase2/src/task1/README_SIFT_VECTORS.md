File Name: SiftSimilarity.py
Author: Group 15

Usage: Gives the similarity measure between two videos based on their Motion Vectors by using Manhattan and Chebyshev distance metrics.

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
1. in_file(in_file.sift) : Name with path of input file containing the SIFT Vectors
2. video_file_name_1(v_i) : Name of the first video being compared together with extension
3. video_file_name_2(v_j) : Name of the second video file together with extension
4. Distance measure: Integer number for the distance measure to find the similarity

Output:
Outputs the similarity between two videos using manhattan or chebyshev distance metrics, depending on the input given, as a numerical value. Lower value indicates higher similarity between the videos. 

1. Run the SiftVectorSimilarity.py file in and IDE like PyCharm or the Python Shell 
2. Enter the correct path for input file, correct video names and integer 1 or 2 (for distance measure) when prompted 
3. The numerical output will be printed to the console