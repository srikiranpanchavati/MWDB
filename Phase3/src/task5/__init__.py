
from lshash import *

sift_features_info = []
sift_features = []
no_of_dims = 0

def extract_features(file_name):
    file_pointer = open(file_name, "r")
    for line in file_pointer:
        line = line.split("[")
        feature_info = line[0].strip()
        feature_info = feature_info[:-1]
        feature_info = feature_info.replace(",",";")
        feature = line[1].strip()
        feature = feature[:-1]
        #no_of_dims = len(feature.split())
        #print no_of_dims
        feature = [float(i) for i in feature.split()]
        sift_features_info.append(feature_info)
        sift_features.append(feature)


if __name__ == '__main__':
    print "Enter the location of the .spc file"
    file_name = raw_input()
    output_file_name = file_name.split(".")
    output_file_name = output_file_name[0]
    file_writer = open(output_file_name + ".lsh" ,"w")
    extract_features(file_name)
    no_of_dims = len(sift_features[0])
    print no_of_dims
    print "Enter the number of hash tables"
    num_of_hash_functions = int(raw_input())
    print "Enter the number of buckets per hash function (in powers of 2). Example : If you need 8 buckets input 3"
    num_of_buckets = int(raw_input())
    lsh = LSHash(hash_size=num_of_buckets, input_dim=no_of_dims, num_hashtables=num_of_hash_functions)
    for i in range(0,len(sift_features)):
        feature_info = sift_features_info[i]
        feature = sift_features[i]
        output = lsh.index(feature)
        for j in range(0,len(output)):
            file_writer.write(output[j] + "," + feature_info)
            file_writer.write("\n")
    file_writer.close()

