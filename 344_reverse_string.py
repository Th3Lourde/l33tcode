'''
Given a List[str], reverse the strings

Have left, right, while l < r: swap

Ok fo that wasn't very fast. How could
we do it better?

Not sure. Just reverse the list?


'''

class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s)-1

        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp

            l += 1
            r -= 1

        return s

if __name__ == '__main__':
    s = Solution()
    # print(s.reverseString(["h","e","l","l","o"]))

    print(s.reverseString(["H","a","n","n","a","h"]))
