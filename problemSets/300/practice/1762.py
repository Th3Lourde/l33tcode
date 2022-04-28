'''
There are n buildings in a line

Youare given an integer array heights with len() of n.

arr[i] represents the height of building i

Ocean is to the right of the buildings

arr[i] has a view of the ocean if for all x in [i+1, n] arr[i] > arr[x]

return a list of indices (0-idx'd) that represent the buildings that have an
ocean view, sorted in increasing order.

[4,2,3,1]
 ^

[4,3,3,1]

4

[1,3,2,4]
       ^
[4,4,4,4]
'''

class Solution:
    def findBuildings(self, heights):
        ocean_view = []

        max_element = float('-inf')
        max_list = [0] * len(heights)

        for idx in range(len(heights)-1, -1, -1):
            max_element = max(max_element, heights[idx])
            max_list[idx] = max_element

        for idx in range(len(heights)-1):
            if heights[idx] > max_list[idx+1]:
                ocean_view.append(idx)

        ocean_view.append(len(heights)-1)

        return ocean_view

print(Solution().findBuildings([2,2,2,2]))
print(Solution().findBuildings([4,2,3,1]))
print(Solution().findBuildings([4,3,2,1]))
print(Solution().findBuildings([1,3,2,4]))
