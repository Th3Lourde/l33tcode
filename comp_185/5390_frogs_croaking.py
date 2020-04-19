
class Solution:


    def minNumberOfFrogs(self, croakOfFrogs):

        if croakOfFrogs == "":
            return -1

        ans = 1
        mapping = {"r":"c", "o":"r", "a":"o", "k":"a"}
        d = {"c":0, "r":0, "o":0, "a":0, "k":0}
        c = []
        filler = 0

        # for char in croakOfFrogs:
        for i in range(len(croakOfFrogs)):
            char = croakOfFrogs[i]
            d[char] += 1

            if char == "c":

                if i != 0 and filler <= 0:
                    c.append(i)

                if filler > 0:
                    filler -= 1

            elif char != "c":
                if d[char] > d[mapping[char]]:
                    return -1

                if char == "k":
                    filler += 1


        vals = list(d.values())

        tmp = vals[0]

        for val in vals:
            if tmp != val:
                return -1

        for hit in c:
            if croakOfFrogs[hit-1] != "k":
                ans += 1

        return ans


    def minNumberOfFrogs1(self, croakOfFrogs):
        d = {"c":0, "r":0, "o":0, "a":0, "k":0}

        for char in croakOfFrogs:
            d[char] += 1




        vals = list(d.values())

        tmp = vals

        for val in vals:
            if tmp != val:
                return -1


        # if len(croakOfFrogs) != tmp*5:
        #     return -1

        return tmp




if __name__ == '__main__':
    s = Solution()

    # print(s.minNumberOfFrogs("crcoakroak"))
    # print(s.minNumberOfFrogs("aoocrrackk"))
    print(s.minNumberOfFrogs("cccrorakrcoakorakoak"))
