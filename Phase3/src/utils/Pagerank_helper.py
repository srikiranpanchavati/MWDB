__author__ = 'sjjai'

import networkx as nx
class Helper:
    def __init__(self):
        pass
    # takes absolute path of the features file and returns it as a 2-d list
    def parse_data_from_file(self, path):
        file = open(path, 'r')
        result_list = []
        for line in file:
            line_list = []
            line = line.replace(",", ";")
            data = line.split(";")
            line_list.append(data[0])
            line_list.append(data[1])
            line_list.append(data[5])
            line_list.append(data[6])
            line_list.append(data[10])
            result_list.append(line_list)

        return self.arr_to_graph(result_list)


    def arr_to_graph(self, data):
        DG = nx.DiGraph()

        for i, row in enumerate(data):

            node_a = self.node_format(row[0], row[1])
            node_b = self.node_format(row[2], row[3])


            DG.add_edge(node_a, node_b)
            DG.add_path([node_a, node_b])


        return DG

    def node_format(self, str1, str2):
        return ''.join([str1, str2])