'''
Given two strings s and p
return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Given two strings s and p.

It is possible that anagrams of p exist in s.
Find all anagrams of p in s and for each anagram found,
    return the starting idx.

Idea:
Sliding window, form a dictionary and add characters
and remove characters.

s = "cbaebabacd", p = "abc"

Every time the dict has enough chr, add the starting index to the list.

So we can compare dictionaries, comparing checks if the keys/values are the same
'''

class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []

        target_dict = {}

        for chr in p:
            if chr in target_dict:
                target_dict[chr] += 1
            else:
                target_dict[chr] = 1

        def checkIfAnagram(current_dict):
            for key in target_dict:
                if key not in current_dict or target_dict[key] != current_dict[key]:
                    return False

            return True

        current_dict = {}
        ans = []

        # Initialize the sliding window into the dict
        for idx in range(len(p)):
            chr = s[idx]
            if chr in current_dict:
                current_dict[chr] += 1
            else:
                current_dict[chr] = 1

        if current_dict == target_dict:
            ans.append(0)

        idx = len(p)

        # print(current_dict)

        while idx < len(s):
            # print("new_val idx: {}".format(idx))
            # print("val_to_remove: {}".format(idx-len(p)))
            chr_to_add = s[idx]

            if chr_to_add in current_dict:
               current_dict[chr_to_add] += 1
            else:
               current_dict[chr_to_add] = 1

            chr_to_remove = s[idx-len(p)]

            current_dict[chr_to_remove] -= 1

            if checkIfAnagram(current_dict):
                ans.append(idx-len(p)+1)

            # print(current_dict)

            idx += 1

        return ans


print(Solution().findAnagrams("cbaebabacd", "abc"))
print(Solution().findAnagrams("abab", "ab"))
print(Solution().findAnagrams( "beeaaedcbc", "c" ))
