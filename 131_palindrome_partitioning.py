'''
Given a string s, partition s ∋ every substring of
the partition is a palindrome

Return all possible palindrome partitioning of s.

Start on the lhs of the string.
Keep track of the current substring that you are on.
If the substring is a palindrome. You make the decision
to either partition at that value, or to not to.

(idx, sub, parition)

Also have a helper function to tell us whether or not
something is or is not a palindrome. Can't think of a
good way to do this other than to go through all of the
elements every time.

"aab"

(0, "", [])
not a palindrome
itr(1, "a", [])

isPalindrome():
    itr(2, "", ["a"])
        itr(3, "b", ["a"])

        itr(3, "", ["a", "b"])

itr(2, "a"+"a", [])

'''

class Solution:
    def partition(self, s):

        def isPalindrome(str):

            if len(str) == 0:
                return False

            elif len(str) == 1:
                return True

            i = 0
            j = len(str)-1

            while i < j:
                if str[i] == str[j]:
                    i += 1
                    j -= 1
                else:
                    return False

            return True

        ans = []

        if len(s) == 0:
            return ans

        def itr(idx, sub, partition):
            if idx >= len(s):
                if isPalindrome(sub):
                    ans.append(list(partition+[sub]))
                elif sub == "":
                    ans.append(list(partition))
                return

            if isPalindrome(sub):
                itr(idx+1, s[idx], list(partition+[sub]))

            itr(idx+1, sub+s[idx], list(partition))

        itr(1, s[0], [])

        return ans



if __name__ == '__main__':
    s = Solution()

    print(s.partition("aba"))
