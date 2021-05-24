'''
[10,8,0,5,3]
[2,4,1,1,3]

[position, speed]

target = 12

[
    [0,1],
    [3,3],
    [5,1],
    [8,4],
    [10,2],
]

[
    12,
    3,
    7,
    1,
    1
]

Create list like the one shown on line 10.
Then for each element, calculate time on road.

fleets initially == number of cars. Every time
time[i] <= time[i+1], fleets -= 1

10
[0,4,2]
[2,1,3]
'''
class Solution:
    def carFleet(self, target, position, speed):
        # cars = []
        fleets = len(position)

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(key=lambda x: x[0])

        # print(cars)

        for idx in range(len(cars)):
            cars[idx] = (target-cars[idx][0])/(cars[idx][1])

        # print(cars)

        # for i in range(len(cars)-1):
        #     found = False
        #     for j in range(i+1, len(cars)):
        #         if found == False and cars[i] <= cars[j]:
        #             fleets -= 1
        #             found = True

        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res


        return fleets

s = Solution()

print(s.carFleet(10, [0,4,2], [2,1,3])) # 1
print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])) # 3
