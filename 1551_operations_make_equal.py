'''
Given List[int], arr

arr[i] = (2 * i) + 1

Operation(x,y):
    arr[x] -= 1
    arr[y] += 1

How many operations do you need to peform to make all
elements of the array equal?

n = 5

[1, 3, 5, 7, 9]

If arr has odd length, make all elements equal to middle element,
some power of 2^i, i is idx-middle

[1, 3, 5, 7, 9]
 4

If arr is even length,
Make closest middle elements equal to each other, one operation
Evey subsequent element: 1 + 2^i

'''

class Solution:
    def minOperations(self, n):
        if n < 2:
            ans = 0

        elif n % 2 == 0:
            ans = 1
            n -= 2
            n = n // 2

            for i in range(1, n+1):
                ans += 2*i + 1

        else:
            # isOdd
            ans = 0
            n -= 1
            n = n // 2

            for i in range(1, n+1):
                ans += 2*i

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(3))
    print(s.minOperations(6))
    print(s.minOperations(31))
