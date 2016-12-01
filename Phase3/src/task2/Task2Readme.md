File Name: SimilarityGraph.py
Author: Group 15

Usage: Creates a similarity graph of k most similar frames from dimensionality reduced SIFT vector file.

Proposed Solution:
  1. Every frame is compared with all the other frames except the frames in the same video.
  2. While comparing two frames, for every sift point present in the source frame a closest sift point is found in the destination frame using 1-Nearest Neighbour algorithm.
  3. Distance between them is calculated using Euclidean distance measure
  4. Average of all the distances of the key points present in source file is computed.
  5. This average distance is converted to similarity value between 1 and 0.
  6. Here 1 means more similar and 0 means least similar
  7. This similarity value is computed for the source frame with all other frames in all other videos.
  8. K most similar frames are selected and written to output file.

Software Requirements:
  1. Windows based environment
  2. Python 2.7.x
  3. numpy packages for Python 2.7
  4. scipy packages for Python 2.7
  5. OpenCV packages for Python 2.7
  6. scikit-learn packages for Python 2.7


System Requirements:
For optimum performance, the following system requirements are recommended
  1. 12GB or higher RAM
  2. Dual Core Intel/AMD processor
  3. 2GB or more free space on disk

Setup:
  1. Download and install suitable Python 2.7.x version compiler
  2. Install numpy and scipy libraries for Python 2.7.x
  3. Alternatively get a python 2.7 implementation that comes pre-installed with these packages like Anacoda

Input:
  1. filename : Absolute path of the input sift vector file with extension. Sift key points in the input file should be in the format
            <i, j, l, x, y, [dim_1, . . . , dim_n]>
    where i --> Video name
          j --> Frame Number
          x --> X coordinate of SIFT vector
          y --> Y coordinate of SIFT vector
          dim_k --> Dimensionally reduced features
  2. K : Number of similar frames that need to be present for each frame in the vector graph

Output:
  1. Generates a file with name "<file_name>_k.gspc" in the same directory as that of the input file.
  2. Similarity graph is stored in this file in below format
            <va,vb,sim>
    where va --> (i,j) from the input of the source frame
          vb --> (i,j) from the input of the target frame
          sim --> Similarity Value of the frame


1. Run the SimilarityGraph.py file in and IDE like PyCharm or the Python Shell
2. Enter the absolute path of input file when prompted
3. Enter an Integer value less than the total number of frames when prompted for k value
4. The output is stored to the file "<file_name>_k.gspc" in the same directory as that of the input file.
