Task 5 is intended to take in a .spc file generated in Task 1 and output the bucket and the hash table into which each of the reduced SIFT features are inserted into.

Input :

The inputs are prompted when we run the code

.spc file -> The file which contains reduced SIFT features one per line in the format as below.

	video_name,frame_number,cell_number,X,Y,< d dimensional vector> 

L -> The number of hash functions or layers 

k -> The number of buckets in each hash table

Output :

One line per reduced SIFT feature in the below format

hash_function,bucket_number,video_name;frame_number;cell_number;X;Y