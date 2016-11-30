import itertools as IT


class SiftWriter(object):
    def __init__(self, out_file):
        self.out_file = out_file

    def write_to_file(self, sift_points, sift_descriptors):
        __file_stream = open(self.out_file, "a")

        for data in IT.izip(sift_points, sift_descriptors):
            write_string_1 = ",".join(str(x) for x in data[0])
            write_string_2 = "[" + " ".join(str(x) for x in data[1]) + "]"
            write_string = write_string_1 + "," + write_string_2
            __file_stream.write("%s\n" % write_string)
        __file_stream.close()
        print("Done writing to file!")
