class MyHashMap:
    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key, value):
        self.map[key] = value

    def get(self,key):
        return self.map[key]

    def remove(self,key):
        self.map[key] = -1

X = MyHashMap()
print(X.put(5,7))
print(X.put(6,12))
print(X.remove(6))
print(X.get(5))
print(X.get(3))
