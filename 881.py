'''
You are given an array of people where
people[i] is the weight of the ith person
and an infinite number of boats where each
boat can carry a max weight of limit.

Each boat can carry at most two people at
a time, provided the sum of the weight of
those people is at most limit.

Return the minimum number of boats to carry every given person

So the game is to find the best pairings

1) Sort the list
2) pointer on left most side, pointer on right most side

assuming that the people can cross the river in any order

[3,2,2,1]

boats = 2

[1,2,2,3] | 3
   ^
   ^
'''

class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()

        l = 0
        r = len(people)-1
        boats = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1

            boats += 1

        return boats

print(Solution().numRescueBoats([1,2], 3))
print(Solution().numRescueBoats([3,2,2,1], 3))
print(Solution().numRescueBoats([3,5,3,4], 5))
