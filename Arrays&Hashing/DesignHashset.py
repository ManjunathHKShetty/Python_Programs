class MyHashSet:
    def __init__(self):
        self.data = []

    def add(self, key):
        if key not in self.data:
            self.data.append(key)

    def remove(self, key):
        if key in self.data:
            self.data.remove(key)

    def contains(self, key):
        return key in self.data

    def __str__(self):
        return f"MyHashSet({list(self.data)})"


my_set = MyHashSet()
my_set.add(6)
my_set.add(8)
my_set.add(7)
my_set.remove(8)

print(my_set)
print(my_set.contains(6))

