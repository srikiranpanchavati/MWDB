class Helper:
    def __init__(self):
        pass

    def parse_data_from_file(self, path):
        file = open(path, 'r')
        result_list = []
        for line in file:
            line_list = []
            data = line.split(";")
            line_list.append(data[0])
            line_list.append(data[1])
            line_list.append(data[2])
            data[3] = data[3].replace("\\n", "").replace(" ", "").replace("[", "").replace("]","")
            line_list.append(map(float, data[3].split(",")))
            result_list.append(line_list)

        return result_list
