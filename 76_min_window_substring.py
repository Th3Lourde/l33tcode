'''



"ADOBECODEBANC" "ABC"

targDict = {"A": 1, "B":1, "C":1}
currentDict = {"A": [10], "B": [9], "C": [10]}

0,5
0,9
5,10
9,12


"ADOBECODEBANC"
             ^



'''




class Solution:
    def minWindow(self, str, t):
        ans = ""

        targDict = {}

        for chr in t:
            if chr in targDict:
                targDict[chr] += 1
            else:
                targDict[chr] = 1

        currentDict = {}

        for k in targDict.keys():
            currentDict[k] = []

        for i in range(len(str)):
            if str[i] in targDict:
                currentDict[str[i]].append(i)

                if len(currentDict[str[i]]) > targDict[str[i]]:
                    del currentDict[str[i]][0]

                haveAns = True
                minIdx = float("inf")
                maxIdx = float("-inf")
                for k in targDict.keys():
                    if len(currentDict[k]) != targDict[k]:
                        haveAns = False
                        break
                    else:
                        if currentDict[k][0] < minIdx:
                            minIdx = currentDict[k][0]

                        if currentDict[k][-1] > maxIdx:
                            maxIdx = currentDict[k][-1]

                if haveAns:
                    subStr = str[minIdx:maxIdx+1]

                    if ans == "" or len(subStr) < len(ans):
                        ans = subStr

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "a"))
