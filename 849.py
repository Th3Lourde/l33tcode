'''
1000001
l
      r
'''

class Solution:
    def maxDistToClosest(self, seats):
        prevSeat = None
        resp = float('-inf')

        # Used when they are both ones
        def calc_distance(l,r):
            idx = l+(r-l)//2
            return min(idx-l, r-idx)

        for idx in range(len(seats)):
            if seats[idx] == 1:
                if prevSeat == None:
                    # Calculate distance between zero and the index that we are at
                    prevSeat = idx
                    resp = max(resp, idx)

                else:
                    # Calculate distance where someone should sit in order to be most alone
                    resp = max(resp, calc_distance(prevSeat, idx))
                    prevSeat = idx

        # Check if the last element is a zero
        if seats[-1] == 0:
            resp = max(resp, len(seats)-1-prevSeat)

        return resp

print(Solution().maxDistToClosest([1,0,0,0,1]))
print(Solution().maxDistToClosest([0,1,1,0,0]))
print(Solution().maxDistToClosest([0,1,0,1,0]))
print(Solution().maxDistToClosest([1,1,0,1,1]))
print(Solution().maxDistToClosest([0,0,0,1]))
print(Solution().maxDistToClosest([1,0,0,0]))
print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))
