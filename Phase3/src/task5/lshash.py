# lshash/lshash.py
# Copyright 2012 Kay Zhu (a.k.a He Zhu) and contributors (see CONTRIBUTORS.txt)
#
# This module is part of lshash and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import json
import numpy as np

from storage import storage

try:
    from bitarray import bitarray
except ImportError:
    bitarray = None

class LSHash(object):
    def __init__(self, hash_size, input_dim, num_hashtables=1,
                 storage_config=None, matrices_filename=None, overwrite=False):

        self.hash_size = hash_size
        self.input_dim = input_dim
        self.num_hashtables = num_hashtables

        if storage_config is None:
            storage_config = {'dict': None}
        self.storage_config = storage_config

        self.matrices_filename = matrices_filename
        self.overwrite = overwrite

        self._init_uniform_planes()
        self._init_hashtables()

    def _init_uniform_planes(self):
        if "uniform_planes" in self.__dict__:
            return

        if self.matrices_filename:
            file_exist = os.path.isfile(self.matrices_filename)
            if file_exist and not self.overwrite:
                try:
                    npzfiles = np.load(self.matrices_filename)
                except IOError:
                    print("Cannot load specified file as a numpy array")
                    raise
                else:
                    npzfiles = sorted(npzfiles.items(), key=lambda x: x[0])
                    self.uniform_planes = [t[1] for t in npzfiles]
            else:
                self.uniform_planes = [self._generate_uniform_planes()
                                       for _ in xrange(self.num_hashtables)]
                try:
                    np.savez_compressed(self.matrices_filename,
                                        *self.uniform_planes)
                except IOError:
                    print("IOError when saving matrices to specificed path")
                    raise
        else:
            self.uniform_planes = [self._generate_uniform_planes()
                                   for _ in xrange(self.num_hashtables)]

    def _init_hashtables(self):
        self.hash_tables = [storage(self.storage_config, i)
                            for i in xrange(self.num_hashtables)]

    def _generate_uniform_planes(self):
        return np.random.randn(self.hash_size, self.input_dim)

    def _hash(self, planes, input_point):
        try:
            input_point = np.array(input_point)  # for faster dot product
            projections = np.dot(planes, input_point)
        except TypeError as e:
            print("""The input point needs to be an array-like object with
                  numbers only elements""")
            raise
        except ValueError as e:
            print("""The input point needs to be of the same dimension as
                  `input_dim` when initializing this LSHash instance""", e)
            raise
        else:
            return "".join(['1' if i > 0 else '0' for i in projections])


    def index(self, input_point, extra_data=None):
        if isinstance(input_point, np.ndarray):
            input_point = input_point.tolist()

        if extra_data:
            value = (tuple(input_point), extra_data)
        else:
            value = tuple(input_point)

        output = []
        for i, table in enumerate(self.hash_tables):
            x = self._hash(self.uniform_planes[i], input_point)
            x = str(int(str(x),2))
            table.append_val(self._hash(self.uniform_planes[i], input_point),
                             value)
            line = str(i) + "," + x
            #print "line :" + line
            output.append(line)
        return output

