

class Solution:
    def findAnagrams(self, s, p): # Works but we got time limit exceeded.

        def confirmAnagram(subStr):

            print(subStr)
            d = {}

            for e in subStr:
                try:
                    d[e] += 1

                except:
                    d[e] = 1

            keys = list(d.keys())

            for k in keys:
                try:
                    if d[k] != goal[k]: return False

                except:
                    return False

            return True

        if len(p) > len(s) or len(p) == 0:
            return []

        targ = 0

        goal = {}

        for char in p:
            targ += ord(char)

            try:
                goal[char] += 1

            except:
                goal[char] = 1

        q = []
        ans = []
        ordSum = 0
        subStr = ''

        for i in range(len(s)):
            print(subStr)
            if len(q) < len(p):
                q.insert(0, [s[i], i])
                ordSum += ord(s[i])
                subStr = s[i] + subStr

            elif len(q) == len(p):
                term = q.pop()

                if ordSum == targ:
                    if confirmAnagram(subStr): # create subStr, goal.
                        ans.append(term[1])

                ordSum -= ord(term[0])

                q.insert(0, [s[i], i])

                ordSum += ord(s[i])

                subStr = s[i] + subStr[:-1]

        if ordSum == targ:
            if confirmAnagram(subStr): # create subStr, goal.
                ans.append(q.pop()[1])

        return ans

if __name__ == '__main__':

    testCases = [
        ["", "abc", []],
        ["a", "abc", []],
        ["ab", "abc", []],
        ["abz", "abc", []],

        ["abc", "abc", [0]],
        ["abcx", "abc", [0]],
        ["xabcx", "abc", [1]],
        ["xabca", "abc", [1,2]],
        ["cabca", "abc", [0,1,2]],
        ["cabycba", "abc", [0,4]],

    ]

    s = Solution()

    for tc in testCases:
        r = s.findAnagrams(tc[0], tc[1])

        assert r == tc[2], "{} != {}".format(r, tc[2])

    print("[passed all testcases] :)")
