        result = [[]]
        for nums in nums:
            result += [i + [nums] for i in result]
        return result


Solution().subsets([1,2,3])
