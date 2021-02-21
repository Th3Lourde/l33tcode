

class Solution:
    # Solution 1
    def reverseBits_1(self, n):
        # 1) Get binary representation of number
        binRepr = bin(n)
        # print("binRepr: " + str(binRepr))
        # 2) Filter out the base info and loop through
        # it in reverse

        ans = ""

        for i in range(len(binRepr)-1, 1, -1):
            ans += binRepr[i]

        for i in range(32-len(ans)):
            ans = ans + "0"

        return int(ans, 2)

    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans<<1) + (n&1)
            n >>= 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))
