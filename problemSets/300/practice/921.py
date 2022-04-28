'''
Just count the number of times a paren isn't valid.
'''

class Solution:
    def minAddToMakeValid(self, s):
        stack = []
        adds = 0

        for chr in s:
            if chr == "(":
                stack.append("(")
            elif chr == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    adds += 1

        adds += len(stack)

        return adds

print(Solution().minAddToMakeValid("((("))
