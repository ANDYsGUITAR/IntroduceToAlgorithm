def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def parent(i):
    return i // 2


class PriorityQueue(object):
    def __init__(self, A):
        self.heap_size = len(A)
        self.data = A

    def heap_maximum(self):
        return self.data[0]

    def max_heapify(self, i):
        l = left(i)
        r = right(i)
        if l <= self.heap_size - 1 and self.data[l] > self.data[i]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size - 1 and self.data[r] > self.data[largest]:
            largest = r
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(self.heap_size // 2, -1, -1):
            self.max_heapify(i)

    def heap_extract_max(self):
        if self.heap_size < 1:
            print("heap underflow")
            return None
        maximum = self.data[0]
        self.data[0] = self.data[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return maximum

    def heap_increase_key(self, i, key):
        if key < self.data[i]:
            print("new key is smaller than current value")
            return None
        self.data[i] = key
        while i > 0 and self.data[parent(i)] < self.data[i]:
            self.data[i], self.data[parent(i)] = self.data[parent(i)], self.data[i]
            i = parent(i)

    def heap_sort(self):
        self.build_max_heap()
        length = len(self.data)
        for i in range(length - 1, 0, -1):
            self.data[0], self.data[i] = self.data[i], self.data[0]
            self.heap_size -= 1
            self.max_heapify(0)
        return self.data

    def max_heap_insert(self, key):
        self.heap_size += 1
        self.data.append(float("-inf"))
        self.heap_increase_key(self.heap_size - 1, key)


A = [5, 2, 4, 6, 1, 3]
test = PriorityQueue(A)
test.build_max_heap()
print(test.data)
print(test.heap_extract_max())
print(test.heap_extract_max())
print(test.heap_extract_max())
test.max_heap_insert(7)
print(test.heap_extract_max())


