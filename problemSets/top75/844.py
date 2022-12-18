'''
Given two strings, every hash symbol represents
a backspace character.

Apply the backspace character to each string, return if they are equal
This seems like a stack
'''

from collections import deque

class Solution:
    def backspaceCompare(self, s, t):
        stack1 = deque()
        stack2 = deque()

        for chr in s:
            if chr == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(chr)

        for chr in t:
            if chr == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(chr)

        return stack1 == stack2
