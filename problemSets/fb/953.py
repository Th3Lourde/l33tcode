'''
Given two words, return if they are in lexigraphical order

Empty character is less than any other character


'''

class Solution:
    def isAlienSorted(self, words, order):
        wordToVal = {}

        for idx in range(len(order)):
            wordToVal[order[idx]] = idx

        def inOrder(w1, w2):
            n = len(w2)

            for idx in range(len(w1)):
                if idx >= n:
                    return False
                elif wordToVal[w2[idx]] < wordToVal[w1[idx]]:
                    return False
                elif wordToVal[w2[idx]] > wordToVal[w1[idx]]:
                    return True

            return True

        for idx in range(len(words)-1):
            if not inOrder(words[idx], words[idx+1]):
                return False

        return True

print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
