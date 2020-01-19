

'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Ok, so given an array, we should put all of the even elements at the front and all of the odd elements at the back

Have two variables: e, o

array[0:e+1] contains all of the even elements that we have currently seen
array[o:len(array)-1] contains all of the elements that we have seen so far that we know are odd

1) Find initial placement for e
2) Find initial placement for o
3) Move e,o until e == o
return array
'''

class Solution:
    def sortArrayByParity(self, A):
        if len(A) == 1:
            return A

        e = 0
        o = len(A)-1

        if A[e]%2 != 0:
            # find even element
            while A[e]%2 != 0 and e < len(A)-1:
                e += 1

            if A[e]%2 == 0:
                tmp = A[e]
                A[e] = A[0]
                A[0] = tmp
                e = 0
                # we now have even element

            else:
                print("No even elements")
                return A

        print("Found even element: {}".format(A[0]))

        if A[o]%2 != 1:
            # find odd element
            while A[o]%2 != 1 and o > 0:
                o -= 1

            if A[o]%2 == 1:
                tmp = A[o]
                A[o] = A[-1]
                A[-1] = tmp
                o = len(A)-1

            else:
                print("No odd elements")
                return A

        print("Found odd element: {}".format(A[-1]))

        # if we get here, we know that we have an even element on the LHS
        # and an odd element on the RHS

        '''
        So how do we want to do this?
        have e increment
        if element is odd,
        we want to switch
        '''

        e += 1
        while (e <= len(A)-1 and o >= 0) and e < o:
            if A[e]%2 != 0:
                # find an odd element to replace it with
                if A[o]%2 == 0:
                    tmp = A[e]
                    A[e] = A[o]
                    A[o] = tmp

                    e += 1
                    o -= 1

                elif A[o]%2 != 0:
                    while A[o]%2 != 0 and o > e:
                        o -= 1
                    if o == e:
                        return A

                    elif A[o]%2 == 0:
                        tmp = A[e]
                        A[e] = A[o]
                        A[o] = tmp

                        e += 1
                        o -= 1

            elif A[e]%2 == 0:
                e += 1

        return A






'''
Simpler solution:
loop through list, record the indicies of even integers, odd integers
create a new list, copy the even integers there, followed by the odd integers,
return the new list

requires you to make a copy of the list, and loop through elements twice
Run-Time: 0(2n)
Memory Complexity: 0(n)
'''


if __name__ == '__main__':
    s = Solution()
    A = [2,3,4,9,11,13]
    print(s.sortArrayByParity(A))
