

'''
given array nums
write a function to move
all of the zeros in the array
to the end of the array, while
maintaining the relative order
of the elements in the array

we could count the number of zeroes
that we encounter when looping through
the array, deleting them as we see
them, then appending them to the array
after we have deleted all of the zeroes

Iterate through the list via while loop


'''
class Solution:
    def moveZeroes(self, nums):
        zeroes = 0
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] == 0:
                del nums[i]
                zeroes += 1
                l = len(nums)

            elif nums[i] != 0:
                i += 1


        add = [0]*zeroes

        return nums + add



if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([1,2,3]))
