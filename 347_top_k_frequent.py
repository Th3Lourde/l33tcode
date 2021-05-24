class Solution:
    def topKFrequent_1(self, nums, k):
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


    def topKFrequent(self, nums, K):
        d = {}

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        arr = []

        while d:
            dels = []
            for k in d:
                arr.append((k, d[k]))
                d[k] -= 1

                if d[k] == 0:
                    dels.append(k)

            for keyToDel in dels:
                del d[keyToDel]

        seen = set()
        k_most_freq = []

        # print(arr)

        for i in range(len(arr)-1, -1, -1):
            if arr[i][0] not in seen:
                k_most_freq.append(arr[i][0])
                seen.add(arr[i][0])

            if len(k_most_freq) == K:
                break

        # print(seen)

        return k_most_freq



s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))
print(s.topKFrequent([3,2,1,2,3,4,5,6,6,5,4,5,6,7,8,9,8,7,6,5,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,2,3,4,5,6,8], 5))
