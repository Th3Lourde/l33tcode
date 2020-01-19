

class Solution:
    def groupThePeople(self, groupSizes):
        '''
        n people
        ids go from 0 --> n-1
        each person belongs in exactly one group
        elements of list tell the group size each person belongs to.
        list is of length n

        Ok. So each id is mapped to one person.
        [3,3,3,3,3,3,1]
        '''

        # Create a dict, key is groupSize, value is list
        # of elements with that groupSize

        d = {}

        for i in range(len(groupSizes)):
            try:
                d[groupSizes[i]].append(i)

            except:
                d[groupSizes[i]] = [i]
                # print(d[groupSizes[i]])


        print(d)

        # Iterate through keys, group appropriately

        keys = list(d.keys())

        ans = []

        for i in range(len(keys)):
            for j in range(int(len(d[keys[i]])/keys[i])):
                ans.append(d[keys[i]][keys[i]*j:keys[i]*(j+1)])







        return ans




if __name__ == '__main__':
    s = Solution()

    # s.groupThePeople([3,3,3,3,3,1,3])
    s.groupThePeople([2,1,3,3,3,2])
