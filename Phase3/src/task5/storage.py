import json
def storage(storage_config, index):
    if 'dict' in storage_config:
        return InMemoryStorage(storage_config['dict'])
class InMemoryStorage():
    def __init__(self, config):
        self.name = 'dict'
        self.storage = dict()
    def append_val(self, key, val):
        self.storage.setdefault(key, []).append(val)


