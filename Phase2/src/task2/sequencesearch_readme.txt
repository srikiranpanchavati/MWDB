Purpose: 
In this program we try to find K most similar sequences in the database to that of the given video sequence. We take video name, start frame and end frame as input and extract the frame sequence as video and store it for visualization. We also take a feature file as input and we use it to calculate the similarity of the input frame sequence with all other videos present in the database. We then find K most similar sequences and store them as videos for visualization.

Pre-requisites:
1. Python 2.7.x
2. openCV 2.4.13
3. OS
3. Windows environment

Installation:
1. Download and install python 2.7.x version.
2. Download and install OpenCV 2.4.13 version.
3. Copy opencv\build\python\2.7\x86\cv2.pyd (distribution file) and place it in python installation location C:\Python27\Lib\site-packages
4. Copy opencv\build\x86\vc12\bin\opencv_ffmpeg2413.dll and place it in C:\Python27
5. Run the source file and the application prompts for the input below.

Input Params:
1. Enter input directory path:
    absolute location of the directory where the .mp4 files are present.
    eg: "G:\CSE515\Phase2\data"

2. Enter video file name:
    name of the video file (without extension) which has to be taken as input for the search.

3. Enter method name to be used for search:
    Enter the similarity measure that needs to be used for searching. Give one of the following keys
		"HISTOGRAM_SIM1": Finding similarity using color histograms as features and Correlation Similarity as similarity measure
        "HISTOGRAM_SIM2": Finding similarity using color histograms as features and Intersection Similarity as similarity measure
        "SIFT_SIM1": Finding similarity using SIFT vectors as features and Chebyshev distance as distance measure
        "SIFT_SIM2": Finding similarity using SIFT vectors as features and Manhattan distance as distance measure
        "MOTION_SIM1": Finding similarity using Motion vectors as features and Manhattan distance as distance measure
        "MOTION_SIM2": Finding similarity using Motion vectors as features and Chebyshev distance as distance measure
        "OVERALL_SIM1": Finding similarity using color histograms and SIFT vectors as features and Manhattan distance as distance measure
		"OVERALL_SIM2": Finding similarity using color histograms and SIFT vectors as features and Minkowski distance as distance measure

4. Enter start frame number: 
    Enter the number of the starting frame of the input video sequence.

5. Enter end frame number: 
    Enter the number of the ending frame of the input video sequence.

6. Enter number of sequences (K): 
    Enter the number of sequences to be retrieved

7. Enter feature file path: 
    Enter absolute path of the file that contains features required for the similarity/distance measure used in algorithm.
	
8. Enter second feature file path:
    If over all similarity is being used then you will be prompted with this additional input. Enter the absolute path of the file that has SIFT features for the videos present in database.

Output: 
	This program will store the input video sequence in a folder named with input video name in the input directory path entered as input. It also ranks K most similar sequences present in the database video and stores them in the same folder. These videos are ranked as per maximum similarity. These videos are also displayed while execution to visualize the input and output. 
	
Decisions Made:
	This program will identify all the sequences in each video of database file. It then finds the similarity with each sequence and picks the sequence that has highest similarity. This sequnce alone is considered for extracting the K most similar sequences. This means that in output there will not be two sequences from the same video.