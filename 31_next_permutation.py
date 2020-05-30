
'''
So we are given a list of numbers.
Want to return the next largest permutation.

[1,2,3] --> [1,3,2] | Start with 3; 3 > 2, switch.
[1,3,2] --> (2,3,1) --> [2,1,3] | Start with 2; 2 > 1, switch. Start with 1, 1 < 3, switch.
[2,1,3] --> [2,3,1] | Start with 3; 3 > 1, switch.
[2,3,1] --> (3,2,1) --> [3,1,2] | Start with 1; 1 is the smallest. Start with 3, 3 < 2. Start with 1, 1 < 2, switch.
[3,1,2] --> [3,2,1] | Start with 2, 3 > 2, switch. Start with 3, 3 > 1, switch. Start with 1. Start with 3, 3 > 2, switch.


[3,2,1] is the largest permutation. Return [::-1] via algo magic.

one algorithm to get the next largest permutation.
another algorithm to make sure we have the smallest, largest permutation.



Start with arr[i], if arr[i] > arr[i+n], n < 0, swap arr[i] and arr[i+n].

arr[i] = 2 | arr[i-1] = 1; 2 > 1 || arr[i] > arr[i-1], swap.


We are done when for all i in arr[int], arr[i-1] > arr[i].
[3,2,1]

1:
|
|---> 1 < 2, 1 < 3, go to 2

2:
|
|---> 2 < 3, go to 3

3:
|
|---> At end, break.

Note: return arr[::-1], only we can't actually just return arr[::-1], need to write algo to do
      the swapping :)
'''

# def findLarger(perm):
#     next = list(perm)
#
#     itr = 0
#     z = len(next)-1
#
#     while perm >= next and z > 0:
#         z = len(next)-1-itr
#
#         for i in range(z-1, -1, -1):
#             if next[i] < next[z]:
#                 tmp = next[i]
#                 next[i] = next[z]
#                 next[z] = tmp
#                 break
#
#         itr += 1
#
#     return next
#
# testCases = [
#     [[1,2,3], [1,3,2]],
#     [[1,3,2], [2,3,1]],
#     [[2,1,3], [2,3,1]],
#     [[2,3,1], [3,2,1]],
# ]
#
# # If this passes, then get next larger passes.
# # If findLarger(perm) == perm, call function that returns the [::-1] version.
# # for tc in testCases:
# #     assert findLarger(tc[0]) == tc[1], "[For {}] {} != {}".format(tc[0], findLarger(tc[0]), tc[1])
#
# def refine(perm, next):
#     valid = list(next)
#     smaller = list(valid)
#     itr = 0
#     z = len(smaller) - 1
#
#     while smaller > perm:
#         z = len(smaller) - 1 - itr
#
#         for i in range(z-1, -1, -1):
#             if smaller[i] > smaller[z]:
#                 tmp = smaller[i]
#                 smaller[i] = smaller[z]
#                 smaller[z] = tmp
#                 break
#
#         if smaller > perm and smaller < next:
#             valid = list(smaller)
#             itr += 1
#
#         else:
#             break
#
#
#     return valid
#
# testCases = [
#     [[1,3,2], [2,3,1], [2,1,3]],
#     [[2,3,1], [3,2,1], [3,1,2]],
# ]
#
# for tc in testCases:
#     assert refine(tc[0], tc[1]) == tc[2], "{} != {}".format(refine(tc[0], tc[1]), tc[2])








# [1,2,3] --> [1,3,2]
# [1,3,2] --> (2,3,1)
# [2,1,3] --> [2,3,1]
# [2,3,1] --> (3,2,1)
# [3,1,2] --> (2,1,3)

