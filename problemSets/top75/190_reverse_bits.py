
'''
Given a number, return the number that is mapped
to the reverse representation of that number.

Get the binary

11111111111111111111111111111101

101010
^

ans = (ans << 1) + n&1

ans = 010101

We could just get the string representation and reverse it


'''

print(bin(4))

class Solution:
    def reverseBits(self, n):
        ans = 0

        # print(bin(ans))

        for _ in range(32):
            ans = (ans << 1) + (n&1)
            n >>= 1

            # print(bin(n))
            # print(bin(ans))

        return ans

print(Solution().reverseBits(11111111111111111111111111111101))
print(Solution().reverseBits(4))
