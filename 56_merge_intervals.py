class Solution:
    def merge_1(self, intervals):
        d = {}

        if len(intervals) == 0:
            return []

        for i in range(len(intervals)):
            try:
                if d[intervals[i][0]] < intervals[i][1]:
                    d[intervals[i][0]] = intervals[i][1]

            except:
                d[intervals[i][0]] = intervals[i][1]

        # print("d: {}".format(d))

        keys = list(d.keys())
        keys.sort()

        tmp = []

        z = 0

        while z <= len(keys)-1:

            if z < len(keys)-1:

                if d[keys[z]] < keys[z+1]:
                    tmp.append([keys[z], d[keys[z]]])

                elif d[keys[z]] >= d[keys[z+1]]:
                    keys[z+1] = keys[z]

                elif d[keys[z]] >= keys[z+1] and d[keys[z]] < d[keys[z+1]]:
                    d[keys[z]] = d[keys[z+1]]
                    keys[z+1] = keys[z]

            else:
                tmp.append([keys[z], d[keys[z]]])

            z += 1

        return tmp

    def merge_2(self, intervals):
        intervals.sort(key=lambda x: x[0])
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        idx = 1

        while idx < len(intervals):
            if intervals[idx][0] <= end:
                if intervals[idx][1] > end:
                    end = intervals[idx][1]
            else:
                ans.append([start, end])
                start = intervals[idx][0]
                end = intervals[idx][1]

            idx += 1


        ans.append([start, end])

        return ans

    def merge(self, intervals):
        merged_intervals = []

        if not intervals:
            return merged_intervals

        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if start <= intervals[i][0] <= end:
                end = max(end, intervals[i][1])

            else:
                merged_intervals.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        merged_intervals.append([start, end])

        return merged_intervals

s = Solution()

testCases = [
    [[[1,2]], [[1,2]]],
    [[[1,4],[4,5]], [[1,5]]],
    [[[1,4],[2,3]], [[1,4]]],
    [[[2,3],[4,5],[6,7],[8,9],[1,10]], [[1,10]]],
    [[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]],[[1,10]]],
    [[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10], [1,10]],[[1,10]]],
    [[[1,2],[2,3],[3,4],[4,7],[5,6],[6,7],[7,8],[8,9],[9,10] ],[[1,10]]],
    [[[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]],
]

passed = True
z = 1

for testCase in testCases:
    resp = s.merge(testCase[0])

    if resp != testCase[1]:
        passed = False
        print("[failed test case {}] wanted {} got {}".format(z, testCase[1], resp))
        break

    z += 1

if passed:
    print("[passed all test cases] :)")
