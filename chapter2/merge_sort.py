def merge(A, p, q, r):
    l_part = [x for x in A[p:q+1]]
    r_part = [x for x in A[q+1:r + 1]]
    l_part.append(float('inf'))
    r_part.append(float('inf'))
    i, j = 0, 0
    for k in range(p, r+1):
        if l_part[i] <= r_part[j]:
            A[k] = l_part[i]
            i += 1
        else:
            A[k] = r_part[j]
            j += 1
    return None


def merge_sort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A


A = [5, 2, 4, 6, 1, 3]
A = merge_sort(A, 0, len(A) - 1)
print(A)