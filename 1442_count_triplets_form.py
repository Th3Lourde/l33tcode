'''
Given an array of integers, arr[int]:

Select indices, (i,j,k) ∋ i ≤ j ≤ k ⩓:

arr[i] ^ arr[i+1] ^ ... ^ arr[j-1] == arr[j] ^ arr[j+1] ^ ... ^ arr[k]

Return the number of indices that this is true for.

Where ^ is the bitwise xor expression

According to: https://stackoverflow.com/questions/14526584/what-does-the-xor-operator-do#:~:text=XOR%20is%20a%20binary%20operation,corresponding%20bits%20of%20a%20number

This operation is also the same as addition modulo 2.

So we are going to itr through all possible options.

We are also going to eval whether or not the subarrays fit.

It would be nice if we could just update each current sum as we add/subtract numbers
from the sublist that we are working with.

1) Initialize a and b based upon starting point
2) Add/Subtract elements from a,b

[2,3,1,6,7]
 i j     k

(3^4^5)^5 = (3^4)

 a = [2] | b = [3,1,6,7]
 a = [2,3] | b = [1,6,7]
 a = [2,3,1] | b = [6,7]
 a = [2,3,1,6] | b = [7]

7^10 == 13
13 ^ 7 == 10
13 ^ 10 == 7

So we can have our queue of elements as well as the current ^.
When we remove an element, pop from front, a ^= A.pop()



 a = [2], (2) | b = [3,1,6,7], (3)




 a = [2,3] | b = [1,6,7]
 a = [2,3,1] | b = [6,7]
 a = [2,3,1,6] | b = [7]

Initialize values with ijk split

a is left list partition
b is right list partition

While j <= k:
    pop b, catch term, append to a
    compare both a,b
    j += 1

1) Check Initialization first
2) Check iteration second



[2,3,1,6,7]

Second time through was much better, go me.



'''

class Solution:
    def countTriplets(self, arr):
        ans = 0

        for i in range(len(arr)-1):

            for k in range(len(arr)-1, i, -1):
                if k == len(arr)-1:
                    B = arr[k]

                    for z in range(k-1, i, -1):
                        B ^= arr[z]

                    b = B
                    # print("[A] Bitwise for: {} = {}".format(arr[i+1: len(arr)], b))

                else:
                    B ^= arr[k+1]
                    b = B

                    # print("[B] Bitwise for: {} = {}".format(arr[i+1: k+1], b))

                a = arr[i]


                for j in range(i+1, k+1):
                    # print(j)
                    a ^= arr[j]
                    b ^= arr[j]


                    if a == b:
                        # print("[ans] {} {} {}".format(i, j, k))
                        ans += 1

                    # else:
                    #     print("[term] {} {} {}".format(i, j, k))


        return ans




    def countTriplets_2(self, arr):

        class xorClass:
            def __init__(self, vals):
                self.val = vals[0]

                for i in range(1,len(vals)):
                    self.val ^= vals[i]

                self.vals = vals

            def __repr__(self):
                return self.val

            def __str__(self):
                return "repr: {} val: {}".format(self.vals, self.val)

            def pushValue(self, val):
                self.val ^= val
                self.vals.append(val)

            def popVal(self):
                term = self.vals[0]
                self.vals = self.vals[1:]
                self.val ^= term
                return term

        i = 0

        ans = 0

        print("arr: {}".format(arr))

        while i < len(arr)-1:
            k = len(arr)
            j = i+1 # Del me

            # Initialize a,b
            a = xorClass(arr[i:j])
            b = xorClass(arr[j:k])

            print(a)
            print(b)

            while i < k:

                j = i+1

                a = xorClass(arr[i:j])
                b = xorClass(arr[j:k])

                while j < k-1:
                    if a.val == b.val:
                        ans += 1
                    # check a == b
                    j += 1
                    tmp = b.popVal()
                    a.pushValue(tmp)

                    print(a)
                    print(b)


                k -= 1

                if i+1 < k:
                    a = xorClass(arr[i:i+1])
                    b = xorClass(arr[i+1:k])

                else:
                    break

                print("")
                print(a)
                print(b)

            i += 1
            # return


        return ans







    def countTriplets_1(self, arr):

        def validTrpl(tpl):
            a = arr[tpl[0]]
            b = arr[tpl[1]]

            for i in range(tpl[0]+1, tpl[1]):
                a ^= arr[i]

            for j in range(tpl[1]+1, tpl[2]+1):
                b ^= arr[j]

            return a == b

        ans = 0

        for i in range(0, len(arr)-1):
            k = len(arr)-1

            while i+1 <= k:
                j = i+1

                while j <= k:
                    trpl = (i,j,k)

                    if validTrpl(trpl):
                        ans += 1

                    j += 1

                k -= 1

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.countTriplets([2,3,1,6,7]))
    print(s.countTriplets([1,1,1,1,1]))
    print(s.countTriplets([2,3]))
    print(s.countTriplets([1,3,5,7,9]))
    print(s.countTriplets([7,11,12,9,5,2,7,17,22]))
