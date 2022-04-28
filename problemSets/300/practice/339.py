'''
What we really want is a function that, given
a NestedInteger, can return the sum.

I feel like we will need recursion.

Given ni[NestedInteger], return it's value

(recursive sum)
r_c(ni, depth)

return the sum of this NestedInteger

r_c(ni, 1)


[1,[4,[6]]]
    ^

r_c([1,[4,[6]]], 0)
    returnSum = 0

    r_c(1,1)
    |--> returns 1

    r_c([4,[6]],1)
        returnSum = 0

        r_c(4,2)
        |--> return 4*2=8

        r_c([6],2)
            r_c(6,3)
'''

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]):

        def r_c(ni, depth):
            if ni.isInteger():
                return ni.getInteger()*depth

            returnSum = 0

            for ni_item in ni.getList():
                returnSum += r_c(ni_item, depth+1)

            return returnSum

        returnSum = 0

        for ni_item in nestedList:
            returnSum += r_c(ni_item , 1)

        return returnSum
