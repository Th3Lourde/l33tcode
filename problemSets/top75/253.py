'''
Given an array of meeting time intervals where
intervals[i] = [start_i, end_i], return the minimum
number of conference rooms required.

Ok so interval problem, find at which point there is
a maximum of intervals intersecting

This problem is way easier if we sort the list, so
sort it.

maxRoomsRequired = 1
roomsRequired = 1
min = 0
max = 30

if nextElement <= max:
    roomsRequired += 1
    min = nextElement[0]
    max = nextElement[1]
    # go to next element

else:
    maxRoomsRequired = max(maxRoomsRequired, roomsRequired)

    min = element[0]
    max = element[1]
    roomsRequired = 1

maxRoomsRequired = max(maxRoomsRequired, roomsRequired)

[[0,30],[5,10],[15,20]]
  ^


[[0,30],[5,10],[15,20],[16,19],[17,18]]
                ^

if interval[1] < stack[-1]:
    append interval[1] to stack
    start = interval[0]

else:
    while stack and interval[0] > stack[-1]:
        stack.pop()

    append interval[1] to stack
    stack = interval[0]

start = 5
stack = [30]
'''

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        heap = []
        intervals.sort()

        for i in intervals:
            if heap == [] or heap[0] > i[0]:
                heapq.heappush(heap, i[1])
            else:
                heapq.heapreplace(heap, i[1])

        return len(heap)
