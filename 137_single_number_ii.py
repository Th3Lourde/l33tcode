class Solution:
    def singleNumber(self, nums):
        singleElement = set()
        multiElement = set()

        for n in nums:
            if n not in singleElement and n not in multiElement:
                singleElement.add(n)

            elif n in singleElement and n not in multiElement:
                multiElement.add(n)
                singleElement.remove(n)

        return singleElement.pop()
