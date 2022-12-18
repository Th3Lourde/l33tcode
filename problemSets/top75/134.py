'''
[1,2,3,4,5]
[3,4,5,1,2]

[-2,-2-2,3,3]

# Do two full rotations
write a function where you enter in the starting idx and the gas
and you get out how far you get

let's return the number of gas stations that we start at, as well
as the index that we end at

if # gas stations is == len(gas), we have found our index

try each gas station
'''


class Solution:
    def canCompleteCircuit(self, gas, cost):
        diffs = [a-b for a,b in zip(gas, cost)]
        n = len(diffs)
        cumsum, startingIdx, i = 0, 0, 0

        while i < 2*n:
            cumsum += diffs[i%n]

            if cumsum < 0:
                if i+1 >= n:
                    return -1

                startingIdx = i+1
                cumsum = 0

            i += 1

        return startingIdx

print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(Solution().canCompleteCircuit([2,3,4], [3,4,3]))
