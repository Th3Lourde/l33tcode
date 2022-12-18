class Solution:
    def groupAnagrams(self, strs):
        d = {}

        for word in strs:
            chrMapping = {}

            for chr in word:
                if chr in chrMapping:
                    chrMapping[chr] += 1
                else:
                    chrMapping[chr] = 1

            key = []

            chrMappingKeys = list(chrMapping.keys())
            chrMappingKeys.sort()

            for chrKey in chrMappingKeys:
                key.append("{}{}".format(chrKey, chrMapping[chrKey]))

            key = "".join(key)

            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]

        return list(d.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
