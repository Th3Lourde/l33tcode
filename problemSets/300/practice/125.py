class Solution:
    def isPalindrome(self, s):
        chrs = set({ "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "1","2","3","4","5","6","7","8","9","0"
        })

        listOfChrs = []

        for idx in range(len(s)):
            if s[idx] in chrs:
                listOfChrs.append(s[idx].lower())

        l = 0
        r = len(listOfChrs)-1

        while l < r:
            if listOfChrs[l] != listOfChrs[r]:
                return False

            l += 1
            r -= 1

        return True

print(Solution().isPalindrome("1P"))
print(Solution().isPalindrome(".#"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
