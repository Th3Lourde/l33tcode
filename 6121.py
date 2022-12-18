import heapq

class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        ans = []

        for k, trim in queries:
            heap = []
            for idx, num in enumerate(nums):
                digit = len(num)
                digit -= trim
                strNum = num[digit:]
                # print(strNum)
                if len(strNum) > 0:
                    heapq.heappush(heap, (int(strNum), idx))

            # print(heap)
            # continue

            for _ in range(k-1):
                _ = heapq.heappop(heap)

            minVal, minIdx = heapq.heappop(heap)

            while heap:
                tmpVal, tmpIdx = heapq.heappop(heap)

                if minVal == tmpVal:
                    minIdx = min(minIdx, tmpIdx)

            ans.append(minIdx)

        return ans


print(Solution().smallestTrimmedNumbers(["24","37","96","04"],[[2,1],[2,2]]))

print(Solution().smallestTrimmedNumbers(["102","473","251","814"],[[1,1],[2,3],[4,2],[1,2]]))
