def left(i):
    return i * 2


def right(i):
    return i * 2 + 1


def parent(i):
    return i // 2


def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l <= heap_size - 1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size - 1 and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


def build_max_heap(A):
    heap_size = len(A)
    for i in range(len(A) // 2, -1, -1):
        print(i)
        max_heapify(A, i, heap_size)

def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)
    return A

A = [5, 2, 4, 6, 1, 3]
A = heap_sort(A)
print(A)