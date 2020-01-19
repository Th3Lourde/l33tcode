
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        longest = 0
        tmp = 0
        i = 0

        while i < len(s):

            # print(d)

            try:
                if type(d[s[i]]) == int:
                    # print("hi")
                    i = d[s[i]] + 1
                    if tmp > longest:
                        longest = tmp

                    tmp = 0
                    d = {}

            except:
                d[s[i]] = i
                i += 1
                tmp += 1

        if tmp > longest:
            return tmp

        elif tmp <= longest:
            return longest


    # Don't think that this is going to work
    def lengthOfLongestSubstring1(self, s: str) -> int:
        d = {}
        longest = None
        tmp = 0

        for i in range(len(s)):
            try:
                if d[s[i]]:
                    if longest == None:
                        longest = tmp
                        d = {s[i]: True}
                        tmp = 1

                    elif longest != None:
                        d = {s[i]: True}
                        if tmp > longest:
                            longest = tmp
                        tmp = 1

            except:
                d[s[i]] = True
                tmp += 1

        if longest == None:
            return tmp
        elif longest != None:

            if tmp > longest:
                return tmp

            elif tmp <= longest:
                return longest


if __name__ == '__main__':
    s = Solution()

    print(s.lengthOfLongestSubstring("dvdf"))
