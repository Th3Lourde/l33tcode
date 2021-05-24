class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        l = 0
        r = len(people)-1
        boats = 0

        while l < r:
            if people[l]+people[r] <= limit:
                l += 1
                r -= 1
                boats += 1
            else:
                r -= 1
                boats += 1

        if l == r:
            boats += 1

        return boats

s = Solution()
print(s.numRescueBoats([1,2], 3))
print(s.numRescueBoats([3,2,2,1], 3))
print(s.numRescueBoats([3,5,3,4], 3))
