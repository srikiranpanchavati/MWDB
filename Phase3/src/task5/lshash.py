import os
import json
import numpy as np
from storage import storage

bitarray = None
#/home/nisar/Downloads/phase3/test.spc
class LSHash(object):

    def __init__(self, hash_size, input_dim, num_hashtables=1):
        self.hash_size = hash_size
        self.input_dim = input_dim
        self.num_hashtables = num_hashtables
        storage_config = {'dict': None}
        self.storage_config = storage_config
        self._init_uniform_planes()
        self._init_hashtables()


    def _init_uniform_planes(self):
        if "uniform_planes" in self.__dict__:
            return
        self.uniform_planes = [self._generate_uniform_planes()
                                       for _ in xrange(self.num_hashtables)]

    def _init_hashtables(self):
        self.hash_tables = [storage(self.storage_config, i)
                            for i in xrange(self.num_hashtables)]

    def _generate_uniform_planes(self):
        return np.random.randn(self.hash_size, self.input_dim)


    def _hash(self, planes, input_point):
        input_point = np.array(input_point)
        projections = np.dot(planes, input_point)
        return "".join(['1' if i > 0 else '0' for i in projections])

    def index(self, input_point):
        if isinstance(input_point, np.ndarray):
            input_point = input_point.tolist()
        value = tuple(input_point)
        output = []
        for i, table in enumerate(self.hash_tables):
            x = self._hash(self.uniform_planes[i], input_point)
            x = str(int(str(x), 2))
            table.append_val(self._hash(self.uniform_planes[i], input_point),
                             value)
            line = str(i) + "," + x
            output.append(line)
        return output
