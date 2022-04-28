class Solution:
    def wordPattern(self, pattern, s):
        # Check that all keys are unique
        words = s.split(" ")
        wordToPattern = {}

        if len(pattern) != len(words):
            return False

        for idx in range(len(pattern)):
            if pattern[idx] in wordToPattern and wordToPattern[pattern[idx]] != words[idx]:
                return False
            else:
                wordToPattern[pattern[idx]] = words[idx]

        value_set = set()

        for value in list(wordToPattern.values()):
            if value in value_set:
                return False

            value_set.add(value )

        return True

print(Solution().wordPattern( "aaa", "aa aa aa aa"))

print(Solution().wordPattern("abba","dog dog dog dog" ))
print(Solution().wordPattern("abba","dog cat cat dog" ))
print(Solution().wordPattern("aaaa","dog cat cat dog" ))
print(Solution().wordPattern("abba","dog cat cat dog" ))
print(Solution().wordPattern("abba","dog cat cat fish" ))
print(Solution().wordPattern("abba","dog cat ct fish" ))
