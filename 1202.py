from collections import deque

class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        pairDict = {}
        swapSets = []
        splitS = list(s)

        for l, r in pairs:
            if l in pairDict:
                pairDict[l].add(r)
            else:
                pairDict[l] = set({r})

            if r in pairDict:
                pairDict[r].add(l)
            else:
                pairDict[r] = set({l})

        keysLeft = set(pairDict.keys())

        # print(keysLeft)

        for key in pairDict:
            if key not in keysLeft:
                continue

            keysToItr = deque([key])
            tmpSet = set({})

            while len(keysToItr) > 0:
                newKey = keysToItr.pop()

                if newKey in tmpSet:
                    continue

                tmpSet.add(newKey)

                for k in pairDict[newKey]:
                    keysToItr.appendleft(k)

            swapSets.append(tmpSet)
            keysLeft -= tmpSet

        for swapSet in swapSets:
            chrList = []
            idxList = []

            for idx in swapSet:
                idxList.append(idx)
                chrList.append(s[idx])

            chrList.sort()
            idxList.sort()

            for i in range(len(idxList)):
                splitS[idxList[i]] = chrList[i]

        return "".join(splitS)

print(Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]))
print(Solution().smallestStringWithSwaps("dcab", [[0,2],[1,2], [4,5], [6,7], [5,6]]))
