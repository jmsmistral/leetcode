import sys

# See here: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
def nextPermutation(arr):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(arr) in [0, 1]:
        return

    # find non-increasing suffix (if one exists - if not return sorted array)
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        arr.sort()
        return

    # find the smallest value in suffix that's larger than the pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1

    # swap successor with pivot
    arr[j], arr[i - 1] = arr[i - 1], arr[j]

    # reverse the suffix
    arr[i: ] = arr[len(arr) - 1: i - 1: -1]



if __name__ == '__main__':
    nums = [1, 2, 3]
    nextPermutation(nums)
    print(nums)

    nums = [3, 2, 1]
    nextPermutation(nums)
    print(nums)

    nums = [1, 1, 5]
    nextPermutation(nums)
    print(nums)
