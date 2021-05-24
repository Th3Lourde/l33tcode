class Solution:
    def isPalindrome_2(self, s):

        if s.strip() == "":
            return True

        i1 = 0
        i2 = len(s)-1

        one = False
        two = False

        while i1 <= i2:
            p1 = s[i1]
            p2 = s[i2]

            # Find a valid p1
            uni = ord(p1)

            if (uni >= 48) and (uni <= 57) or (uni >= 97) and (uni <= 122):
                one = True

            # if capital, change to lowercase
            elif (uni >= 65) and (uni <= 90):
                # Change to lowercase
                p1 = p1.lower()
                one = True

            else:
                one = False
                i1 += 1

            # Find a valid p2
            uni = ord(p2)

            if (uni >= 48) and (uni <= 57) or (uni >= 97) and (uni <= 122):
                two = True

            # if capital, change to lowercase
            elif (uni >= 65) and (uni <= 90):
                # Change to lowercase
                p2 = p2.lower()
                two = True

            else:
                two = False
                i2 -= 1

            # By this point, we should have a valid
            # p1 and p2. If so, time to check to
            # see if they are the same character

            if one and two:
                if p1 == p2:
                    print("p1: {} p2: {}".format(p1, p2))
                    i1 += 1
                    i2 -= 1
                elif p1 != p2:
                    return False


        # if not(one and two):
        #     return False
        # elif (one and two):
        #     return True
        return True


    def isPalindrome_1(self, s):
        tmp = list(s)

        '''
        We must remove the non-alphanumeric characters
        before we will be able to check to see if the
        string is or is not a palindrome.
        '''

        # 1) Remove non-alphanumeric

        i = 0
        while i < len(tmp):


            # Check is tmp[i] is in
            # the valid alphanumeric range
            # if so, continue.
            # if not, remove it from the list

            # ord() <-- get unicode val
            uni = ord(tmp[i])

            # print("{} --> {}".format(tmp[i], uni))


            # if in [0,9], continue
            if (uni >= 17) and (uni <= 26):
                i += 1

            # if capital, change to lowercase
            elif (uni >= 65) and (uni <= 90):
                # Change to lowercase
                tmp[i] = tmp[i].lower()
                i += 1

            # if lowercase, continue
            elif (uni >= 97) and (uni <= 122):
                i += 1

            else:
                tmp.remove(tmp[i])


        # By this time, hope that we have a string
        # that is only composed of alpha-numeric
        # characters.

        tmp = "".join(tmp)

        # print(tmp)

        # Palindrome algorithm:

        if len(tmp)%2 == 0:
            # Even
            # for i in range((len(tmp)/2) - 1):

            # -1 is where we want to stop at, range
            # ends before the value that we want to
            # stop at.
            for i in range(int((len(tmp)/2))):
                if tmp[i] != tmp[len(tmp)-i-1]:
                    return False

        elif len(tmp)%2 == 1:
            # Odd
            for i in range(int((len(tmp)-1)/2)):
                if tmp[i] != tmp[len(tmp)-i-1]:
                    return False


        return True


    def isPalindrome(self, s):
        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

s = Solution()

t1 = "A man, a plan, a canal: Panama"
t1 = "tacocat"

print(s.isPalindrome(t1))

t2 = "race a car"
print(s.isPalindrome(t2))

t3 = "0P"
print(s.isPalindrome(t3))
