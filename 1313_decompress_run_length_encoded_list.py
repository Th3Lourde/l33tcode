'''
Given a list of numbers, length of list is
even.

nums[i] = freq
nums[i+1] = value

[1,2,3,4]
 ^ ^

One   two
Three fours

ans = []

for even itr:
    ans = ans + [i+1]*i

[2] = [2]
[4]*3 = [4,4,4]

[] + [2] = [2]

'''

class Solution:
    def decompressRLElist(self, nums):
        ans = []

        for i in range(0, len(nums), 2):
            ans += [nums[i+1]]*nums[i]

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.decompressRLElist([1,2,3,4]))

    print(s.decompressRLElist([4,1,2,3]))
