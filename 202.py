class Solution:
    def isIsomorphic(self, s, t):
        dictA = {}
        dictB = {}

        for idx, chr in enumerate(s):
            if chr not in dictA:
                dictA[chr] = [idx]
            else:
                dictA[chr].append(idx)

        for idx, chr in enumerate(t):
            if chr not in dictB:
                dictB[chr] = [idx]
            else:
                dictB[chr].append(idx)

        seen = set()

        for i in range(len(s)):
            if i in seen:
                continue

            listA = dictA[s[i]]
            listB = dictB[t[i]]

            if listA != listB:
                return False

            for idx in listA:
                seen.add(idx)

        return True

print(Solution().isIsomorphic("egg", "add"))
print(Solution().isIsomorphic("foo", "bar"))
print(Solution().isIsomorphic("paper", "title"))
