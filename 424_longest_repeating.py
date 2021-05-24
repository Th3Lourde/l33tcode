class Solution:
    def characterReplacement(self, s, k):
        maxFreq = 0
        maxRun = 0
        freq = {}
        l = 0

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1

            maxFreq = max(maxFreq, freq[s[r]])

            if r-l+1 <= maxFreq+k:
                maxRun = max(maxRun, r-l+1)

            while r-l+1 > maxRun:
                freq[s[l]] -= 1

                if freq[s[l]] == 0:
                    del freq[s[l]]

                l += 1

        return maxRun


print(Solution().characterReplacement("ABAB", 2)) # 4
print(Solution().characterReplacement("AABABBA", 1)) # 4
print(Solution().characterReplacement("AB", 2)) # 2
print(Solution().characterReplacement("ABBB", 2)) # 4
print(Solution().characterReplacement("BAAAB", 2)) # 5
print(Solution().characterReplacement("ABAA", 0))
