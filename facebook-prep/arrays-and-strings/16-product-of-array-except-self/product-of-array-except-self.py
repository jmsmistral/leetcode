import sys

def productExceptSelf(arr):
    # calculate left array
    left = [0] * len(arr)
    left[0] = 1
    for i in range(1, len(arr)):
        left[i] = arr[i - 1] * left[i - 1]

    # calculate right array
    right = [0] * len(arr)
    right[-1] = 1
    for i in range(len(arr) - 2, -1, -1):
        right[i] = arr[i + 1] * right[i + 1]

    # calculate output as left[i] * right[i]
    output = [0] * len(arr)
    for i in range(len(arr)):
        output[i] = left[i] * right[i]
    return output


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    productExceptSelf(arr)

    # Example
    # arr   = [1, 2, 3, 4]
    # left  = [1, 1, 2, 6]
    # right = [24, 12, 4, 1]
    # out   = [24, 12, 8, 6]
