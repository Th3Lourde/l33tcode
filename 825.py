'''
n people on a social media website.

ages[i] is the age of the ith person

Person x will not send a friend request to a person y
(x != y) if any of the following conditions is true:

age[y] <= .5 * age[x] + 7
age[y] > age[x]
# age[y] > 100 && age[x] < 100

else x will send a friend request to y.

so for every age, move left until won't friend, move right until
won't friend, then move to the next age.
'''

class Solution:
    # TLE
    def numFriendRequests_1(self, ages):
        ages.sort()

        def willFriend(x,y):
            # if ages[y] == ages[x]:
            #     return True
            # elif ages[y] <= .5*ages[x] + 7:
            if ages[y] <= .5*ages[x] + 7:
                return False
            elif ages[y] > ages[x]:
                return False
            # elif ages[y] > 100 and ages[x] < 100:
            #     return False

            return True

        friendRequests = 0

        for x in range(0, len(ages)):
            for y in range(x-1, -1, -1):
                if willFriend(x, y):
                    friendRequests += 1
                else:
                    break

            for y in range(x+1, len(ages)):
                if willFriend(x, y):
                    friendRequests += 1
                else:
                    break

        return friendRequests

    def numFriendRequests(self, ages):
        ageToCount = {}
        friendRequests = 0

        for i in range(0, 121):
            ageToCount[i] = 0

        for age in ages:
            ageToCount[age] += 1

        for age in range(15, 121):
            validFriendAge = int(0.5*age + 8)

            while validFriendAge <= age:
                friendRequests += ageToCount[validFriendAge] * (ageToCount[age] - (age == validFriendAge))
                validFriendAge += 1

        return friendRequests



print(Solution().numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110])) # 29
print(Solution().numFriendRequests([101, 56, 69, 48, 30])) # 4

print(Solution().numFriendRequests([16,16])) # 2
print(Solution().numFriendRequests([16,17,18])) # 2
print(Solution().numFriendRequests([20,30,100,110,120])) # 3
