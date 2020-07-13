'''
Given an array of paths

How do we figure out where the end destination is?

Create a dictionary that maps everything, then query
the intial map until we hit the end.

[["B","C"],["D","B"],["C","A"]]

Everything has the same final destination, so we don't
need to check everything. Just one thing.

[["B","C"],["D","B"],["C","A"]]

B : C
D : B
C : A

B : C --> A done

when checking, if key isn't in dict, return key


I guess that we can have a greedier approach. Update the
keys as we go, kind like union find.


'''

class Solution:

    # Better way of doing it:
    # def solution(paths):
    #     s = set(p[0] for p in paths)
    #     for p in paths:
    #         if p[1] not in s:
    #             return p[1]


    def destCity(self, paths):

        if not paths: return none

        d = {}

        for path in paths:
            d[path[0]] = path[1]

        term = d[paths[0][0]]

        while term in d.keys():
            term = d[term]

        return term


if __name__ == '__main__':
    s = Solution()

    # print(s.destCity([["B","C"],["D","B"],["C","A"]]))
    print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
