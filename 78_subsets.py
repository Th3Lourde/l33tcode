'''
Given an integer array nums of unique elements,
return all possible subsets.

[
    [],
    [1],
    [2],
    [1,2],
    [3],
    [1,3],
    [2,3],
    [1,2,3],
]

[1,2,3]
     ^


'''

class Solution:
    def subsets(self, nums):
        resp = [[]]

        for num in nums:
            newTerms = []
            for e in resp:
                newTerms.append(e + [num])
                
            resp += newTerms

        return resp

print(Solution().subsets([1,2,3]))
