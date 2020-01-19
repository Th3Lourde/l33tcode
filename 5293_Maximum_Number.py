

class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        '''
        Given a string, find the maximum occurrences of a substring with the following properties:
            * The number of unique characters in the substring must be less than or equal to maxLetters
            * The substring size must be \in [minSize, maxSize]

            Ok so we are looking for a substring of size \in [minSize, maxSize]

        '''

        size = minSize
        ans = 0

        seen = {}

        i = 0

        # find all occurrences of substring size substring
        # what if we define what are valid substrings and invalid substrings
        # and then count them conditionally, then return the max count?

        # We only need to worry about minSize, if our string is:
        # "abcabc"
        # and minSize == 2
        # and maxSize == 3
        # ab occurs twice
        # abc occurs twice
        # this is true for both things

        while (i < len(s)-size):

            substring = s[i:i+size+1]

            print("substring: {}".format(substring))

            # make sure we haven't seen the substring already
            try:
                seen[substring]
                i += 1

            except:
                seen[substring] = 1

                # 1) check the number of unique characters in substring
                cpy = substring
                chars = len(substring)

                unique = 0

                passes_u = True

                # does is pass the unique
                while True:
                    if unique > maxLetters:
                        passes_u = False
                        break

                    elif len(cpy) > 0:
                        print("char: {}".format(cpy[0]))
                        cpy = cpy.replace(cpy[0], "")
                        unique += 1

                    elif cpy == "":
                        break

                occurence = 0

                if passes_u:
                    print("hi")
                    # count the number of occurrences of the substring
                    for i in range(i, len(s)-size, size):
                        if s[i:i+size]:
                            occurence += 1

                    if occurence > ans:
                        ans = occurence
                    i += 1

                elif not passes_u:
                    i += 1



        print("ans: {}".format(ans))

if __name__ == '__main__':
    z = Solution()

    s = "aabcabcab"
    maxLetters = 2
    minSize = 2
    maxSize = 3

    z.maxFreq(s, maxLetters, minSize, maxSize)
