import heapq as h
class Solution:
    def getNumberOfBacklogOrders(self, orders):
        sellHeap = []
        buyHeap = []

        for order in orders:

            # buy
            if order[2] == 0:
                while sellHeap and order[1] > 0:
                    minVal = sellHeap[0]

                    if minVal[0] <= order[0]:
                        # order executed
                        executed = min(minVal[1], order[1])
                        order[1] -= executed

                        sellHeap[0] = (minVal[0], minVal[1]-executed)

                        if sellHeap[0][1] < 1:
                            h.heappop(sellHeap)

                    else:
                        break

                if order[1] > 0:
                    h.heappush(buyHeap, (order[0]*-1, order[1]))

            # sell
            else:
                while buyHeap and order[1] > 0:
                    minVal = buyHeap[0]

                    if minVal[0]*(-1) >= order[0]:
                        # order executed
                        executed = min(minVal[1], order[1])
                        order[1] -= executed

                        buyHeap[0] = (minVal[0], minVal[1]-executed)

                        if buyHeap[0][1] < 1:
                            h.heappop(buyHeap)

                    else:
                        break

                if order[1] > 0:
                    h.heappush(sellHeap, (order[0], order[1]))

            # print("sellHeap: {}".format(sellHeap))
            # print("buyHeap: {}".format(buyHeap))

        backLog = 0

        for s in sellHeap:
            backLog += s[1]

        for b in buyHeap:
            backLog += b[1]

        return backLog % (10**9 + 7)

s = Solution()

print(s.getNumberOfBacklogOrders([[26,7,0],[16,1,1],[14,20,0],[23,15,1],[24,26,0],[19,4,1],[1,1,0]]))

print(s.getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]]))
print(s.getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]))
