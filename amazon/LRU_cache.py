# description: https://leetcode.com/problems/lru-cache

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.used_queue = {} # preserves order insertion
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.used_queue.pop(key, None)
            self.used_queue[key] = key
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.used_queue:
            self.used_queue.pop(key, None)
            self.used_queue[key] = key
            self.cache[key] = value
        elif len(self.cache) == self.capacity:
            evict = next(iter(self.used_queue)) # improves performance, using iterators
            self.used_queue.pop(evict, None)
            self.cache.pop(evict, None)

            self.used_queue[key] = key
            self.cache[key] = value
        else:
            self.used_queue[key] = key
            self.cache[key] = value


# Time complexity: O(n), where n is the number of operations (n*O(1))
# Space complexity: O(k), where k is the number of keys stored in cache