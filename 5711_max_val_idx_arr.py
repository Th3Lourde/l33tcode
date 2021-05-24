'''
Somehow there's an issue with calculating
the sum.

Do some examples, figure out what the issue is,
move on to the next problem.

dude what, literally same logic only some of the code got moved to
a different function and magically everything is better

I will give that we don't need to worry about num more than once.
'''

class Solution:
    def maxValue(self, n, index, maxSum):

        if maxSum == n:
            return 1

        def partial(x):
            return x * (x + 1) // 2

        # k is the val at arr[index]
        def calculateSum(num):
            r = n - index - 1
            l = index
            count = num
            if num <= l + 1:
                count += partial(num - 1) + l - num + 1
            else:
                count += partial(num - 1) - partial(num - l - 1)

            if num <= r + 1:
                count += partial(num - 1) + r - num + 1
            else:
                count += partial(num - 1) - partial(num - r - 1)

            return count


        l = 1
        r = maxSum

        ans = 1

        # print("Starting with l: {}, r: {}".format(l, r))

        while l < r:
            # m = (l+r)//2

            m = r - (r - l) // 2

            s = calculateSum(m)
            # print("l: {}, r: {}".format(l, r))
            # print("arr sum of m={}:{}".format(m, s))
            # print("m: {}".format(m))

            # if m == l or m == r:
            #     break

            if s <= maxSum:
                l = m
            else:
                r = m-1

        return l






    # Correct, too slow
    def maxValue_1(self, n, index, maxSum):
        arr = [1 for _ in range(n)]

        # number of additions = n
        # int((maxSum-arrSum)/n)
        # return arr[idx]+

        arrSum = n
        ans = arr[index]
        allUpdated = False

        while arrSum <= maxSum:
            ans = arr[index]


            if allUpdated == True:
                return arr[index] + int((maxSum-arrSum)/n)
                continue


            arr[index] += 1
            arrSum += 1


            # print("arrSum:{} arr:{}".format(arrSum, arr))
            lUpdated = False
            rUpdated = False

            if index == 0:
                lUpdated = True

            if index == len(arr)-1:
                rUpdated = True


            for i in range(index+1, len(arr)):
                if abs(arr[i-1]-arr[i]) > 1:
                    arr[i] += 1
                    arrSum += 1

                else:
                    break

                if i == len(arr)-1:
                    rUpdated = True
                    # print("r")

            for i in range(index-1, -1, -1):
                if abs(arr[i+1]-arr[i]) > 1:
                    arr[i] += 1
                    arrSum += 1


                else:
                    break

                if i == 0:
                    lUpdated = True
                    # print("l")

            if lUpdated and rUpdated:
                allUpdated = True

            # print("Post adjustments: {}".format(arr))

        # print(allUpdated)
        return ans

s = Solution()

'''
3
0
815094800

expected: 271698267

0 1 2
2,3,2
'''
print(s.maxValue(3,0,815094800)) # 271698267

print(s.maxValue(6,1,10)) # 3

print(s.maxValue(3,0,10)) # 4

print(s.maxValue(9,3,16)) # 3

print(s.maxValue(4,0,4)) # 1

print(s.maxValue(4,2,6)) # 2

print(s.maxValue(9,0,909))# 105
print(s.maxValue(9,5,909))
print(s.maxValue(9,0,90924720)) # 10102750
print(s.maxValue(4,2,30)) #8



print(s.maxValue(9801,8469,439132987)) # 48554
