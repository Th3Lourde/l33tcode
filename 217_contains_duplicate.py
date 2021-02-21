
class Solution:
    def containsDuplicate(self, nums):
        s = set()

        for n in nums:
            if n in s:
                return True
            s.add(n)

        return False

if __name__ == '__main__':
    s = Solution()

    print(s.containsDuplicate([1,2,3,1]))
    print(s.containsDuplicate([1,2,3,4]))
    print(s.containsDuplicate([1,2,3,4,1]))
