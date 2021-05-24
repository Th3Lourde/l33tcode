'''
Given an array that was sorted and then rotated,
find the minimum element.

Brute-Force: 0(n), find min

If l <= m:
    min Value from [l,m] is l
    l = m+1

If m <= r:
    min Value from [m,r] is m

if l <= m:
    l = m+1


min(2,3,3)
 0 1 2 3 4 5 6
[4,5,6,7,0,1,2]
 l           r

'''

class Solution:
    def findMin(self, arr):
        l = 0
        r = len(arr)-1
        minVal = min(arr[l], arr[r])

        while l < r:
            m = l + (r-l)//2

            minVal = min(minVal, arr[m])

            if arr[l] <= arr[m]:
                l = m+1
                minVal = min(minVal, arr[l])
            else:
                r = m

        return minVal

s = Solution()

print(s.findMin([3,4,5,1,2])) # 1
print(s.findMin([4,5,6,7,0,1,2])) # 0
print(s.findMin([11,13,15,17])) # 11
print(s.findMin([11,13,17])) # 11
print(s.findMin([11,13,7])) # 11
print(s.findMin([1])) # 1
print(s.findMin([1,0])) # 0
print(s.findMin([0,1])) # 0
