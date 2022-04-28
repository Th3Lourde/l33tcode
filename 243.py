class Solution:
    def shortestDistance(self, wordsDict, word1, word2):
        trimmedDict = []
        minDist = float('inf')

        for idx, word in enumerate(wordsDict):
            if word == word1 or word == word2:
                trimmedDict.append((idx, word))

        for idx in range(len(trimmedDict)-1):
            if trimmedDict[idx][1] != trimmedDict[idx+1][1]:
                minDist = min(minDist, trimmedDict[idx+1][0]-trimmedDict[idx][0])

        return minDist

print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))
