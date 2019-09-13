def counting_sort(A, k):
    C = [0] * (k + 1)
    B = [0] * len(A)
    for i in range(len(A)):
        C[A[i]] += 1
    # now C[i] contains the number of elements equal to i
    print(C)
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    # now C[i] contains the number of elements less than or equal to i
    print(C)
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B

A = [5, 2, 4, 6, 1, 3, 0, 2]
B = counting_sort(A, 6)
print(B)