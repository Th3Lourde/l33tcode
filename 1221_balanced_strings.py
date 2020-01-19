class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        balance = 0

        for i in range(len(s)):
            if s[i] == "R":
                balance += 1
            elif s[i] == "L":
                balance -= 1

            if balance == 0:
                ans += 1

        return ans


if __name__ == '__main__':
    # s = "RLRRLLRLRL"
    # s = "RLLLLRRRLR"
    s = "LLLLRRRR"

    S = Solution()



    r = S.balancedStringSplit(s)
    print(r)
