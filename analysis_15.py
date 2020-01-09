class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # Sort the list initially
        N, result = len(nums), [] # N == number of elements, result == ans, thing to return
        for i in range(N): # For every number

            if i > 0 and nums[i] == nums[i-1]:
                # if we are at a duplicate, continue
                # continue will just increase i, skip rest of code
                continue

            target = nums[i]*-1 # We are looking for two terms who sum
                                # is the negative representation of this
                                # number (target = nums[i]*1)

            '''
            Thus, we are looking for two terms
            that sum to target.
            The list is sorted, so if the elements
            exist, they are >i and < len(nums)

            i+1 to put the left goalpost in place
            N-1 to put the right goalpost in place
            '''

            s,e = i+1, N-1

            while s<e: # While our goalposts don't overlap:
                if nums[s]+nums[e] == target: # If we have found a trio:
                    result.append([nums[i], nums[s], nums[e]]) # Add the trio to our ans
                    s = s+1 # move the left goalpost

                    while s<e and nums[s] == nums[s-1]: # while goalposts are valid and we have repeats, move left goalpost right
                    # '''
                    # The idea here is to ensure that if there is a string of repeated terms, that we only use the 'last'
                    # character in that string. Thus ensuring ...
                    # '''
                        s = s+1

                elif nums[s] + nums[e] < target: # If we are low, move left goalpost
                                                 # This works because the list is sorted. Since the list is sorted
                                                 # The only way to decrease our 2sum is to move the right goalpost
                                                 # left.
                    s = s+1

                else: # If we are high, move right goalpost
                      # Works for a similar reason. This is where the use of the
                      # initial while statement comes into play. Once the left goal-
                      # post is ahead of the right goalpost, we can stop b/c we know
                      # that there can no-longer exist a solution
                    e = e-1
        return result


if __name__ == '__main__':
    s = Solution()

    print(s.threeSum([1,0,0,0]))
