'''
Given a collection of integers that
might contain duplicates, return all
possible subsets.

Perform one linear pass store all elements with duplicates.

[1,2,2,3,4,4]

[1,2,2]

1, 1,2, 1,2,2
2, 2,2, []

[[],[1],[1,2],[1,2,2],[1,2,2,3],[1,2,2,3,4],[1,2,2,3,4,4],[1,2,2,4],[1,2,2,4,4],[1,2,3],[1,2,3,4],[1,2,3,4,4],[1,2,4],[1,2,4,4],[1,3],[1,3,4],[1,3,4,4],[1,4],[1,4,4],[2],[2,2],[2,2,3],[2,2,3,4],[2,2,3,4,4],[2,2,4],[2,2,4,4],[2,3],[2,3,4],[2,3,4,4],[2,4],[2,4,4],[3],[3,4],[3,4,4],[4],[4,4]]

Sort the list then apply a backtracking algo.

(nums, idx, ans)

'''

class Solution:
    def subsetsWithDup(self, nums):

        nums.sort()

        def itr(nums, idx, term, ans):

            if idx >= len(nums):
                if term not in ans:
                    ans.append(term)
                return

            itr(nums, idx+1, term + [nums[idx]], ans)

            itr(nums, idx+1, term, ans)

        ans = []

        itr(nums, 0, [], ans)

        return ans


if __name__ == '__main__':
    s = Solution()

    s.subsetsWithDup([1,2,2])
