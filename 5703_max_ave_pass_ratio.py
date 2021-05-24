import heapq
# I got the right answer, but my custom heap initialization
# isn't fast enough :/
class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        hp = [(a/b - (a+1)/(b+1), a, b) for a, b in classes]
        heapq.heapify(hp)

        for student in range(extraStudents):
            key, a, b = heapq.heappop(hp)
            heapq.heappush(hp, ( (a+1)/(b+1) - (a+2)/(b+2), a+1, b+1 ))

        return sum(a / b for _, a, b in hp) / len(classes)





s = Solution()

print(s.maxAverageRatio([[2,2]], 2))
print(s.maxAverageRatio([[1,2],[3,5],[2,2]], 2))
print(s.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))
