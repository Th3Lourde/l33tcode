'''
Given a list of directory info
path, files in the directory,
find out all groups of duplicate files
in the file system in terms of their paths

Return a list of lists of strings.

Each list contains strings. Each strings is
a path that leads to a file with the same content.

[ [d,d,f,f,]]
[0] represents paths that lead to a file that has
the same content. How could we do this?

The input:
List of strings. First part of the string represents
the path, the rest represent the file names and their content.

We want to create a dict ∋ we can query by file content
and get the list of paths that lead to a file with that content.

for each str, split by " "

the first index if the base path
get the index of '(', z

add the file name to the base path and use it as a key for
our dict. the contents of the file

the contents of the file is the key. The path is the value.

If the key already has a value, add it to the set.

Then loop through all elements in the set and append the values
to our answer

["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

["root/a, 1.txt(abcd), 2.txt(efgh)"]

map = {}

map = {"abcd": ["root/a/1.txt", "root/c/3.txt"], "efgh": ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]}
set = {"abcd", "efgh"}

map = {}
duplicates = set()

for path in paths:
    path = path.split(" ")
    basePath = path[0]

    for i in range(1, len(path)):

        openParen = path[i].index("(")
        file = path[i][:openParen]
        contents = path[i][openParen+1:-1]

        fullPath = path + "/" + file

            # Update set
        if contents in map:
            map[contents].append(fullPath)

            if contents not in duplicates:
                duplicates.add(contents)

            # Update map
        elif contents not in map:
            map[contents] = [fullPath]

ans = []

for duplicate in duplicates:
    ans.append(mapping[duplicate])

return ans

Memory complexity: linear + duplicated file contents
Time   complexity: number of paths * how long each path is/file is.

Ok so that solution kicked ass.



'''

class Solution:
    def findDuplicates(self, paths):
        mapping = {}
        duplicates = set()

        for path in paths:
            path = path.split(" ")
            basePath = path[0]

            for i in range(1, len(path)):

                openParen = path[i].index("(")
                file = path[i][0:openParen]
                # print(file)
                contents = path[i][openParen+1:-1]

                fullPath = basePath + "/" + file

                    # Update set
                if contents in mapping:
                    mapping[contents].append(fullPath)

                    if contents not in duplicates:
                        duplicates.add(contents)

                    # Update map
                elif contents not in mapping:
                    mapping[contents] = [fullPath]

        ans = []

        for duplicate in duplicates:
            ans.append(mapping[duplicate])

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.findDuplicates(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
