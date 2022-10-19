# description: https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.previous = self.right, self.left

    def top(self):
        return self.right.previous

    def bottom(self):
        return self.left.next

    def insert(self, node):
        old = self.right.previous
        old.next, node.previous = node, old
        node.next, self.right.previous = self.right, node

    def remove(self, node):
        previous = node.previous
        nxt = node.next
        previous.next, nxt.previous = nxt, previous


class LRUCache:
    def __init__(self, capacity: int):
        self.table = {}
        self.capacity = capacity
        self.lru = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key in self.table:
            value = self.table[key].value
            self.lru.remove(self.table[key])
            self.table[key] = Node(key, value)
            self.lru.insert(self.table[key])
            return self.table[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.lru.remove(self.table[key])
        self.table[key] = Node(key, value)
        self.lru.insert(self.table[key])

        if len(self.table) > self.capacity:
            least = self.lru.bottom().key
            self.lru.remove(self.lru.bottom())
            del self.table[least]


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
