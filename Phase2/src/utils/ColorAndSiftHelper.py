# Helper function to Extract the Color Histogram features into numpy arrays


class ColorAndSiftHelper(object):
    def __init__(self, chst_file_name, sift_file_name, video1_name, video2_name):
        self.chst_file_name = chst_file_name
        self.sift_file_name = sift_file_name
        self.video1_name = video1_name
        self.video2_name = video2_name

    def parse_chst_files(self):
        video1_hists = []
        video2_hists = []
        f = open(self.chst_file_name, "r")
        for line in f:
            if line.startswith(self.video1_name):
                line = line.strip(self.video1_name).strip(";").strip()
                video1_hists.append(line.split(';'))
            elif line.startswith(self.video2_name):
                line = line.strip(self.video2_name).strip(";").strip()
                video2_hists.append(line.split(';'))
        return video1_hists, video2_hists

    def parse(self):
        video1_sift_vectors = []
        video2_sift_vectors = []
        f = open(self.sift_file_name, "r")
        for line in f:
            if line.startswith(self.video1_name) or line.startswith(self.video2_name):
                line = line.translate(None, '[]\n')
                feature = line.split(';')


    def parse_sift_files(self):
        video1_sift_vectors = []
        video2_sift_vectors = []
        f = open(self.sift_file_name, "r")
        for line in f:
            if line.startswith(self.video1_name):
                line = line.strip(self.video1_name).strip(";").strip()
                #print line.split(';')
                video1_sift_vectors.append(line.split(';'))
            elif line.startswith(self.video2_name):
                line = line.strip(self.video2_name).strip(";").strip()
                video2_sift_vectors.append(line.split(';'))
        #print video1_sift_vectors
        # print video2_sift_vectors
        return video1_sift_vectors, video2_sift_vectors
