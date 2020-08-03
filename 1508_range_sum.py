class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arrS = []

        for i in range(len(nums)):
            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
                arrS.append(tmp)

        arrS.sort()

        return sum(arrS[left-1:right]) % (10**9 + 7)
