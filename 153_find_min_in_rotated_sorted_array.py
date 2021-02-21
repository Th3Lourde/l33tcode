'''
Array of length n is sorted in ascending order.
Array is rotated between 1 and n times.
Find the min.

Brute force solution: Single pass 0(n), find min.
There's probably a solution that is related to
binary search, so we might as well shoot for it.

So we are given that the array is sorted.

[1,2,3,4,5] → [3,4,5,1,2]
               ^   ^   ^

We can write a modified binary search algorithm,
then search for float('-inf').

As we search, keep track of the elements that we
see, keep updating a tmp var so we only save the
min value.
'''
# Does it work if the edge cases are the values

class Solution:
    def findMin(self, arr):
        ans = arr[0]

        if arr[-1] < arr[0]:
            ans = arr[-1]


        l = 0
        r = len(arr)-1

        while l < r:
            m = (l+r)//2

            if arr[m] < ans:
                ans = arr[m]

            if arr[l] < arr[r]:
                # If we are in a sorted subarray
                # return the min value
                return arr[l]

            if arr[l] < arr[m]:
                # l --> m is sorted, check
                # min element then move right
                if arr[l] < ans:
                    ans = arr[l]

                l = m+1
            else:
                # l --> r is sorted, we have
                # the min element
                r = m

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3,4,5,1,2]))
    print(s.findMin([5,1,2,3,4]))
    print(s.findMin([1,2,3,4,5]))
    print(s.findMin([4,5,1,2,3]))
    print(s.findMin([1,2,3,4,5]))
    print(s.findMin([4,5,6,7,0,1,2]))
    print(s.findMin([13,15,17,11]))
