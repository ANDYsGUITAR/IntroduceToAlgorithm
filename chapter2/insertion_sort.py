
def insertion_sort(nums):
    for j in range(1, len(nums)):
        val = nums[j]
        i = j - 1
        while i >= 0 and nums[i] > val:
            nums[i + 1] = nums[i]
            i -= 1
        nums[i + 1] = val

    return nums


def insertion_sort_DESC(nums):
    for j in range(1, len(nums)):
        val = nums[j]
        i = j - 1
        while i >= 0 and nums[i] < val:
            nums[i + 1] = nums[i]
            i -= 1
        nums[i + 1] = val

    return nums


A = [5, 2, 4, 6, 1, 3]
A = insertion_sort(A)
print(A)
A = insertion_sort_DESC(A)
print(A)