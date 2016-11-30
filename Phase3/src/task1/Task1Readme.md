File Name: HistogramSimilarity.py
Author: Group 15

Usage: Applies PCA on SIFT features and gives the SIFT descriptors with reduced dimensionality in terms of the resulting PC axes.

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
  3. Alternatively get a python 2.7 implementation that comes pre-installed with these packages like Anacoda

Input:
1. in_file(infile.sift) : Name with path of input file containing the SIFT vectors
2. n_dimensions(d) : Target dimensionality of the reduced feature space

Output:
Outputs the SIFT descriptors with target dimensions to out_file.spc
Scores of each PC axes are printed to the console along with their original indexes

1. Run the HistogramSimilarity.py file in and IDE like PyCharm or the Python Shell
2. Enter the correct path for input file, target dimensionality between 1 and 127
3. The output SIFT features are written to 'out_file.spc'
4. The scores for each of the 'd' PC axes along with their original indexes
