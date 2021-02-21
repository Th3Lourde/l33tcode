class Solution:
    def arrayStringsAreEqual(self, word1, word2):

        stringOne = ""
        stringTwo = ""

        for subStr in word1:
            stringOne += subStr

        for subStr in word2:
            stringTwo += subStr

        return stringOne == stringTwo


if __name__ == '__main__':
    s = Solution()

    print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
    print(s.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
    print(s.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
