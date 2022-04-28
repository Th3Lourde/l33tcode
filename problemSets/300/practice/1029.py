'''
A company is planning to interview 2n people.
Given the array costs, where cost[i] = [aCost, bCost]

cost of flying ith person to city a is acost
cost of flying ith person to city b is bcost

return the minimum cost to fly every person to a
city such that n people arrive in each city

So we have 2n people
we have two cities
each person carries a cost of going to city a vs city b

minimize the cost needed to fly people to different places.

So we can brute force it until we get the optimal solution.

2nCn

For each person, send them to the city that costs less

Then take the city that we have too much of, sort and then move
the least costly person to the next city.

[10,20],[30,200],[400,50],[30,20]
                           ^


a = [
[10,20],
[30,200],

]

b = [
[400,50],
[30,20],
]


'''

class Solution:
    def twoCitySchedCost(self, costs):
        city_a = []
        city_b = []
        cost = 0

        for aCost, bCost in costs:
            city_a.append([aCost, bCost])

        # print("b4 opt")
        # print(city_a)
        # print(city_b)

        if len(city_a) > len(costs)/2:
            city_a.sort(key=lambda x: x[1]-x[0], reverse=True)

            print("Post sort")
            print(city_a)

            while len(city_a) > len(costs)//2:
                city_b.append(city_a.pop())

        else:
            city_b = sorted(city_b, key=lambda x: x[0]-x[1], reverse=True)

            # print("Post sort")
            # print(city_b)

            while len(city_b) > len(costs)/2:
                city_a.append(city_b.pop())


        print("after opt")
        print(city_a)
        print(city_b)

        for aCost, _ in city_a:
            cost += aCost

        for _, bCost in city_b:
            cost += bCost

        return cost


print(Solution().twoCitySchedCost([[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]))

print(Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
print(Solution().twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))
