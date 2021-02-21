# still don't understand masks: https://leetcode.com/problems/sum-of-two-integers/discuss/377906/easy-peasy-python(comments-works-for-negative)-solution-using-bit
class Solution:
    # Fails for negative numbers,
    # doesn't really use bit manipulation
    def getSumF(self, a, b):

        ans = []
        carry = 0

        # Works if both pos
        while a > 0 or b > 0:
            tA = a & 1
            tB = b & 1

            if tA == 1 and tB == 1:
                if carry == 1:
                    ans.insert(0, "1")
                else:
                    ans.insert(0, "0")
                    carry = 1

            elif tA == 1 or tB == 1:
                if carry == 1:
                    ans.insert(0, "0")
                    carry = 1
                else:
                    ans.insert(0, "1")

            else:
                if carry == 1:
                    ans.insert(0, "1")
                    carry = 0
                else:
                    ans.insert(0, "0")

            a >>= 1
            b >>= 1

            if a < 0:
                a = 0

            if b < 0:
                b = 0

        if carry == 1:
            ans.insert(0, "1")

        s = "".join(ans)

        return int(s, 2)

    def getSum(self, a, b):
        c = 0
        mask = 0xffffffff

        if a == 0:
            return b

        if b == 0:
            return a

        while b & mask != 0:
            c = (a&b) << 1
            a = a ^ b
            b = c

        return a&mask if b > mask else a


if __name__ == '__main__':
    s = Solution()

    print(s.getSum(-2, 3))
