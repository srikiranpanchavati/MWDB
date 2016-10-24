File Name: HistogramSimilarity.py
Author: Group 15

Usage: Gives the similarity measure between two videos based on their color histogram by using correlation, intersect, chisquare, bhattacharya, euclidean and manhattan distances.

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
1. in_file(in_file.chst) : Name with path of input file containing the color histograms
2. video_file_name_1(v_i) : Name of the first video being compared together with extension
3. video_file_name_2(v_j) : Name of the second video file together with extension
4. Distance measure: Integer number for the distance measure to find the similarity

Output:
Outputs the similarity between two videos by using correlation, intersect, chisquare, bhattacharya, euclidean and manhattan distances, depending on the input given, as a numerical value. In case of euclidean, manhattan, chisquare and bhattacharya lower value signifies more similarity. In case of intersect and correlation  higher value signifies more similarity


1. Run the HistogramSimilarity.py file in and IDE like PyCharm or the Python Shell 
2. Enter the correct path for input file, correct video names and integer 1,2,3,4,5,6 (for distance measure) when prompted 
3. The numerical output will be printed to the console