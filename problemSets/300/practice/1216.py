class Solution:
    def isValidPalindrome(self, s, k):
        mem = {}
        # count = self.helper(s, 0, len(s)-1, mem)
        count = self.helper(s, 0, len(s), mem)
        return count <= k

    def helper(self, str, l, r, cache):
        if l == r or l+1 == r:
            return 0

        if (l,r) in cache:
            return cache[(l,r)]

        # if str[l] == str[r]:
        if str[l] == str[r-1]:
            cache[(l,r)] = self.helper(str, l+1, r-1, cache)
        else:
            cache[(l,r)] = min(self.helper(str, l+1, r, cache), self.helper(str, l, r-1, cache)) + 1

        return cache[(l,r)]

print(Solution().isValidPalindrome("bacabaaa", 2))
print(Solution().isValidPalindrome("abefzba", 1))
print(Solution().isValidPalindrome("abcdca", 2))
print(Solution().isValidPalindrome("abbababa", 1))

'''
01234567
bacabaaa
 ^   ^

cache = [

(0,4) = +
(1,5) =
]

helper(0,7)
    cache[0,7] = min(
        helper(0,6), +
        helper(1,7),
    )+1

helper(0,6)
    cache[0,6] = min(
        helper(0,5), +
        helper(1,6),
    )+1

helper(0,5)
    cache[0,5] = min(
        helper(0,4), +
        helper(1,5)
    )+1



'''
