


class Solution:
    def validPalindrome(self, s):
        can_remove = True
        index_stop = None
        i = 0
        j = len(s)-1


        while (i != j and i < j) and (j > 0 and i < len(s)-1):

            # print("i: {} j: {}".format(i, j))


            if s[i] == s[j]:
                i += 1
                j -= 1

            elif s[i] != s[j]:
                if can_remove:
                    r = self.validHelper(s[i:j+1])
                    # print(r)

                    if not(r):
                        if s[j-1] == s[i]:
                            # print("hi")
                            j -= 1
                            can_remove = False

                        else:
                            return False

                    if r:
                        return True

                elif not(can_remove):
                    return False

        return True


    def validHelper(self, s):
        v_can_remove = True
        v_i = 0
        v_j = len(s)-1


        while (v_i != v_j and v_i < v_j) and (v_j > 0 and v_i < len(s)-1):

            # print("i: {} j: {}".format(i, j))


            if s[v_i] == s[v_j]:
                v_i += 1
                v_j -= 1

            elif s[v_i] != s[v_j]:
                if v_can_remove:
                    if s[v_i+1] == s[v_j]:
                        v_i += 1
                        v_can_remove = False

                    else:
                        return False

                elif not(v_can_remove):
                    return False

        return True



if __name__ == '__main__':
    s = Solution()

    # text = "abc"

    # text = "bddb"

    # text = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

    # text = "ebcbbececabbacecbbcbe"

    text = "deeee"

    print(s.validPalindrome(text))
