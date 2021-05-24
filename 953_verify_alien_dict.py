class Solution:
    def isAlienSorted(self, words, order):
        dict = {}
        for i in range(len(order)):
            dict[order[i]] = i

        def isFirstLessThanSecond(d, w1, w2):
            p1 = 0
            p2 = 0

            while p1 < len(w1) and p2 < len(w2):
                if d[w1[p1]] < d[w2[p2]]:
                    return True
                elif d[w1[p1]] > d[w2[p2]]:
                    return False
                else:
                    p1 += 1
                    p2 += 1

            if len(w1) > len(w2):
                return False

            return True

        for i in range(len(words)-1):
            if isFirstLessThanSecond(dict, words[i], words[i+1]) == False:
                return False
        return True




if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
    print(s.isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz"))
