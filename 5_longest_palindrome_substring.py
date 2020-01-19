

class Solution:

    def is_palindrome(self, x:str) -> bool:
        if len(x)%2 == 0:
            for i in range(int(len(x)/2)):
                if x[i] != x[len(x)-i-1]:
                    return False
            return True

        elif len(x)%2 != 0:
            for i in range(int((len(x)-1)/2)):
                if x[i] != x[len(x)-i-1]:
                    return False
            return True


    def longestPalindrome(self, s:str) -> str:

        if s == '':
            return ''

        start = 0
        end = len(s)

        while end > 1:
            s_tmp = start
            e_tmp = end
            while (e_tmp) <= len(s):
                r = self.is_palindrome(s[s_tmp:e_tmp])
                if r:
                    return s[s_tmp:e_tmp]
                s_tmp += 1
                e_tmp += 1

            end -= 1

        return s[0]


if __name__ == '__main__':
    s = Solution()

    # my_str = "babad"

    my_str = "cbbd"

    print(s.longestPalindrome(my_str))

    # print(s.is_palindrome("cb"))
