class Solution:
    def isMatch(self, text, pattern):
        stack = [(0,0)]

        while stack != []:
            i, j = stack.pop()

            while j < len(pattern):
                # Handle for when we are out of string, (text)
                if pattern[j] == ".":
                    if j < len(pattern)-1 and pattern[j+1] == "*":
                        # Look for next chr in pattern
                        # If there is no chr: return True
                        target = ""
                        targetIdx = 0
                        for jCpy in range(j+2, len(pattern)):
                            if pattern[jCpy] != "*" and pattern[jCpy] != ".":
                                # Found target
                                target = pattern[jCpy]
                                targetIdx = jCpy

                        # print("Target: {} targetIdx: {}".format(target, targetIdx))

                        if target == "": return True

                        # Loop through text, everytime we see target,
                        # append to stack

                        for iCpy in range(i, len(text)):
                            if text[iCpy] == target:
                                stack.append((iCpy, targetIdx))

                        # print(stack)
                        break

                    else:
                        j += 1
                        i += 1

                elif pattern[j] != ".":
                    if j < len(pattern)-1 and pattern[j+1] == "*":
                        while i < len(text) and text[i] == pattern[j]:
                            i += 1
                            j += 2

                    else:
                        if pattern[j] == text[i]:
                            j += 1
                            i += 1
                        else:
                            break

            if i >= len(text) and j >= len(pattern): return True

        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aab","c*a*b"))
