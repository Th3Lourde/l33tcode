


class Solution:
    def topKFrequent(self, nums, k):
        # 1) Create dict
        sD = {} # standard dictionary

        for i in range(len(nums)):
            try:
                sD[nums[i]] += 1
            except:
                sD[nums[i]] = 1

        rD = {} # reverse dictionary
        for key in sD.keys():
            try:
                rD[sD[key]].append(key)
            except:
                rD[sD[key]] = [key]


        print(sD)
        print(rD)

        # print(list(sD.values()))

        import heapq

        heapq.heapify(list(rD.keys()))

        top_k = heapq.nlargest(k, list(rD.keys()))

        ans = []
        t = 0
        while t < k:
            for element in top_k:
                for hit in rD[element]:
                    ans.append(hit)
                    t += 1
                    if t == k:
                        return ans




if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([3,2,1,2,3,4,5,6,6,5,4,5,6,7,8,9,8,7,6,5,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,2,3,4,5,6,8], 5))
