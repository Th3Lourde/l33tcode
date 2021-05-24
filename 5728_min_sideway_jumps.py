import bisect as b
class Solution:
    def minSideJumps(self, obstacles):
        n = len(obstacles)

        c = 0

        obDict = {1:[], 2:[], 3:[]}

        for idx, lane in enumerate(obstacles):
            if lane:
                obDict[lane].append(idx)

        # print(obDict)

        def jumpLanes(lane):
            if lane == 1:
                return [2,3]
            elif lane == 2:
                return [1,3]
            else:
                return [1,2]

        def selectLane(unit, lane):
            # print("unit: {}, lane: {}".format(unit, lane))
            opts = jumpLanes(lane)

            val1 = 0

            if obstacles[unit] != opts[0]:
                laneArr = obDict[opts[0]]
                idx1 = b.bisect_right(laneArr, unit)

                if idx1 == len(laneArr):
                    val1 = float('inf')
                else:
                    val1 = laneArr[idx1]

            val2 = 0

            if obstacles[unit] != opts[1]:

                laneArr2 = obDict[opts[1]]
                idx2 = b.bisect_right(laneArr2, unit)

                if idx2 == len(laneArr2):
                    val2 = float('inf')
                else:
                    val2 = laneArr2[idx2]

            # print("Lane: {} = {}".format(opts[0], val1))
            # print("Lane: {} = {}".format(opts[1], val2))

            if val1 > val2:
                return opts[0]
            return opts[1]

        def itr(unit, lane, c):
            c += 1

            # if c > 8:
            #     return 0

            if unit >= n:
                return 0

            while unit < n and obstacles[unit] != lane:
                unit += 1

            if unit == n:
                return 0

            unit -= 1

            minJumps = float('inf')

            return itr(unit, selectLane(unit, lane), c)+1

            # for l in jumpLanes(lane):
            #     if obstacles[unit] != l:
            #         minJumps = min(minJumps, itr(unit, l)+1)

            # return dp[(unit,lane)]

        return itr(0, 2, 0)

s = Solution()

print(s.minSideJumps([0,1,2,3,0])) # 2
print(s.minSideJumps([0,2,1,0,3,0]))

