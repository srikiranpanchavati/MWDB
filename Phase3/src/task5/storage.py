# lshash/storage.py
# Copyright 2012 Kay Zhu (a.k.a He Zhu) and contributors (see CONTRIBUTORS.txt)
#
# This module is part of lshash and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php
import json
try:
    import redis
except ImportError:
    redis = None

__all__ = ['storage']


def storage(storage_config, index):
    if 'dict' in storage_config:
        return InMemoryStorage(storage_config['dict'])


class BaseStorage(object):
    def __init__(self, config):
        raise NotImplementedError

    def append_val(self, key, val):
        raise NotImplementedError



class InMemoryStorage(BaseStorage):
    def __init__(self, config):
        self.name = 'dict'
        self.storage = dict()



    def append_val(self, key, val):
        self.storage.setdefault(key, []).append(val)


