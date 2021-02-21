class Solution:
    def mergeAlternately(self, word1, word2):
        ans = ""

        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            if len(ans) % 2 == 0:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1

        ans += word1[i:]
        ans += word2[j:]

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.mergeAlternately("123", "45"))
