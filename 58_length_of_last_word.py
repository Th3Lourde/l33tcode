'''
Or can we do one better.
What if we start on the rhs?

move left until you find a character (not a space)
count until you run out of room or hit a space.

return
'''

class Solution:
    def lengthOfLastWord(self, s):
        ptr = len(s)-1

        # find right most character
        while s[ptr] == " ":
            ptr -= 1

        # found right most character, count
        # how long the word is
        wordLength = 0

        while ptr >= 0 and s[ptr] != " ":
            wordLength += 1
            ptr -= 1

        return wordLength

print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord("foo "))
