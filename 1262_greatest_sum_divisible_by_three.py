
'''
Still working on problem
'''

class Solution:
    def maxSumDivThree(self, nums):
        def getTarget(currentElement):
            tmp =  currentElement//3
            if tmp*3 < currentElement:
                return (tmp+1)*3 - currentElement
            elif tmp*3 > currentElement:
                return tmp*3 - currentElement


        def constructTarget(target, keys, d):
            '''
            So keys are already sorted in descending order
            search for the largest element < target


            '''



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
            newSum = []

            if i > len(keys)-1:
                break

            currentElement = keys[i]

            if currentElement%3 == 0:
                # ans.append(currentElement)
                newSum.append(currentElement)
                print("{} is divisible by three".format(currentElement))

            elif currentElement%3 != 0:

                target = getTarget(currentElement)

                # maybe update dictionary about currentElement here?
                print("target for {} is {}".format(currentElement, target))

                if target == 1:
                    try:
                        if d[1] > 0:
                            newSum.append(1)
                            # update frequency of 1

                    except:
                        print("target does not exist in dict")

                elif target > 1:
                    # try to construct target using keys
                    constructTarget(target, keys, d)

            # define end condition

            if d[currentElement] == 1:
                del keys[0]

            elif d[currentElement] > 1:
                d[currentElement] -= 1

             # i += 1


        print("Done :)")

        ans += newSum


if __name__ == '__main__':
    s = Solution()
    s.maxSumDivThree([3,6,5,1,8])
