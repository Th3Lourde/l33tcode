class Solution:
    def simplifyPath(self, path):
        # print(path)
        # path = path.replace("//","/")
        # print(path)
        #
        # path_arr = path.split("/")
        path_arr = []

        current_element = ""

        for idx in range(len(path)):
            if path[idx] != "/":
                current_element += path[idx]
            else:
                if len(current_element) == 0:
                    continue
                else:
                    # current_element += path[idx]
                    path_arr.append(current_element)
                    current_element = ""

        if len(current_element) > 0:
            path_arr.append(current_element)


        # print(path_arr)
        # return

        i = 0

        while i < len(path_arr):
            if path_arr[i] == "..":
                del path_arr[i]

                if i > 0:
                    del path_arr[i-1]
                    i -= 1

                i -= 1

            elif path_arr[i] == ".":
                del path_arr[i]
                i -= 1

            i += 1

        # print(path_arr)

        resp = ""

        for path in path_arr:
            if len(path) > 0:
                resp += "/" + path

        if len(resp) == 0:
            return "/"

        if len(resp) == 1:
            return resp

        if resp[0] != "/":
            resp = "/" + resp

        if resp[-1] == "/":
            return resp[1:len(resp)-1]

        return resp

print(Solution().simplifyPath("/a//b////c/d//././/.."))
print(Solution().simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"))
