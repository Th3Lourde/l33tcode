'''
Given a data structure, employee

loop through all employees, create
an id --> importance




ans = 0

for employee in employees:
    ans += employee.importance

    for sub in employee.sub: <-- So these are actually just ids
        ans += mapping[sub]

return ans


So we care about the id that we are given.


[1,5,[2,3]]
[2,3,[4]]
[3,4,[]]
[4,1,[]]

Got it right.

'''

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        mapping = {}
        ans = 0
        person = None

        for employee in employees:
            mapping[employee.id] = employee

            if employee.id == id:
                person = employee

        ans += person.importance
        q = person.subordinates

        while q:
            sub = q.pop()

            ans += mapping[sub].importance
            q = mapping[sub].subordinates + q

        return ans
