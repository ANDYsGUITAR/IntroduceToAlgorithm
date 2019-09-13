def bucket_sort(A):
    max_val = max(A)
    min_val = min(A)
    bucket = [0] * (max_val - min_val + 1)
    for i in range(len(A)):
        bucket[A[i] - min_val] += 1
    result = []
    for i in range(len(bucket)):
        if bucket[i] != 0:
            result += [i + min_val] * bucket[i]
    return result

A = [5, 2, 4, 6, 1, 3, 0, 2]
A = bucket_sort(A)
print(A)
