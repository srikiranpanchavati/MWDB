File Name: videofeatues.py
Author: Sri Kiran Panchavati Ganesh

Purpose: Implements n-bin histogram and SIFT features corresponding to a cell of size r x r of a frame in a video.
Generates this report for all corresponding .mp4 files present in the input directory that is provided as an input.

Pre-requisites:
	1. Python 2.7.x
	2. openCV 2.4.13
	3. numpy
	4. scipy
	3. Windows environment
	
Installation:
	1. Download and install python 2.7.x version.
	2. Download and install OpenCV 2.4.13 version.
	3. Copy opencv\build\python\2.7\x86\cv2.pyd (distribution file) and place it in python installation location C:\Python27\Lib\site-packages
	4. Copy opencv\build\x86\vc12\bin\opencv_ffmpeg2413.dll and place it in C:\Python27
	5. Run the source file and the application prompts for the input below.
	

Input Params:
	1. Task : task1, task2, exit
		a. task1: Histogram generation
		b. task2: SIFT features generation
		c. exit: exit application.
		
	2. Input directory path:
		absolute location of the directory where the .mp4 files are present.
		eg: "G:\CSE515\Phase1\data"

	3. Output file name:
		name of the file (without extension) where the generated output has to be stored.
		adds .chst for histogram and .sift for SIFT features.
		will be generated in the current directory.

	4. Resolution (r) : 
		Size of the cell which corresponds to the r x r matrix each frame has to be divided
		value should be greater than 0.
		
	5. bin-size (n): 
		applicable only for task1 (histogram). Will not be prompted for task2
		value should be between 1 - 256
	
Output:
	Generates either a .chst or .sift file which contains the features extracted.
	File contents:
		task1.chst:  
			Contains histogram description of each cell corresponding to a frame in a video.
			output format:
				Video name; Frame number; Cell number; [ n-bin histogram ]
		task2.sift:
			Contains SIFT feature description of each cell corresponding to a frame in a video.
			output format:
				Video name; Frame number; Cell number; [ x-cordinate, y-cordinate, scale, orientation, [ descriptors a1 ... a128 ] ]
			
	
	
	
	
 