
'''
Plan:
1) Identify the break
2) Find the min/max elements in the break
3) Identify the subbarray that will allow
   the max/min elements to be in order
4) return the length of said subbarray
5) Profit
'''

# Doesn't work, come back later
class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        '''
        Ok so let's do this 'better' and try to make it
        more efficient with less code
        '''

        # 1) Identify the break
        '''
        Here we are identifying the subarray that,
        if removed, would result in nums being sorted
        It must exist.
        '''


        # break_s, break_e, are indices
        break_s = 0
        found_s = False
        break_e = len(nums)-1
        found_e = False

        while (break_s < break_e) and (not found_s or not found_e):
            if nums[break_s] > nums[break_s+1]:
                found_s = True
                break_s = break_s + 1

            if not found_s:
                break_s += 1

            if nums[break_e] < nums[break_e-1]:
                found_e = True
                break_e = break_e - 1

            if not found_e:
                break_e -= 1

        if not(found_s) and not(found_e):
            return 0


        print("Input: {}".format(nums))
        print("Break: {}".format(nums[break_s:break_e+1]))













    def findUnsortedSubarray_1(self, nums) -> int:
        print("Input: {}".format(nums))

        '''
        Step 1: Identify the break
        After this step is complete
        we should know the subbarray
        that contains all elements
        that are out of place
        '''

        start = -1
        start_i = 0
        end = -1
        end_i = len(nums)-1

        while (start_i < end_i) and (start == -1 or end == -1):
            if nums[start_i] > nums[start_i+1] and start == -1:
                start = start_i

            if nums[end_i] < nums[end_i-1] and end == -1:
                end = end_i

            if start == -1:
                start_i += 1

            if end == -1:
                end_i -= 1


        if start == -1 and end == -1:
            # There are no elements out of
            # place, thus return 0
            return 0

        else:
            '''
            2) Find the max and min elements
            in the break
            '''

            break_min = None
            break_max = None

            for j in range(start, end+1, 1):
                if break_min == None:
                    # break_min = nums[j]
                    break_min = j

                elif nums[break_min] > nums[j]:
                    # break_min = nums[j]
                    break_min = j

                if break_max == None:
                    # break_max = nums[j]
                    break_max = j

                elif nums[break_max] < nums[j]:
                    # break_max = nums[j]
                    break_max = j

                # print("[break_min, break_max]: [{},{}]".format(break_min, break_max))

            # Have the min/max of break, execute 3)
            '''
            3) Identify the subarray that will allow
            us to put break_min, break_max in the proper
            place
            '''
            print("[break_min, break_max]: [{},{}]".format(break_min, break_max))

            if break_max != break_min:
                ans_start = 0
                ans_end = len(nums)-1
                found_max = False
                found_min = False

                # While we have not found the subarray:
                while found_max == False or found_min == False:
                    # Either we find and element < min that is next to an element > min
                    # Or we find an element < min that is next to the begining of the break

                    if found_min == False:

                        if (ans_start == 0 and nums[0] > nums[break_min]):
                            found_min = True
                            ans_start = ans_start
                            print("found_min == True: nums[{}]".format(ans_start))

                        elif ans_start == 0 and nums[ans_start+1] >= nums[break_min]:
                            found_min = True
                            ans_start = ans_start+1
                            print("found_min == True: nums[{}]".format(ans_start))


                        elif (nums[ans_start] < break_min and nums[ans_start+1] >= nums[break_min]) or (nums[ans_start] < break_min and ans_start+1 == start_i):
                            # print(start_i)


                            # We have found where to start the final subarray
                            found_min = True
                            # ans_start = ans_start+1
                            ans_start = ans_start+1
                            print("found_min == True: nums[{}]".format(ans_start))


                    if found_max == False:

                        if (found_max == False) and (ans_end == len(nums)-1 and nums[break_max] > nums[ans_end]):
                            found_max = True
                            ans_end = len(nums)-1
                            print("found_max == True: nums[{}]".format(ans_end))

                        elif ans_end == len(nums)-1 and nums[ans_end-1] < nums[break_max]:
                            # print("hi")
                            found_max = True
                            ans_end = len(nums)-2
                            print("found_max == True: nums[{}]".format(ans_end))

                        elif nums[ans_end] >= nums[break_max] and ans_end-1 == end_i:
                            found_max = True
                            ans_end = ans_end-1
                            print("found_max == True: nums[{}]".format(ans_end))

                        elif nums[ans_end] >= nums[break_max] and nums[ans_end-1] < nums[break_max]:
                            found_max = True
                            ans_end = ans_end-1
                            print("found_max == True: nums[{}]".format(ans_end))


                            # Same logic only with break_max
                        # else:
                        #     print("Input: {}".format(nums))
                        #     print("ans_end: {}".format(ans_end))
                        #     print("break_max: {}".format(break_max))
                        #     (nums[ans_end] > nums[break_max] and nums[ans_end-1] <= nums[break_max])
                        #     print("1")
                        #     (nums[ans_end] > nums[break_max] and ans_end-1 == end_i)
                        #     print("2")



                        # elif (nums[ans_end] > nums[break_max] and nums[ans_end-1] <= nums[break_max]) or (nums[ans_end] > nums[break_max] and ans_end-1 == end_i):
                        #     # We have found where to end the final subarray
                        #     found_max = True
                        #     ans_end = ans_end-1
                        #     print("found_max == True: nums[{}]".format(ans_end))


                    if not found_min:
                        ans_start += 1

                    if not found_max:
                        ans_end -= 1


                # We have now found the subarray needed in order to sort all
                # of the elements in our break

                # It could be the case that the max in our subarray
                # is the max in nums. Since we are covering the entire
                # array nums, we will just get the max back too us.
                # This is also true when we find the min subarray.



                # Length of the subarray includes the endpoints, so
                # end-start+1

                return ans_end-ans_start+1




if __name__ == '__main__':
    s = Solution()

    # print(s.findUnsortedSubarray([1,3,2,4]))

    print(s.findUnsortedSubarray([1,3,2,2,4]))
    # print(s.findUnsortedSubarray([1,3,2,2,4]))
    # print(s.findUnsortedSubarray([1,3,2,2,2]))
    # print(s.findUnsortedSubarray([1,3,5,7,6,2,8,9]))
    # print(s.findUnsortedSubarray([3,5,7,6,2,8,9]))
    # print(s.findUnsortedSubarray([3,5,7,6,2]))


    # print(s.findUnsortedSubarray([1,3,2,3,3]))
    # print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
    # print(s.findUnsortedSubarray([0,1,4,5,3,7,2,6,8,9]))
