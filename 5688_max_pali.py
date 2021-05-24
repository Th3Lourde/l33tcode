import functools
class Solution:
    def longestPalindrome(self, w1, w2):
        ans = 0
        string = w1+w2

        @functools.cache
        def f(l, r):
            if l >= r: return int(l==r)
            if string[l] == string[r]: return 2 + f(l+1, r-1)

            return max(f(l+1, r), f(l, r-1))


        for chr in "abcdefghijklmnopqrstuvwxyz":
            i = w1.find(chr)
            j = w2.rfind(chr)

            if i != -1 and j != -1: ans = max(ans, f(i, j+len(w1)))

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("cacb", "cbba"))
    print(s.longestPalindrome("cfe", "ef"))


word = "cfeef"
@functools.cache
def f(lo, hi):
    if lo >= hi: return int(lo == hi)
    if word[lo] == word[hi]: return 2 + fn(lo+1, hi-1)
    return max(fn(lo+1, hi), fn(lo, hi-1))
