


class Solution:
    def checkIfExist(self, arr):
        d = {}

        for i in range(len(arr)):
            try:
                d[arr[i]] += 1
            except:
                d[arr[i]] = 1


        keys = list(d.keys())

        for key in keys:
            try:
                if (d[key*2]):
                    if (key*2 == 0) and (d[0] >= 2):
                        return True

                    elif (key*2 != 0):
                        return True

            except: continue

        return False



if __name__ == '__main__':
    s = Solution()
    print(s.checkIfExist([7,1,14,11]))
    print(s.checkIfExist([3,1,7,11]))
    print(s.checkIfExist([]))

    print(s.checkIfExist([-2,0,10,-19,4,6,-8]))
    print(s.checkIfExist([0,0]))
