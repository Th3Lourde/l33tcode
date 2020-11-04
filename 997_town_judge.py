
'''
A town judge exists or does not exist.
Return -1 a town judge doesn't exist.
Return the individual that is the judge if a judge exists

A person is a judge if:
    - Everyone trusts the person
    - The person trusts no one
(there's only one person that meets this criteria)

Data:
trust: List[List[int]]

Create one dictionary that contains who people trust
d[person] = [people person trusts]

Create a set of unique people. Loop through set and if
a key has a value of [], that key is the judge.

Else, return -1.

loop through trust, creating map, set as you go
then loop through set.

0(n) + 0(k), k == number of distinct people

'''

class Person:
    def __init__(self):
        self.trusts = set()
        self.isTrustedBy = set()

    def __repr__(self):
        return "(trusts: {} | isTrustedBy: {})".format(self.trusts, self.isTrustedBy)

class Solution:

    # Re-Write With Non-Class Def
    def findJudge(self, n, trust):
        if not trust and n == 1:
            return n
        elif not trust:
            return -1

        people = {}

        for whoTrusts, isTrusted in trust:
            if whoTrusts not in people:
                people[whoTrusts] = Person()

            if isTrusted not in people:
                people[isTrusted] = Person()

            people[whoTrusts].trusts.add(isTrusted)
            people[isTrusted].isTrustedBy.add(whoTrusts)

        print(people)

        for id in people:
            person = people[id]

            if person.trusts == set() and len(person.isTrustedBy) == n-1: return id

        return -1


if __name__ == '__main__':
    s = Solution()

    print(s.findJudge(2, [[1,2]]))
