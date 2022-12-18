'''
Design a hit counter:

Design a hit counter which counts the number of hits received in the past 5 minutes
(300 seconds)

So you are getting hits at times that are monotonically increasing
You want to count the number of hits

So keep all of the hits in a list, when you get timestamp you perform binary search
on the hits that happened 300 seconds from timestamp (if negative hold at zero).


'''

import bisect

class HitCounter:

    def __init__(self):
        self.q = []

    def hit(self, timestamp):
        self.q.append(timestamp)

    def getHits(self, timestamp):
        startPoint = max(0, timestamp - 300 + 1)

        idx = bisect.bisect_left(self.q, startPoint)
        return len(self.q[idx:])
