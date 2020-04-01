


class Solution:

    def decodeString(self, s):
        ans = [""]
        z = -1

        nums = {
            "1":True,
            "2":True,
            "3":True,
            "4":True,
            "5":True,
            "6":True,
            "7":True,
            "8":True,
            "9":True,
            "0":True
        }

        i = len(s)-1

        while i >= 0:
            t = s[i]

            if t != "[" and t != "]" and z == -1:
                ans.insert(0, t)

            elif t == "]":
                z += 1

                if z == 0:
                    subStr = [""]

                elif z > 0:
                    subStr.append("")

            elif t == "[":
                strS = subStr.pop()
                z -= 1
                i -= 1

                n = ""

                while True:
                    try:
                        nums[s[i]]
                        n = s[i] + n
                        i -= 1
                    except:
                        strS *= int(n)
                        i += 1
                        break

                if z >= 0:
                    subStr[z] = strS + subStr[z]

                elif z == -1:
                    ans.insert(0, strS)

            elif z >= 0:
                subStr[z] = t + subStr[z]


            i -= 1

        return "".join(ans)

    def decodeString1(self, s):
        ans = [""]
        z = 0

        nums = {
            "1":True,
            "2":True,
            "3":True,
            "4":True,
            "5":True,
            "6":True,
            "7":True,
            "8":True,
            "9":True,
            "0":True
        }

        i = len(s)-1

        while i >= 0:
            t = s[i]

            if t != "[" and t != "]" and z == 0:
                ans.insert(0, t)

            elif t == "]":
                z += 1
                subStr = ""

            elif t == "[":
                z -= 1
                i -= 1

                n = ""

                while True:
                    try:
                        nums[s[i]]
                        n = s[i] + n
                        i -= 1
                    except:
                        subStr *= int(n)
                        i += 1
                        break

                if z == 0:
                    ans.insert(0,subStr)
                    subStr = ""

            elif z >= 1:
                subStr = t + subStr

            i -= 1

        return "".join(ans)




if __name__ == '__main__':
    s = Solution()

    testCases = [
        ["3[a]2[bc]", "aaabcbc"],
        ["3[a2[c]]", "accaccacc"],
        ["2[abc]3[cd]ef", "abcabccdcdcdef"],
        ["100[leetcode]", "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"],
        ["", ""],
        ["3[a]2[b4[F]c]", "aaabFFFFcbFFFFc"]
    ]

    z = 0
    for test in testCases:
        resp = s.decodeString(test[0])

        if resp == test[1]:
            print("[passed {}]".format(z))

        elif resp != test[1]:
            print("[failed {}] wanted {} got [{}]".format(z, test[1], resp))

        z += 1
