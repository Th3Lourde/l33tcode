
'''
Given string, return # palindromic substrings
exist within the string.

have a function that returns whether or not
a string is a palindrome.

Every time you find a valid palindrome,
store it in a dict.

If it is not a valid palindrome, also store.

So you can just look-up instead of re-use the palindrome
algo.

Assume we have palindrome algo implemented
'''




class Solution:
    def countSubstrings(self, s):

        def isPalindrome(word):

            if len(word) == 1:
                return True

            i = 0
            while i < len(word)//2:
                if word[i] != word[i*(-1)-1]:
                    return False
                i += 1

            return True

        palis = {}
        ans = 0

        for i in range(len(s), -1, -1):
            possiblePaliL = i

            for j in range(len(s)-possiblePaliL):
                possiblePali = s[j:j+i+1]
                print(possiblePali)

                try:
                    if palis[possiblePali]:
                        ans += 1

                except:
                    if isPalindrome(possiblePali):
                        palis[possiblePali] = True
                        ans += 1

                    else:
                        palis[possiblePali] = False

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.countSubstrings("abc"))
