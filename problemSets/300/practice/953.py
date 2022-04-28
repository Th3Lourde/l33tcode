class Solution:
    def isAlienSorted(self, words, order):
        chrToVal = {}

        for idx in range(len(order)):
            chrToVal[order[idx]] = idx

        def compare(wordA, wordB):
            idxA = 0
            idxB = 0

            while idxA < len(wordA) and idxB < len(wordB):
                if wordA[idxA] == wordB[idxB]:
                    idxA += 1
                    idxB += 1
                elif chrToVal[wordA[idxA]] < chrToVal[wordB[idxB]]:
                    return True
                else:
                    # print("idxA {}|idxB {} | ({},{})".format(idxA, idxB, wordA[idxA], wordB[idxB]))
                    return False

            if idxA < len(wordA) and idxB >= len(wordB):
                return False

            return True

        for idx in range(len(words)-1):
            if not compare(words[idx], words[idx+1]):
                return False

        return True

print(Solution().isAlienSorted(["hell", "hell", "hello"],"hlabcdefgijkmnopqrstuvwxyz"))

print(Solution().isAlienSorted(["ubg","kwh"],"qcipyamwvdjtesbghlorufnkzx"))
