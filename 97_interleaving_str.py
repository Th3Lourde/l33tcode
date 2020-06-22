
'''
("aabcc","dbbca","aadbbcbcac")

s3: "aadbbcbcac"
            ^
s1: "aabcc"
i        ^
s2: "dbbca"
j       ^


1 1 2 1 2 1 2 1
            &

Ok, so the issue is that which
character we use matters. I feel
like this is turning into a dp problem

Yea this is dp.
I am not doing dp. So we are
skipping this problem :/
'''


class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        i = 0
        j = 0

        for char in s3:
            if i < len(s1) and s1[i] == char:
                print("i: {} s1[i]: {}".format(i, s1[i]))
                i += 1

            elif j < len(s2) and s2[j] == char:
                print("j: {} s2[j]: {}".format(j, s2[j]))
                j += 1

            else:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isInterleave("aabcc","dbbca","aadbbcbcac"))
