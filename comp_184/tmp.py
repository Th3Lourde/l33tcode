
import math
def NcK(n,k):
    top = math.factorial(n)
    bottom = math.factorial(k)*math.factorial(n-k)
    return top/bottom


def test(n):
    ans = NcK(12,n) - 12*math.factorial(n-1)
    print("[n:{}] = {}".format(n,ans))


for i in range(1,4):
    test(i)