print(s.minSideJumps([0,1,1,3,3,0])) # 0
print(s.minSideJumps( [0,2,2,1,0,3,0,3,0,1,3,1,1,0,1,3,1,1,1,0,2,0,0,3,3,0,3,2,2,0,0,3,3,3,0,0,2,0,0,3,3,0,3,3,0,0,3,1,0,1,0,2,3,1,1,0,3,3,0,3,1,3,0,2,2,0,1,3,0,1,0,3,0,1,3,1,2,2,0,0,3,0,1,3,2,3,2,1,0,3,2,2,0,3,3,0,3,0,0,1,0,2,0,0,0,2,1,2,0,2,2,3,3,3,0,0,1,1,3,0,0,0,1,2,2,1,2,1,3,2,2,3,1,3,0,1,1,1,3,0,0,0,2,0,2,0,3,1,2,3,3,2,2,2,0,0,0,1,0,0,0,0,3,0,0,0,3,0,2,1,2,3,1,0,3,3,2,0,1,1,0,1,0,2,2,2,1,3,0,3,0,2,1,1,3,1,0,1,2,2,0,2,2,0,0,3,3,1,3,0,1,1,0,3,0,2,1,2,2,0,0,0,1,2,3,1,2,1,1,2,2,1,1,0,2,3,3,3,0,2,3,2,0,0,0,1,0,2,2,0,0,2,0,2,0,1,1,0,3,1,3,3,0,1,0,3,0,3,1,2,3,1,0,0,2,3,2,0,0,3,1,2,3,2,2,3,1,3,3,2,0,1,3,0,3,2,2,3,2,1,2,2,0,3,2,0,2,1,2,2,3,1,3,2,2,0,0,1,0,3,1,3,3,0,0,2,2,2,2,0,1,0,3,1,3,3,3,0,2,3,2,0,3,3,3,3,3,3,2,2,1,1,0,3,1,3,2,3,0,0,0,2,1,1,3,1,3,2,1,3,0,1,1,3,2,2,1,0,0,3,2,1,3,2,3,3,2,1,2,0,2,2,0,2,2,3,2,0,2,3,3,1,1,2,0,1,1,1,2,3,2,1,2,1,0,2,3,1,1,3,3,2,0,1,3,2,3,3,0,1,2,3,2,1,1,2,1,0,0,1,0,3,1,1,1,0,2,0,2,2,3,0,1,0,2,0,0,3,1,1,2,0,0,2,1,1,0,2,2,2,3,1,2,0,1,2,0,1,2,1,2,3,1,1,1,1,0,3,3,2,1,0,0,1,0,3,0,0,2,2,2,1,1,2,1,2,1,1,2,0,3,1,3,2,1,2,2,3,1,0,1,1,1,0,0,0,1,3,3,2,2,1,2,0,0,0,3,1,3,2,3,1,3,2,3,1,3,2,0,1,2,1,1,2,1,3,0,1,1,1,3,3,1,0,0,3,2,2,3,1,1,0,3,0,0,3,0,3,1,2,0,2,3,2,3,0,3,2,3,0,2,2,3,0,3,3,3,1,0,1,2,2,0,3,3,1,3,2,2,3,2,1,1,0,0,0,0,2,1,0,1,1,1,1,0,3,0,1,0,0,1,0,2,0,0,1,2,0,0,0,3,3,1,0,3,2,1,2,3,2,0,3,3,0,2,3,1,1,0,2,2,3,3,0,1,0,0,3,1,2,3,0,1,2,3,2,2,0,1,2,0,3,0,3,0,1,1,3,2,2,2,3,1,2,0,0,3,0,2,3,3,1,0,3,3,0,0,0,3,2,1,1,3,1,1,1,1,1,1,3,3,3,0,0,1,1,1,1,2,2,0,1,0,2,2,0,2,1,3,1,1,1,2,1,1,0,3,1,0,2,3,0,1,2,0,0,3,1,2,3,0,0,3,1,0,2,2,0,1,1,2,2,1,3,1,2,1,0,1,2,3,2,3,0,3,1,3,0,2,0,3,1,1,0,3,2,0,3,0,2,0,0,3,3,1,1,1,0,0,1,1,1,2,3,1,3,1,2,0,0,3,3,0,3,3,0,0,0,3,3,0,3,3,2,3,3,3,3,1,1,1,3,1,1,3,3,1,0,0,3,1,2,0,2,0,3,0,2,1,0,1,0,2,3,3,3,2,3,3,2,0,0,0,2,2,3,0,0,3,0,2,3,0,1,3,2,1,2,0,1,3,2,2,0,1,1,3,3,0,2,3,0,3,3,1,2,3,2,1,0,2,3,2,2,2,3,0,1,1,3,1,0,2,1,3,2,2,2,3,3,1,1,1,3,2,3,1,0,2,3,0,2,3,0,1,3,3,1,1,1,1,0,1,1,2,2,0,2,1,1,0,1,0,3,1,1,1,3,3,2,1,2,3,2,2,3,1,0,3,2,0,1,0,1,3,3,3,0,3,3,2,3,1,2,2,1,1,0,0,3,0]))


'''
Ok so can we find a deterministic way to pick which
lane we wish to jump to?

We are already skipping lanes that have obstacles.

So the question is really: given an option between
two lanes, which lane do we pick?

My guess would be whichever one hits an obstacle later.

If lane A hits obstacle in two units and
lane B hits obstacle in three, use lane B

It's probably be better to do an initial loop and store
what index obstacles for each lane are located.

Then, given a unit and a lane, find the smallest obstacle of a
specific lane > unit. Binary search?

'''
