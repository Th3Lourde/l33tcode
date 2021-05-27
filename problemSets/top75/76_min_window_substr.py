from collections import deque
from collections import Counter

class Solution:
    def minWindow(self, s, t):
        chrToFreq = Counter(t)
        startIdx = 0
        endIdx = 0
        min_window = ""
        chrsLeft = len(t)

        for endIdx in range(len(s)):
            if chrToFreq[s[endIdx]] > 0:
                chrsLeft -= 1

            chrToFreq[s[endIdx]] -= 1

            while chrsLeft == 0:
                # Compare current string to smallest string
                length, validStr = endIdx-startIdx, s[startIdx:endIdx+1]

                if not min_window or length < len(min_window):
                    min_window = validStr

                chrToFreq[s[startIdx]] += 1

                if chrToFreq[s[startIdx]] > 0:
                    chrsLeft += 1

                startIdx += 1

        return min_window






# Correct, too slow
class Solution_1:
    def minWindow(self, s, t):
        chrsToLookFor = {}

        for chr in t:
            if chr not in chrsToLookFor:
                chrsToLookFor[chr] = 1
            else:
                chrsToLookFor[chr] += 1

        chrToIdx = {}

        for chr in chrsToLookFor:
            chrToIdx[chr] = deque()

        resLen = float('inf')
        res = ""

        def dictContainsString(currentDict, targetDict):
            minVal, maxVal = float('inf'), float('-inf')

            for key in targetDict:
                if key not in currentDict or len(currentDict[key]) != targetDict[key]:
                    return False, 0, ""

                minVal = min(minVal, currentDict[key][0])
                maxVal = max(maxVal, currentDict[key][-1])

            return True, maxVal-minVal, s[minVal: maxVal+1]

        # print(chrsToLookFor)

        for idx, chr in enumerate(s):
            validDict, length, subStr = dictContainsString(chrToIdx, chrsToLookFor)

            if validDict and length < resLen:
                res = subStr
                resLen = length

            if chr in chrsToLookFor:
                chrToIdx[chr].append(idx)

                if len(chrToIdx[chr]) > chrsToLookFor[chr]:
                    chrToIdx[chr].popleft()


            # print("idx: {}".format(idx))
            # print(chrToIdx)

        validDict, length, subStr = dictContainsString(chrToIdx, chrsToLookFor)

        if validDict and length < resLen:
            res = subStr
            resLen = length

        return res

print(Solution().minWindow("cabwefgewcwaefgcf","cae"))

print(Solution().minWindow("ADOBECODEBANC", "ABC"))

print(Solution().minWindow("A", "B"))




'''
 01234567890123456
"cabwefgewcwaefgcf"
             ^

"cae"

{'c': 1, 'a': 1, 'e': 1}

{
    'c': [9],
    'a': [11],
    'e': [12],
}


'''
