'''
n bulbs, numbered 1-n

bulb can either be off, yellow, blue
no requirement for off, yellow
can be blue iff, it is yellow and all previous bulbs are yellow

given a list of numbers that represent turning bulbs
on or off, return the number of times all lights that are on are blue
return the momment where this is true.

Start counting bulbs at 1.
Start counting momments at 0.

naive is to have two for loops, checking if lights are on.
Do that first.


'''

class Solution:


    def numTimesAllBlue(self, light):
        maxB = light[0]
        s = 0
        ans = 0

        for bulb in light:
            maxB = max(maxB, bulb)

            s += bulb

            if bulb == 1 and s == 1:
                ans += 1

            elif bulb >= 1 and ((maxB)*(maxB+1))/2 == s:
                ans += 1

        return ans














    def numTimesAllBlue4(self, light):
        d = [0*len(light)]
        maxB = 1
        ans = 1

        for bulb in light:

            d[bulb-1] = 1

            maxB = max(maxB, bulb)


            try:
                if sum(d[:bulb]) == ((bulb)*(bulb-1)/2) or sum(d[:maxB]) == ((maxB)*(maxB-1)/2):
                    ans += 1

            except:
                if sum(d[:maxB]) == ((maxB)*(maxB-1)/2):
                    ans += 1

        return ans


    def numTimesAllBlue1(self, light):
        n = 0
        a = 0
        maxB = 0

        for bulb in light:

            maxB = max(maxB, bulb)

            n += bulb
            if n == ((bulb*(bulb-1))/2):
                a += 1

        return a




    def numTimesAllBlue2(self, light):
        n = len(light)
        num_on = 0
        ans = []
        z = 0
        tmp = 0

        d = {}
        for i in range(1, n+1):
            d[i] = False

        for bulb in light:
            # print("bulb: {}".format(bulb))
            tmp += bulb

            if d[bulb]:
                d[bulb] = False
                num_on -= 1
                # print("Turn off")

            elif not d[bulb]:
                d[bulb] = True
                num_on += 1
                # print("Turn on")

            # Check for blue lights
            if num_on >= bulb:
                # print("Searching: {}".format(d))
                find = True
                for j in range(1, num_on+1):
                    if not d[j]:
                        # print("{} is off".format(j))
                        find = False
                        break

                # If it gets through this, it passes
                if find:
                    ans.append(z)

            z += 1

        return len(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.numTimesAllBlue([2,1,4,3,6,5]))
