'''
Given string s that only consists of digits

Check if you can split the string into two or
more non-empty substrings such that

the numerical value of the substrings is in descending
order and the numerical difference between two substrings
is one

1) Start with set-up, pick what we start with.
2) See if you can make string less than current

"050043"
^

idx, current string
'''

class Solution:
    def splitString(self, s):
        def itr(inputS, idx):
            # print("itr: {} | {}".format(inputS, s[idx:]))
            if idx >= len(s):
                return True

            for i in range(idx, len(s)):
                # print("inputS:{} | tmp:{}".format(inputS, s[idx:i+1]))
                # print(inputS > s[idx:i+1])
                # print(int(inputS)-int(s[idx:i+1]) == 1)
                if int(inputS) > int(s[idx:i+1]) and int(inputS)-int(s[idx:i+1]) == 1:
                    # print("[hit]: {}".format(s[idx:i+1]))
                    if itr(s[idx:i+1], i+1):
                        return True

            return False

        for i in range(1, len(s)):
            if itr(s[0:i], i) and len(s[0:i]) != len(s):
                return True

        return False

print(Solution().splitString("4771447713"))
print(Solution().splitString("10"))




print(Solution().splitString("10009998"))
print(Solution().splitString("1234"))
print(Solution().splitString("050043"))
print(Solution().splitString("9080701"))
