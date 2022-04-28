'''
Given an integer array that is sorted in increasing order and integer k
find the kth positive integer that isn't in the array

Consider the set of positive integers

[0,1,2,3,....,+inf]

The difference between this set and the given array contains the
elements not in the arr that are missing. Find the k-th element
in this set.

Method 1: keep a counter, this counter repre

arr = [2,3,4,7,11]
               ^
k = 0
counter = 9
'''

class Solution:
    def findKthPositive(self, arr, k):
        counter = 1
        arrPtr = 0

        while arrPtr < len(arr):
            if counter == arr[arrPtr]:
                arrPtr += 1
            else:
                k -= 1

            if k == 0:
                return counter

            counter += 1

        for _ in range(k-1):
            counter += 1

        return counter

print(Solution().findKthPositive([2,3,4,7,11], 10))
