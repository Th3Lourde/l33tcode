


class Solution:
    def groupAnagrams(self, strs):

        if len(strs) == 0:
            return []

        possibleGrams = {}
        for s in strs:
            tmp = {}
            for c in range(len(s)):
                try:
                    tmp[s[c]] += 1
                except:
                    tmp[s[c]] = 1

            unique = list(tmp.keys())
            unique.sort()

            k = ""
            for key in unique:
                k += "{}".format(key*tmp[key])

            try:
                possibleGrams[k].append(s)
            except:
                possibleGrams[k] = [s]

        return list(possibleGrams.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
