'''
Given List[List[int]]
First number represents height
Second number represents # people > greater height on front of them
'''


class Solution:
    def reconstructQueue(self, people):
        import heapq

        d = {}

        for person in people:
            try:
                d[person[0]].append(person)

            except:
                d[person[0]] = [person]

        keys = list(d.keys())

        for key in keys:
            li = d[key]
            li.sort(key = lambda x: x[1] )

        keys.sort()

        ans = []

        for key in reversed(keys):
            for element in d[key]:
                ans.insert(element[1], element)

        return ans










        # ans = []
        # for element in reversed(people):
        #     ans.insert(element[1], element)



        # ans = []
        # for element in tmp:
        #     for val in element:
        #         ans.insert(val[1], val)
        #
        #
        # print(ans)




if __name__ == '__main__':
    s = Solution()
    s.reconstructQueue([[7,1], [4,4], [7,0], [5,0], [6,1], [5,2]])
