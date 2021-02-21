'''
Given a string s, partition s s.t.
every subtstring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

The obvious solution is to have a list containing
only single elements:

"aab" → ["a", "a", "b"]

"aaa" → ["a", "a", "a"]

So let's start there.

However how do we build up?

If every element (- last one), looks right and asks the
question: Is this a palindrome? We would be able to build
up.

Hmmm maybe another function call after this initial split?
Else we'd mess-up on edge case.

So how about this:
    - have a length of a palindrome that we are looking for
    go l → r, if we find a pali, function call (recursion).
    - do a function call to simulate what would happen if we
    were to use that pali, however keep going.

    after we find all palis of lenght 2, look for length 3,
    4, ..., len(input)-1.

If we start at all single-element palindromes and build up,
we'll run into a scenario where we will double-count, which
will result in us needing to use a set.

If we instead create a palindrome bridge from l → r, we won't
double count.

Maybe we can create a data structure that answer the question of
is s[i:j] a palindrome?

Given an index in the string to look at, our current partition of
the string, search for valid palis to complete our path.


'''
    # 12.14.20
class Solution:
    def partition(self, s):
        ans = []
        self.itr(s, ans, 0, [])
        return ans

        # p is our current partition
    def itr(self, s, ans, idx, p):
        if idx >= len(s):
            ans.append(p)
            return

        for k in range(idx, len(s)):
            subList = s[idx: k+1]
            if subList[::] == subList[::-1]:
                # Have valid pali
                self.itr(s, ans, k+1, p+[subList])








class Solution1:
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

    print(s.partition("a"))
