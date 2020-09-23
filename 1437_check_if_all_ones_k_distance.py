'''
Given an array nums of 0s and 1s and an
integer k, retrun True if all 1's are at
least K places away from each other, else
return false.

Each element is either a zero or a one.

Pass through the array, record the distance
between k-values, if the distance is ever
< k, return false. At end of loop, return true.

[0,0,0,0,1,0,0,0,1,0,0,1]
                       ^

 last1 = 2

 num = 0


'''

class Solution:
    def kLengthApart(self, nums, k):
        last1 = -1

        for num in nums:

            # See 0, have seen 1
            if num == 0 and last1 != -1:
                last1 += 1


            elif num == 1 and last1 != -1:
                # Check against k, can return False
                if last1 < k:
                    return False

                last1 = 0

            elif num == 1 and last1 == -1:
                last1 = 0

        return True

if __name__ == '__main__':
    s = Solution()

    print(s.kLengthApart([1,0,0,0,1,0,0,1], 2))
    print(s.kLengthApart([1,0,0,0,1,0,1], 2))
    print(s.kLengthApart([1,1,1,1,1,1,1], 0))
    print(s.kLengthApart([1,0,1,0,1,0,1], 1))
    print(s.kLengthApart([1,1,1,0,1,0,1], 1))
