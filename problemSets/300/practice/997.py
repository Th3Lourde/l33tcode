'''
People labeled 1 --> n

A person is a judge, or is not a judge.

If the person is a judge:
    - They trust no-one
    - Everyone trusts them (except themselves)
    - They are the only person that satisfies the first two properties

Given list of elements

trust[i] = [a_i, b_i]

a_i trusts b_i

dict of potential judges
as we loop through trust list,
 - If person trusts themselves, remove from list
 - If person is trusted by someone else, add them to list

When done, if the number of people in the dict is 1, return that
person

return -1


n = 3,
trust = [[1,3],[2,3]]
                  ^

potential_judges
pj = {
    1:set(),
    2:set(),
    3:set({1,2}),
}

pj[3] --> the people that trust person 3

Loop through pj, if len(value) == n-1, store person
if person already populated, return -1

n = 3, trust = [[1,3],[2,3],[3,1]]
                             a,b


pj = {
}

testCases:
- Two judges | -1
- One judge  | judge
- no judge b/c they are not trusted | -1
- One judge, judge trusts person | -1


'''

class Solution:
    def findJudge(self, n, trust):
        pj = {}

        for i in range(1, n+1):
            pj[i] = 0

        for a, b in trust:
            if b in pj:
                pj[b] += 1

            if a in pj:
                pj[a] = -1*n

        judge = -1

        for person in pj:
            if pj[person] == n-1:
                # print(person)
                if judge == -1:
                    judge = person
                else:
                    return -1

        return judge

print(Solution().findJudge(4, [[1,3],[2,3],[1,4],[2,4]]))
print(Solution().findJudge(4, [[1,2]]))
print(Solution().findJudge(2, [[1,2]]))
print(Solution().findJudge(3, [[1,3],[2,3]]))
print(Solution().findJudge(3, [[1,3],[2,3],[3,1]]))
