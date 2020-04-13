

class Solution:
    def wordBreak(self, s, wordDict):

        # d = {}
        #
        # for word in wordDict:
        #     d[word] = True
        #
        # wordDict = d

        l = 0
        r = len(s)

        while l != r:
            try:
                if wordDict[s[l:r]]:
                    if r != len(s):
                        l = r
                        r = len(s)

                    elif r == len(s):
                        return True

            except:
                r -= 1

        print(s[l:])

        while l >= 0:
            try:
                ...

            except:
                l -= 1

        return False


if __name__ == '__main__':
    s = Solution()

    testCases = [
        # ["a", {"a":True}, True],
        # ["ab", {"a":True, "b":True}, True],
        # ["applesz", {"apples":True}, False],
        # ["leetcode", {"leet": True, "code":True}, True],
        # ["catsandog", {"cats": True, "dog": True, "sand": True, "and": True, "cat": True}, False],
        # ["applepenapple", {"apple": True, "pen": True}, True],

        ["abcd", {"a": True, "abc": True, "b": True, "cd": True}, True],

    ]

    passed = True
    z = 1

    for testCase in testCases:
        resp = s.wordBreak(testCase[0], testCase[1])

        if resp != testCase[2]:
            passed = False
            print("[failed test case {}] wanted {} got {}".format(z, testCase[2], resp))
            break

        z += 1

    if passed:
        print("[passed all test cases] :)")
