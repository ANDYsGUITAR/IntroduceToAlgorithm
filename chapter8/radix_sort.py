def radix_sort(list, d=3): # 默认三位数，如果是四位数，则d=4，以此类推
    for i in range(d):  # d轮排序
        s = [[] for k in range(10)]  # 因每一位数字都是0~9，建10个桶
        for j in list:
            s[int(j / (10 ** i)) % 10].append(j)
        re = [a for b in s for a in b]
    return re

A = [5, 2, 4, 6, 1, 3, 0, 2]
A = radix_sort(A, 1)
print(A)