from collections import deque

class Solution:
    def addBinary(self, a, b):
        ans = deque()
        one = 0
        ptr1 = len(a)-1
        ptr2 = len(b)-1

        while ptr1 >= 0 and ptr2 >= 0:
            s = one

            if a[ptr1] == "1":
                s += 1

            if b[ptr2] == "1":
                s += 1

            one = 0

            if s % 2 == 0:
                ans.appendleft("0")
            elif s == 1:
                ans.appendleft("1")
            else:
                ans.appendleft("1")
                one = 1

            if s > 1:
                one = 1

            ptr1 -= 1
            ptr2 -= 1

        while ptr1 >= 0:
            s = one
            one = 0

            if a[ptr1] == "1":
                s += 1

            if s % 2 == 0:
                ans.appendleft("0")
            elif s == 1:
                ans.appendleft("1")
            else:
                ans.appendleft("1")
                one = 1

            if s > 1:
                one = 1

            ptr1 -=1

        while ptr2 >= 0:
            s = one
            one = 0

            if b[ptr2] == "1":
                s += 1

            if s % 2 == 0:
                ans.appendleft("0")
            elif s == 1:
                ans.appendleft("1")
            else:
                ans.appendleft("1")

            if s > 1:
                one = 1

            ptr2 -= 1

        if one:
            ans.appendleft("1")

        return "".join(list(ans))

print(Solution().addBinary("1010", "1011"))
print(Solution().addBinary("11", "1"))
