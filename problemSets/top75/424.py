'''
You are given a string s

You are given an integer k

You can choose any character and replace it with any
other character. You can do this k times.

Your goal is to create the longest substring possible,
where said substring is composed of the same characters.

What is the longest substring that you can create?

So two pointers and two vars.

var one represents the characters in the substring
var two represents the chr that the substr is made up of

swaps = k

AABABBA
  ^
    ^

AABABBA
'''

class Solution:
    def characterReplacement(self, s, k):
        ...
