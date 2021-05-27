'''
Given a string s, return the longest palindromic substring in s.

0(n²) --> Two pointer, check if each pointer is a valid palindrome

What if I started at the middle and then worked up from there?

Cause if I find a palindrome of a certain length I know it will be
the biggest palindrome that I can find.

 01234
"babad"

chrToIdx = {
    "b" : [0,2]
    "a" : [1,3]
    "d" : [4]
}

Bottom-Up DP:

dp[start][end] == Palindrome

 01234
"babad"

-|0|1|2|3|4
0|T|T|T|T|T
1| | | | |
2| | | | |
3| | | | |
4| | | | |


'''

class Solution:
    def longestPalindrome(self, s):
        ...
