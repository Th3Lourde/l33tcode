

class Solution:
    def removeDuplicates(self, s): # LC uses S instead of s.
        k = 2
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
        ["abcd", "abcd"],
        ["", ""],
        ["daabbccd", ""],
        ["daaabbbcccd", "dabcd"],
        ["aaabbbccc", "abc"],
        ["pbbcggttciiippooaais", "ps"],
    ]

    for tc in testCases:
        r = s.removeDuplicates(tc[0])
        assert r == tc[1], "[For {}] {} != {}".format(tc[0], r, tc[1])

    print("[passed all test cases]")
