'''
Given a string `path`
which is an absolute path starting with a slash

Convert it to the simplified canonical path.

A canonical has the following format:

The path starts with a single `/`
Any two directories are separated by a single slash `/`
The path does not end with a trailing `/`
The path only contains the directories on the path from the root
    dir to the target file or directory (no period )

So if you go into a directory, and then you go out of it, don't include it

/a/../b --> /b

1) Everywhere you see a // --> /
2) Everywhere you see a /./ --> "" (remove it)

Use a stack to keep track of the folders that we are in
Every time we see a /../, pop from stack. If stack is empty
do nothing

Then we are done, put the dir back together
'''

class Solution:
    def simplifyPath(self, path):
        path = path.replace("/./", "/")
        path = path.replace("//", "/")
        path = path[1:]

        movements = path.split("/")
        print(movements)
        stack = []

        for idx in range(len(movements)):
            if movements[idx] == '' or movements[idx] == ".":
                continue
            elif movements[idx] == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(movements[idx])

        resp = ""

        print(stack)

        for idx in range(len(stack)):
            resp += "/" + stack[idx]

        if resp == "":
            return "/"

        return resp

print(Solution().simplifyPath("/a//b////c/d//././/.."))



print(Solution().simplifyPath("/home/./..//bar"))
print(Solution().simplifyPath("/a/./b/../../c/"))
print(Solution().simplifyPath("/a/./b/../../c/.."))
print(Solution().simplifyPath("/home/"))
print(Solution().simplifyPath("/../"))
print(Solution().simplifyPath("/home//foo/"))
