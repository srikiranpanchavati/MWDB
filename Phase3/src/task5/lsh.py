import os
import json
import numpy as np



class HashTable():
    def __init__(self, config):
        self.storage = dict()
    def insert_into_hash_table(self, key, value):
        self.storage.setdefault(key, []).append(value)


#C:\Users\nshaik2\Downloads\demo.spc
class LSH(object):

    def generate_uniform_planes(self):
        return np.random.randn(self.hash_size, self.input_dim)

    def convert_to_numpy_array(self,input_value):
        return np.array(input_value)

    def perform_dot_product(self,input_value1,input_value2):
        return np.dot(input_value1, input_value2)

    def convert_to_tuple(self,input_value):
        return tuple(input_value)

    def hash(self, planes, input_point):
        input_point = self.convert_to_numpy_array(input_point)
        projections = self.perform_dot_product(planes, input_point)
        output_hash = ""
        for i in projections:
            if i > 0:
                output_hash += "1"
            else:
                output_hash += "0"
        return output_hash



    def perform_lsh(self, input_value):
        value = self.convert_to_tuple(input_value)
        output = []
        for i, table in enumerate(self.hash_tables):
            x = self.hash(self.get_random_float_values[i], input_value)
            x = str(int(str(x), 2))
            table.insert_into_hash_table(x, value)
            line = str(i) + "," + x
            output.append(line)
        return output

    def __init__(self, no_of_buckets, no_of_dimensions, no_of_hashtables):
        self.hash_size = no_of_buckets
        self.input_dim = no_of_dimensions
        self.num_hashtables = no_of_hashtables
        self.storage_config = {'dict': None}
        #self.uniform_planes = [self.generate_uniform_planes()
         #                      for _ in xrange(self.num_hashtables)]
        self.get_random_float_values = []
        for i in range(0, self.num_hashtables):
            result = self.generate_uniform_planes()
            self.get_random_float_values.append(result)
        self.hash_tables = []
        for i in range(0,self.num_hashtables):
            result = storage(self.storage_config,i)
            self.hash_tables.append(result)



def storage(storage_config, index):
    return HashTable(storage_config['dict'])