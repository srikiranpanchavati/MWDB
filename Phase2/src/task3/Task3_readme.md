Phase 2 - video Retrieval
Task 3 - Dimensionality Reduction
Files: pca.py and Kmeans.py
Author: Group 15

Purpose: Given a set of features vectors of a set of object. Dimensionality reduction is achieved by using PCA and Kmeans transformations
Outputs a feature vector file similar to input but will now contain reduced dimensions 'd' where is specified as part of input.

Pre-requisites:

	1. Python 2.7.x
	2. openCV 2.4.13
	3. numpy
	4. scipy
	5. scikit-learn
	6. Windows environment
	
Installation:

	1. Download and install python 2.7.x version.
	2. Download and install OpenCV 2.4.13 version.
	3. Copy opencv\build\python\2.7\x86\cv2.pyd (distribution file) and place it in python installation location C:\Python27\Lib\site-packages
	4. Copy opencv\build\x86\vc12\bin\opencv_ffmpeg2413.dll and place it in C:\Python27
	5. Run the corresponding source file either pca or kmeans and the application prompts for the input below.
	
PCA: 
	Input:
		1. Input file path: absolute path of the data file containing the video details and features (.chst, .sift or .mvect)
		2. new dimensions (d): number to which the original feature vector has to be reduced. (value should be less than or equal to original dimensions).
	
	Output: 
		1. Generates a .cpca or .spca or .mpca based on the input feature file and stores in the directory path of the iput file with the same name along with '_d' where 'd' is the number of new dimensions after reduction.		
		2. File contents:
			1. .cpca:  contains file name, frame number, cell number and reduced feature dimensions of histogram.
			2. .spca:  contains file name, frame number, cell number and reduced feature dimensions of SIFT.
			3. .pca:  contains file name, frame number, cell number and reduced feature dimensions of motion vectors.
		3. Displays the original index and score values of the 'd' reduced dimensions on the program console as (original_index, score).
		
KMeans: 
	Input:
		1. Input file path: absolute path of the data file containing the video details and features (.chst, .sift or .mvect)
		2. new dimensions (d): number to which the original feature vector has to be reduced. (value should be less than or equal to original dimensions).
	
	Output: 
		1. Generates a .ckm or .skm or .mkm based on the input feature file and stores in the directory path of the iput file with the same name along with '_d' where 'd' is the number of new dimensions after reduction.		
		2. File contents:
			1. .cpca:  contains file name, frame number, cell number and reduced feature dimensions of histogram
			2. .spca:  contains file name, frame number, cell number and reduced feature dimensions of SIFT.
			3. .pca:  contains file name, frame number, cell number and reduced feature dimensions of motion vectors.
		3. Displays the original index and score values of the 'd' reduced dimensions on the program console as (original_index, score).
			
			
	
