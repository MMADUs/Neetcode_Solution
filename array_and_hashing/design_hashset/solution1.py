# solution 1 (python)
# problem ref: https://neetcode.io/problems/design-hashset/question?list=neetcode250

# Example:
#
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)

# NOTE: cannot use python build in `set()`


class MyHashSet:
    def __init__(self):
        self.capacity = 10  # just a number of buckets basically
        self.buckets = [[] for _ in range(self.capacity)]

    def add(self, key: int) -> None:
        # simple hash
        hash = key % self.capacity
        bucket = self.buckets[hash]

        if key not in bucket:
            self.buckets[hash].append(key)

    def remove(self, key: int) -> None:
        # simple hash
        hash = key % self.capacity

        self.buckets[hash].remove(key)

    def contains(self, key: int) -> bool:
        # simple hash
        hash = key % self.capacity
        bucket = self.buckets[hash]

        return True if key in bucket else False


# my solution used array in bucket, modern implementation can use various structure
# such as: linked-list or a balanced-tree for more efficient value lookup in the bucket

# hash function can also be implemented in various way, the common concern in hash function
# is the collision handling problem (where appended value arrives to the same bucket everytime)


if __name__ == "__main__":
    hashset = MyHashSet()

    hashset.add(1)  # set = [1]
    hashset.add(2)  # set = [1, 2]

    a = hashset.contains(1)  # return True
    b = hashset.contains(3)  # return False, (not found)

    hashset.add(2)  # set = [1, 2]
    hashset.contains(2)  # return True
    hashset.remove(2)  # set = [1]

    c = hashset.contains(2)  # return False, (already removed)

    print(a, b, c)

# time complexity: O(N)