class Solution:

    def nextPermutation(self, nums):
        # Looking for index i s.t. nums[i] < nums[i] + 1

        if len(nums) < 2:
            return 0

        current = 0

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]  :
                current = i
                break

        if current == 0 and nums[0] > nums[1]:
            a = 0
            b = len(nums)-1
            c = None

            while a < b:
                c = nums[a]
                nums[a] = nums[b]
                nums[b] = c

                a += 1
                b -= 1

        elif (current == 0 and nums[0] < nums[1]) or (current != 0):
            greater = None

            for i in range(current+1, len(nums)):
                if nums[current] < nums[i]:
                    if greater == None:
                        greater = i

                    elif greater:
                        if nums[i] <= nums[greater]:
                            greater = i

            tmp = nums[current]
            nums[current] = nums[greater]
            nums[greater] = tmp

            # print(nums)

            # Last step, reverse nums[current:len(nums)]
            a = current+1
            b = len(nums)-1
            c = None

            while a < b:
                c = nums[a]
                nums[a] = nums[b]
                nums[b] = c

                a += 1
                b -= 1








    # Might not fulfill modify in-place requirement b/c we create new arrays.
    # Also wrong, good attempt though
    def nextPermutation_2(self, nums):

        def findLarger(perm):
            next = list(perm)

            itr = 0
            z = len(next)-1

            while perm >= next and z > 0:
                z = len(next)-1-itr

                for i in range(z-1, -1, -1):
                    if next[i] < next[z]:
                        tmp = next[i]
                        next[i] = next[z]
                        next[z] = tmp
                        break

                itr += 1

            return next

        def refine(perm, next):
            valid = list(next)
            smaller = list(valid)
            itr = 0
            z = len(smaller) - 1

            while smaller > perm:
                z = len(smaller) - 1 - itr

                for i in range(z-1, -1, -1):
                    # print("i: {} smaller[i]: {}".format(i, smaller[i]))
                    if smaller[i] > smaller[z]:
                        tmp = smaller[i]
                        smaller[i] = smaller[z]
                        smaller[z] = tmp
                        itr = 0
                        break

                print("[smaller]: {}".format(smaller))

                if valid == smaller:
                    itr += 1

                if smaller > perm and smaller < next:
                    valid = list(smaller)

                else:
                    break

            return valid

        next = findLarger(nums)

        if next == nums:
            a = 0
            b = len(nums)-1
            c = None

            while a < b:
                c = nums[a]
                nums[a] = nums[b]
                nums[b] = c

                a += 1
                b -= 1

        elif next != nums:
            nums = refine(nums, next)



if __name__ == '__main__':
    s = Solution()

    testCases = [
        [[1,2,3], [1,3,2]],
        [[1,3,2], [2,1,3]],
        [[2,1,3], [2,3,1]],
        [[2,3,1], [3,1,2]],
        [[3,1,2], [3,2,1]],
        [[3,2,1], [1,2,3]],
        [[5,4,7,5,3,2], [5,5,2,3,4,7]],
        [[0], [0]],
        [[1,2], [2,1]],
        [[2,3,1,3,3], [2,3,3,1,3]],
    ]

    for tc in testCases:
        inp = list(tc[0])
        s.nextPermutation(tc[0])
        assert tc[0] == tc[1], "[for: {}]{} != {}".format(inp, tc[0], tc[1])


# [1,2,3] --> [1,3,2] | Start with 3; 3 > 2, switch.
# [1,3,2] --> (2,3,1) --> [2,1,3] | Start with 2; 2 > 1, switch. Start with 1, 1 < 3, switch.
# [2,1,3] --> [2,3,1] | Start with 3; 3 > 1, switch.
# [2,3,1] --> (3,2,1) --> [3,1,2] | Start with 1; 1 is the smallest. Start with 3, 3 < 2. Start with 1, 1 < 2, switch.
# [3,1,2] --> [3,2,1] | Start with 2, 3 > 2, switch. Start with 3, 3 > 1, switch. Start with 1. Start with 3, 3 > 2, switch.





















    # def nextPermutation_1(self, nums):
    #
    #     if len(nums) >= 2:
    #
    #         itr = -1
    #         term = nums[itr]
    #         hit = False
    #
    #         while term != nums[0]:
    #
    #             for i in range(len(nums)-1+itr, -1, -1):
    #                 if nums[i] < term:
    #                     nums.insert(i, term)
    #                     nums.pop()
    #                     term = nums[0]
    #                     hit = True
    #                     break
    #
    #             itr -= 1
    #             term = nums[itr]
    #
    #         if hit == False:
    #             a = 0
    #             b = len(nums)-1
    #             c = None
    #
    #             while a < b:
    #                 c = nums[a]
    #                 nums[a] = nums[b]
    #                 nums[b] = c
    #
    #                 a += 1
    #                 b -= 1
