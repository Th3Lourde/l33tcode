
class Solution:

    # This works, is brute-force solution
    def longestPalindrome(self, s):
        if s == "":
            return ""

        for i in range(len(s), 1, -1):
            for j in range(len(s)-i+1):
                potential = s[j:j+i]

                if potential == potential[::-1]:
                    return potential

        return s[0]

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("aa"))
