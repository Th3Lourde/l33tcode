def kadane(arr):
    if len(arr) == 0:
        return 0

    size = len(arr)
    currMax = max(arr)
    endMax = 0

    for i in range(size):
        endMax = endMax + arr[i]

        if endMax < 0:
            endMax = 0

        elif (currMax < endMax):
            currMax = endMax

    return currMax

print(kadane([-2, -3, -1, -1, -2, -5, -3]))
