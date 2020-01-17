

class Solution:
    def maxSumDivThree(self, nums):
        def getTarget(currentElement):
            tmp =  currentElement//3
            if tmp*3 < currentElement:
                return currentElement - (tmp+1)*3
            elif tmp*3 > currentElement:
                return currentElement - tmp*3



        d = {}
        for i in range(len(nums)):
            try:
                d[nums[i]]

            except:
                d[nums[i]] = 1

        # Now we have all of the elements
        # in the dictionary

        keys = list(d.keys())
        keys.sort(reverse=True)

        ans = []

        i = 0
        while True:

            if i > len(keys)-1:
                break

            currentElement = keys[i]

            if currentElement%3 == 0:
                ans.append(currentElement)
                print("{} is divisible by three".format(currentElement))

            elif currentElement%3 != 0:

                target = getTarget(currentElement)

                print("target for {} is {}".format(currentElement, target))

            # define end condition

            if d[currentElement] == 1:
                del keys[0]

            elif d[currentElement] > 1:
                d[currentElement] -= 1

             # i += 1


        print("Done :)")


if __name__ == '__main__':
    s = Solution()
    s.maxSumDivThree([3,6,5,1,8])
