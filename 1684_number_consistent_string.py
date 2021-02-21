
class Solution:
    def countConsistentStrings(self, allowed, words):
        allowedSet = set(allowed)
        ans = 0

        for word in words:
            ans += 1

            for chr in word:
                if chr not in allowedSet:
                    ans -= 1
                    break

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
