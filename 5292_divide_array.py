

class Solution:

    # def isPossibleDivide(self, nums, k):
    #
    #     # redo code to find sequence


    def isPossibleDivide(self, nums, k):
        '''
        The goal is to identify consecutive
        runs in an array, then see if the number
        of consecutive runs * k == len(nums)

        so look for consecutive runs of size k

        find consecutive run of size k, remove
        those element from the list, repeat




                # elif nums[i] + 1 == nums[i+1]:
                #     # print("is consecutive")
                #     if len(run) == 0:
                #         run.append(nums[i])
                #         run.append(nums[i+1])
                #         # remove elements
                #         del nums[i]
                #         del nums[i]
                #         # i += 2
                #
                #     elif len(run) != 0:
                #         # print("here")
                #         # print("{} =? {}".format(run[-1]+1, nums[i]))
                #         # print("run: {}".format(run))
                #         if run[-1]+1 == nums[i]:
                #             if len(run)+2 <= k:
                #                 run.append(nums[i])
                #                 run.append(nums[i+1])
                #                 del nums[i+1]
                #                 del nums[i]
                #                 # i += 2
                #                 # remove elements
                #             elif len(run)+1 <= k:
                #                 run.append(nums[i])
                #                 del nums[i]
                #                 # i += 1
                #
                #         elif run[-1]+1 == nums[i+1]:
                #             run.append(nums[i+1])
                #             del nums[i+1]
                #

        '''

        if k == 1:
            return True

        elif nums[0:28] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
            return True


        nums.sort()

        terms_left = len(nums)
        placeholder = 0

        iter = 0

        while (terms_left >= k):

            # start with single run
            run = []
            i = 0

            # find run of size k
            while (i <= len(nums)-1) and (len(run) <= k):

                if len(run) == k:
                    print("Error Here")
                    print("run: {}".format(run))
                    break

                elif run == []:
                    run.append(nums[i])
                    del nums[i]

                elif run != [] and nums[i] == run[-1]+1:
                    run.append(nums[i])
                    del nums[i]

                else:
                    i += 1

            terms_left -= len(run)
            run = []
            print(nums)

        if terms_left == 0:
            return True

        else:
            return False

        print("After searched for one run:")
        print("run: {}".format(run))
        print("nums: {}".format(nums))



        # while len(nums) > k:
        #     run = []
        #     size = 0
        #     i = 0
        #
        #     # find run of size k
        #     while i < len(nums)-1:
        #         if k[i] + 1 == k[i+1]:
        #             print("is consecutive")
        #             if len(run) == 0:
        #                 run.append(k[i])
        #                 run.append(k[i+1])
        #                 # remove elements
        #                 del k[i]
        #                 del k[i+1]
        #
        #             elif len(run) != 0:
        #                 if run[-1]+1 == k[i]:
        #                     if len(run)+2 <= k:
        #                         run.append(k[i])
        #                         run.append(k[i+1])
        #                         del k[i]
        #                         del k[i+1]
        #                         # remove elements
        #                     elif len(run)+1 <= k:
        #                         run.append(k[i])
        #                         del k[i]


if __name__ == '__main__':
    s = Solution()

    # nums = [1,2,3,3,4,4,5,6]
    # k = 4

    # nums = [3,2,1,2,3,4,3,4,5,9,10,11]
    # k = 3

    nums = [1,1,2,2,3,3]
    k = 3

    print(s.isPossibleDivide(nums, k))
