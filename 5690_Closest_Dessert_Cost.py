class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        dist = float('inf')
        cost = float('inf')
        toppingSet = [set({0})]

        def populateToppings(idx, cost, toppingSet):
            toppingSet[0].add(cost)
            if idx >= len(toppingCosts):
                return


            for i in range(idx, len(toppingCosts)):
                populateToppings(i+1, cost, toppingSet)
                populateToppings(i+1, cost+toppingCosts[i], toppingSet)
                populateToppings(i+1, cost+toppingCosts[i]*2, toppingSet)

        populateToppings(0, 0, toppingSet)

        toppings = list(toppingSet[0])

        for base in baseCosts:
            for topping in toppings:
                actual = topping+base

                if abs(target-actual) < dist:
                    dist = abs(target-actual)
                    cost = actual
                elif abs(target-actual) <= dist and actual < cost:
                    cost = actual
        return cost

if __name__ == '__main__':
    s = Solution()
    print(s.closestCost([3,10], [2,5], 9))
