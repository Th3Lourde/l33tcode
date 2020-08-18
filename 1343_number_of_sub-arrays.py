'''

Given an array of integers, and two integers
k, threshold:

Return the number of sub-arrays of size k
with an average ≥ threshold

I believe subarray means a group of elements
that are adjacent to each other.

So create a sliding box of size k, add/subtract
from ave as we slide the box.

1) Generate the sliding box so to speak
2) As we iterate through elements, add/sub

Ok, so this is technically correct. However
we get a TLE. I wonder what we could do in
order to make the code faster.

We could use the python library that we
know is quick.

Ok so this worked with the deque algo.

I wonder what another way to do it might be.

So the other way was actually something that I
had thought of, using a variable that keeps track
of the left element instead of keeping a list
of all of the different values.

'''

from collections import deque

class Solution:


    def numOfSubarrays(self, arr, k, t):
        ans = 0

        # sub = []
        sub = deque()
        ave = 0

        for i in range(k):
            # sub.append(arr[i])
            sub.append(arr[i])
            ave += arr[i]/k

        if ave >= t:
            ans += 1

        for i in range(k, len(arr)):
            ave -= sub[0]/k
            sub.popleft()
            sub.append(arr[i])
            # sub = sub[1:] + [arr[i]]
            ave += arr[i]/k

            if ave >= t:
                ans += 1

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))

    print(s.numOfSubarrays([1,1,1,1,1], 1, 0))

    print(s.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))

    print(s.numOfSubarrays([7,7,7,7,7,7,7], 7, 7))

    print(s.numOfSubarrays([4,4,4,4], 4, 1))
