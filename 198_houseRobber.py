
'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.

Ok so you are determining the most lucrative 'walk' through nums
where you have the option to take a step of length 2 or 2+ for every
step.

Logic dictates that you (probably) want to maximize the number of steps you take
The complexities of the problem come into play when you might miss high-value
houses if you simply hit every other house.

One approach would be to identify the most-valuable houses and then to construct
a path such that you are able to hit all of them. There can of course be valuable
houses next to each other so we will want to include the ability to pick houses
based upon a net gain.

The brute-force solution would be to find all possible (legal) paths through the
neighborhood and return the max one. Implement this first.

Looked up the solution online. Happy with this decision. Not sure I would have
gotten it if I hadn't looked it up. Onto the next one.
'''


class Solution:
    def rob(self, nums):
        even_sum = 0
        odd_sum = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum = max(even_sum + nums[i], odd_sum)

            else:
                odd_sum = max(even_sum, odd_sum + nums[i])

        return max(even_sum, odd_sum)


if __name__ == '__main__':
    s = Solution()
