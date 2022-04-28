'''
chrTest:
if s contains character not in set({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ".", "+", "-", "e", "E", })
return False

frequencyTest:
if s contains character with count > 1 for set({"e", "E", "."})
if s contains character with count > 2 for set({"+", "-"})

Character specific tests:

Cannot be a decimal on the rhs of e/E:
There can only be digits on the rhs of e/E.

+,-:
+,- either has an index 0
or it is next to an e/E. Where the element to the left is an e
for +,-, i-1 in {e, E}

e,E:
there cannot be both an "e" and an "E"
lhs of e,E element to the left must be a number
rhs of e,E must be a number or a +/-, two to the right (if existent, must be a number)

--------------------- --------------------- --------------------- --------------------- ---------------------
'''

class Solution:
    def isNumber(self, s):
        validChrs = set({ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", ".", "e", "E"})

        freqDict = {
            "+":[],
            "-":[],
            ".":[],
            "e":[],
            "E":[],
        }

        for idx, chr in enumerate(s):
            if chr not in validChrs:
                return False

            if chr in freqDict:
                freqDict[chr].append(idx)

        # print(freqDict)
        # There must be some numbers in the str
        containsNums = False

        for chr in s:
            if chr in set({ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}):
                containsNums = True

        if not containsNums:
            return False


        # Tests for .
        if len(freqDict["."]) > 1:
            return False

        elif len(freqDict["."]) == 1 and len(s) == 1:
            return False


        # Tests for +/-
        if (len(freqDict["+"]) + len(freqDict["-"])) > 2:
            return False

        if len(s) == 1 and s == "+" or s == "-":
            return False

        for idx in freqDict["+"]+freqDict["-"]:
            if idx == 0 or s[idx-1] in set({"e", "E"}):
                continue
            else:
                return False

        # Tests for e/E
        if (len(freqDict["e"]) + len(freqDict["E"])) > 1:
            return False

        eIdx = None

        if len(freqDict["e"]) > 0:
            eIdx = freqDict["e"][0]

        if len(freqDict["E"]) > 0:
            eIdx = freqDict["E"][0]

        if eIdx != None:
            # Check left
            if eIdx == 0:
                return False

            if s[eIdx-1] == "." and eIdx-1 == 0:
                return False

            if s[eIdx-1]  not in set({".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}):
                return False

            if s[eIdx+1:] in ["","-","+"]:
                return False

            # Check right
            for idx in range(eIdx+1, len(s)):
                if idx == eIdx+1 and s[idx] in set({"+", "-"}):
                    continue

                elif s[idx] not in set({ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}):
                    return False

        return True


tests = [
    ("46.e3", True),

    ("+.", False),


# Decimal
    (".", False),
    (".5", True),
    ("5.0", True),
    ("5.", True),
    ("5.", True),
# Sign
    ("+5", True),
    ("-5", True),
    ("5+", False),
    ("5-", False),

    ("0e", False),

    ("abc+e-040", False),
    ("+e-040", False),
    ("+23e-04.0", False),
    ("+2.3e-", False),
    ("+", False),
    ("-", False),
    ("e", False),
    ("E", False),
    ("+2.3e-040", True),
    ("a234", False),
    ("+23-4", False),
    ("+2.3e-4", True),
    ("+2.3e-4+", False),
]

for s, want in tests:
    got = Solution().isNumber(s)
    if got != want:
        print("'{}' want {} got {}".format(s, want, got))
