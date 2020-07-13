'''
Given a string, reverse the order of characters
in each word, while still preserving white space
and initial word order.

If space, add space.

Start at end of string, build new string, adding to the
LHS.

"abc contest"
tsetnoc  <-- add to lhs
bca <-- add to lhs

"bca tsetnoc"

going through the words in reverse order:

werd = ""
if c != " "
    werd = word + c

if c == "":
    ans = " " + werd
    werd = ""

So we got the optimal solution, joy.

'''

class Solution:
    def reverseWords(self, s):
        ans = ""
        werd = ""

        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                werd = werd + s[i]

            elif s[i] == " ":
                ans = " " + werd + ans
                werd = ""

        ans = werd + ans

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
