
'''
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Ok so we are given that the majority element always exists in the array

It is also true that the majority element happens the most amount of times
in the array. This means that we can simply just figure out which element
occurs the most and then return that.

loop through the list
keep a dictionary that keeps track of occurrences
after we are past n/2 elements, start checking the value of
the elements in the dictionary. Return the element with the
highest occurrence.
'''


class Solution:

    # faster than 5%
    # less memory than 100%
    def majorityElement_1(self, nums):
        d = {}

        max = nums[0]

        elem = int(len(nums)/2)

        for i in range(len(nums)):
            try:
                d[nums[i]] += 1

                if i > elem:
                    if d[max] < d[nums[i]]:
                        max = nums[i]

                    if d[nums[i]] > len(nums)/2:
                        return nums[i]

            except:
                d[nums[i]] = 1

        return max


    # get all of the unique elements in the list
    # make a copy of the list, cast as string
    # for every unique element in the list, remove
    # it from the string-copy, if the length is below
    # a certain threshold, return the element.
    # else: make another copy and move on to the
    # next element

    '''
    This may not be faster because this requires us
    to loop through the entire list in order to cast
    it as a string. Is casting a cariable from 1 datatype
    to another an isomorphism? It might be. Very cool :D
    '''
    def majorityElement(self, nums):
        unique = list(set(nums))

        list1 = [1, 2, 3]
        str1 = ''.join(str(e) for e in list1)

        for i in range(len(unique)):
            cpy = ''.join(nums)
            print(cpy)


            cpy = cpy.replace(str(unique[i]), "")
            print(cpy)
            if len(cpy) < len(nums)/2:
                return unique[i]



if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))
