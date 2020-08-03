'''
Given two strings, haystack, needle,

We are looking for a needle in a haystack.

Note we are not just checking to see if we can
form a needle in the haystack, we are literally

looking to see if the string needle is present
in haystack.

We are returning the first occurrence of needle.

Or the index that marks the beginning of needle
in the haystack.


Ok so needle has a length, are there any constraints
on the size of needle?

If we are given an empty needle, return 0

find length of needle, if length == 0, return 0


Else:
    i = 0 --> len(haystack)-

So we want to loop through all of the valid possible
indices that could represent the beginning of a needle.

len(haystack)-1-len(needle)-1 ← represents the last valid
index at which a needle could end at

                        # Ends before :^)
for i in range(0, len(haystack)-len(needle)-1):
    ...

hello | len | 4
ll    | len | 1

4 - 1 == 3, which represents the value we should top at

len(haystack)-1-len(needle)

"haystack", len(needle) = 2
       ^

However we want to include this index. So add one.

tc: linear
mc: constant


'''

class Solution():
    def strStr(self, haystack, needle):
        if needle == "":
            return 0

        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i: i+len(needle)] == needle:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()

    print(s.strStr("hello", "ll"))

    print(s.strStr("hello", ""))

    print(s.strStr("hello", "z"))

    print(s.strStr("hello", "lloz"))

    print(s.strStr("hello", "llo"))

    print(s.strStr("hello", "hell"))

    print(s.strStr("hello", "ell"))

    print(s.strStr("hello", "llo"))
