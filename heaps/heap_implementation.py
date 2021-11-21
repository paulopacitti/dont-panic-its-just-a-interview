class MinHeap:
    def __init__(self, array = None):
        if array == None:
            self.array = []
        else:
            self.array = array
            self.heapify(0)

    def parent(self, pos):
        return pos//2
 
    def left(self, pos):
        return 2 * pos
 
    def right(self, pos):
        return (2 * pos) + 1

    def is_leaf(self, pos):
        if pos >= (len(self.array)//2) and pos <= len(self.array):
            return True
        return False
 
    def swap(self, pos_1, pos_2):
        self.array[pos_1], self.array[pos_2] = self.array[pos_2], self.array[pos_1]

    def heapify(self, pos):
        if not self.is_leaf(pos):
            if self.array[pos] > self.array[self.left(pos)] or self.array[pos] > self.array[self.right(pos)]:
                if self.array[self.left(pos)] < self.array[self.right(pos)]:
                    self.swap(pos, self.left(pos))
                    self.heapify(self.left(pos))
                else:
                    self.swap(pos, self.right(pos))
                    self.heapify(self.right(pos))

    def insert(self, element):
        self.array.append(element)
 
        current = len(self.array) - 1
        while self.array[current] < self.array[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        popped = self.array[0]
        self.array[0] = self.array[len(self.array)-1]
        self.heapify(0)
        return popped

     
print('The minHeap is ')
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(17)
min_heap.insert(10)
min_heap.insert(84)
min_heap.insert(19)
min_heap.insert(6)
min_heap.insert(22)
min_heap.insert(9)

print("The Min val is " + str(min_heap.remove()))