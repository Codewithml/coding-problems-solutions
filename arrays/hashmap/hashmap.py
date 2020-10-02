class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hashFunction(self, key):
        return key % self.size

    def set(self, key, value):
        hashIndex = self.hashFunction(key)
        for item in self.table[hashIndex]:
            if item.key == key:
                item.value = value
                return
        self.table[hashIndex].append(Item(key, value))

    def get(self, key):
        hashIndex = self.hashFunction(key)
        for item in self.table[hashIndex]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        hashIndex = self.hashFunction(key)
        for index, item in enumerate(self.table[hashIndex]):
            if item.key == key:
                del self.table[hashIndex][index]
                return
        raise KeyError('Key not found')
