class Solution:
    def decodeString(self, s):
        idx, num, stack = 0, 0, [""]
        n = len(s)

        while idx < n:
            if s[idx].isdigit():
                # Update digit
                num = num*10 + int(s[idx])
            elif s[idx] == "[":
                # Have finished creating digit
                # add digit, reset num, add current str val
                stack.append(num)
                num = 0
                stack.append("")
            elif s[idx] == "]":
                # Have finished solving this subproblem
                subProblem = stack.pop()
                mult = stack.pop()
                parentProblem = stack.pop()
                stack.append(parentProblem + mult * subProblem)
            else:
                # chr, build on to whatever chr we have been creating
                stack[-1] += s[idx]

            idx += 1

        return "".join(stack)







print(Solution().decodeString("2[2[y]pq]"))
print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("10[10[b]]"))
print(Solution().decodeString("5[a]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
print(Solution().decodeString("accaccacc"))
print(Solution().decodeString("3[a]2[bc]"))
