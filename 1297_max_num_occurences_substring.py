

class Solution:
    '''
    Given a string s, return the maximum number of ocurrences of any substring under the following rules:
     - The number of unique characters in the substring must be less than or equal to maxLetters.
     - The substring size must be between minSize and maxSize inclusive.

     We can just look for the maximum ocurrences of any substring of minSize.
     For all strings of size maxSize, there exists a substring with at least
     an equal number of occurences

     find all unique substrings of size minSize that have the proper number of uniue characters
     for every substring of minSize, find it's frequency




    '''
    # Time limit exceeded. So it works but isn't fast enough
    # 37/40, come back to later
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        # 1) Find all substrings of minSize
        # that have the correct number of unique characters
        def getUniqueChars(str):
            unique = 0
            while len(str) != 0:
                str = str.replace(str[0], "")
                unique += 1

            return unique

        subFreq = {}
        # Find all substrings of min size with
        # valid num characters
        for i in range(len(s)-minSize+1):
            subStr = s[i:i+minSize]

            try:
                subFreq[subStr] += 1

            except:
                if getUniqueChars(subStr) <= maxLetters:
                    subFreq[subStr] = 1

        if subFreq == {}:
            return 0

        elif subFreq != {}:
            return max(subFreq.values())



if __name__ == '__main__':
    s = Solution()

    # print(s.maxFreq("aababcaab", 2, 3, 4))
    print(s.maxFreq("aababcaab", 2, 3, 4))
