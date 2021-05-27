'''
Given an array of strs, return a list of list of strings.
Where each element in the list represents strs in input that
are anagrams of each other

Each index in response list will have a counter that represents
the chrs that are present in the list

'''

from collections import Counter

class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]

        return list(anagrams.values())

# Correct, slow
class Solution_1:
    def groupAnagrams(self, strs):
        idxToCounter = {}
        responseList = []

        def equal(counter1, counter2):
            for key in counter1:
                if counter1[key] != counter2[key]:
                    return False

            for key in counter2:
                if counter1[key] != counter2[key]:
                    return False

            return True

        for word in strs:
            chrFreq = Counter(word)
            noMapping = True

            for idx in idxToCounter:
                if len(idxToCounter[idx]) == len(chrFreq) and equal(idxToCounter[idx],chrFreq):
                    responseList[idx].append(word)
                    noMapping = False
                    break

            if noMapping:
                idxToCounter[len(responseList)] = chrFreq
                responseList.append([word])

        return responseList

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat", "teaa"]))

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
print(Solution().groupAnagrams(["a",""]))
