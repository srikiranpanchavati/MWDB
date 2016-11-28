
def format_sift(sift_file):
    """
    :param sift_file:
    convert input file to two arrays
        1. 2d array <video_name, frame_no, cell_no, x, y>
        2. 2d array <scale, orientation, des0, des1,..., des128>
        Maintain proper indexing
    :return:
        1, 2
    """
    pass


def pca(inp_array):
    """
    :param inp_array:
    Execute PCA on inp_array
        1. features in new dimension
        2. scores<original_index, score>
        "Score is a vector not a single point
        "Score should be sorted by eigen values
        Maintain proper indexing
    :return:
        1, 2
    """
    pass


def write_output(arr1, arr3, file_name):
    """
    write to output file in below format
    <V, F, C, x, y, [dimi, . . . , dimd]

    """
    pass

if __name__ == "__main__":
    """
    Read Input from the user <Sift file, target dimensions>
    Call method format_sift()
        1. arr1
        2. arr2
    Call PCA(arr2)
        3. new feature set
        4. scores
    Call write_output(1, 3, file_name)
    Print scores(4) on console
    """
    pass