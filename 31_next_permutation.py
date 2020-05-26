
'''
My understanding:
Return the next 'largest' permutation of a given list.

If no such permutation exists, return the list sorted in
ascending order.
|
|---> Sort and return (nlog(n))

If given an empty list:
|
|---> return it


Start at the RHS, look for the first element that is
smaller than our current element. Insert the element there.
If no such permutation exists, return the list in a flipped
form.

[1,2,3]:
grab 3, 3 > 2, insert 3 before 2 --> [1,3,2]

[3,2,1]:
grab 1, 1 < 2, 1 < 3, at end. Return input[::-1]

[1,1,5]:
grab 5, 5 > 1, insert 5 before 1 --> [1,5,1]
'''

'''
[a,b], where b > a; want [b,a]

len([a,b]) / 2 =  1
int(len([a,b,c]) / 2)-1 =  1

a = 0
b = len(nums)-1
c = None

while a < b:
    c = nums[a]

    nums[a] = nums[b]

    nums[b] = c

    a += 1
    b -= 1

[1,2,3,4]:
a = 0
b = 3
c = None

c = 1
nums[0] = 4
nums[3] = 1
|
|---> [4,2,2.5,3,1]
a += 1 --> a = 1
b -= 1 --> b = 2

[2,3,1]

[1,3,2] --> [2,1,3]


'''


class Solution:
    def nextPermutation(self, nums):

        if len(nums) >= 2:

            itr = -1
            term = nums[itr]
            hit = False

            while term != nums[0]:

                for i in range(len(nums)-1+itr, -1, -1):
                    if nums[i] < term:
                        nums.insert(i, term)
                        nums.pop()
                        term = nums[0]
                        hit = True
                        break

                itr -= 1
                term = nums[itr]

            if hit == False:
                a = 0
                b = len(nums)-1
                c = None

                while a < b:
                    c = nums[a]
                    nums[a] = nums[b]
                    nums[b] = c

                    a += 1
                    b -= 1
