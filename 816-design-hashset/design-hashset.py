class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key):
        if key not in self.arr:
            self.arr.append(key)

    def remove(self, key):
        if key in self.arr:
            self.arr.remove(key)

    def contains(self, key):
        return key in self.arr