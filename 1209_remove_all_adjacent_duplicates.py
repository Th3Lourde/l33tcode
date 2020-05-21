

class Solution:
    def removeDuplicates(self, s, k):
        start = 0
        run = 0
        Continue = True

        while Continue:
            char = ""
            Continue = False
            hits = {}

            for i in range(len(s)):
                if char == "":
                    char = s[i]
                    run = 1
                    start = i

                elif s[i] != char:
                    char = s[i]
                    run = 1
                    start = i

                elif s[i] == char:
                    run += 1

                    if run == k:
                        hits[start] = True
                        char = ""
                        Continue = True

            tmp = ""
            i = 0

            while i < len(s) and Continue:
                try:
                    if hits[i]:
                        i += k

                except:
                    tmp += s[i]
                    i += 1

            if i == len(s):
                s = tmp

        return s






if __name__ == '__main__':
    s = Solution()

    testCases = [
        ["abcd", 2, "abcd"],
        ["", 2, ""],
        ["daabbccd", 2, ""],
        ["daaabbbcccd", 2, "dabcd"],
        ["aaabbbccc", 2, "abc"],
        ["daaadbbbdcccd", 3, "d"],
        ["deeedbbcccbdaa", 3, "aa"],
        ["pbbcggttciiippooaais", 2, "ps"],
    ]

    for tc in testCases:
        r = s.removeDuplicates(tc[0], tc[1])
        assert r == tc[2], "[For {}, {}] {} != {}".format(tc[0], tc[1], r, tc[2])

    print("[passed all test cases]")
