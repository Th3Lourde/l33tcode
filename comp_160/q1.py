

class Solution:
    def findSolution(self, customFunction, z):


        a = 1
        b = 1
        x = 0
        y = 0

        ans = []

        if customfunction.f(a,b) == z:
            ans.append([a,b])


        for i in range(1,1001):

            val = customfunction.f(i,i)

            if val == z:
                if [i,i] not in ans:
                    ans.append([i,i])

            for k in range(i, 1001):
                val = customfunction.f(k,i)

                if val > z:
                    break

                if val == z:
                    if [k,i] not in ans:
                        ans.append([k,i])

            for h in range(i, 1001):
                val = customfunction.f(i,h)

                if val > z:
                    break

                if val == z:
                    if [i,h] not in ans:
                        ans.append([i,h])


        return ans






        while customfunction.f(a,b) <= z:
            while customfunction.f(a+x, b) <= z:
                if customfunction.f(a+x, b) == z:
                    if [a+x, b] not in ans:
                        ans.append([a+x, b])
                x += 1
            x = 0

            while customfunction.f(a, b+y) <= z:
                if customfunction.f(a, b+y) == z:
                    if [a, b+y] not in ans:
                        ans.append([a+x, b])
                y += 1

            y = 0

            a += 1
            b += 1


        return ans













if __name__ == '__main__':
    s = Solution()



'''
So we are given a function and a target value.
We want to return all (a,b) s.t. f(a,b) = z.

The solution will be on 1 <= x,y <= 1000

1 <= z <= 1000


-----------------------------------------------
We are also told that the function is constantly
increasing:
    f(x+1, y) > f(x, y)
    f(x, y+1) > f(x, y)

1) Start with f(1,1).

Check if f(a,b) > z. If so break

if f(a,b) <= z:
    - Iterate through a+1, a+2, ...
    - Iterate through b+1, b+2, ...
Then add one to a and b and keep going




'''
