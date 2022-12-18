'''
Loop through strs

Create a dict where dict[key] = [val, ...]

The key is the chrs of the str sorted, the val is str

Once the dict is created, return the vals of the dict as a list

Create each key by splitting on "", sorting, then joining

'''

class Solution:
    def groupAnagrams(self, strs):
        dict = {}

        for str in strs:
            # 1) Create key
            chrKey = list(str)
            chrKey.sort()
            chrKey = "".join(chrKey)

            # 2) Add key to dict
            if chrKey in dict:
                dict[chrKey].append(str)
            else:
                dict[chrKey] = [str]

        # 3) return vals
        return list(dict.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
