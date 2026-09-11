# solution 1 (python)
# problem ref: https://neetcode.io/problems/design-hashmap/question?list=neetcode250

# Example:
#
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1); // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3); // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2); // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2); // return -1 (i.e., not found), The map is now [[1,1]]

# NOTE: cannot use python build in `dict()`


class KVPair:
    def __init__(self, key: int, value: int):
        # NOTE: using tuple also works, but this is the easiest
        self.key = key
        self.value = value

    def __eq__(self, key: int):
        return key == self.key  # enables int `==` class


class MyHashMap:
    def __init__(self):
        self.capacity = 10
        self.buckets = [[] for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        # simple hash
        hash = key % self.capacity
        bucket = self.buckets[hash]

        # replacement if key is the same
        for kv in bucket:
            if key == kv:
                kv.value = value
                return

        bucket.append(KVPair(key, value))

    def get(self, key: int) -> int:
        # simple hash
        hash = key % self.capacity
        bucket = self.buckets[hash]

        for kv in bucket:
            if key == kv:
                return kv.value  # found

        return -1  # not found

    def remove(self, key: int) -> None:
        # simple hash
        hash = key % self.capacity
        bucket = self.buckets[hash]

        for i, kv in enumerate(bucket):
            if key == kv:
                del bucket[i]
                return


if __name__ == "__main__":
    hashmap = MyHashMap()

    hashmap.put(1, 1)  # [[1,1]]
    hashmap.put(2, 2)  # [[1,1], [2,2]]

    a = hashmap.get(1)  # return 1
    b = hashmap.get(3)  # return -1

    hashmap.put(2, 1)  # [[1,1], [2,1]]
    c = hashmap.get(2)  # return 1

    hashmap.remove(2)  # [[1,1]]
    d = hashmap.get(2)  # return -1

    print(a, b, c, d)

# time complexity: O(N)
