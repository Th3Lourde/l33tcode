

class Solution:

    def buddyStrings(self, A:str, B:str) -> bool:

        if len(A) != len(B):
            return False

        if A == B:
            # Look for repeated character in A,
            d = {}

            for i in range(len(A)):
                try:
                    d[A[i]] += 1
                    return True

                except:
                    d[A[i]] = 1

            return False


        have_swapped = False
        index = -1

        for i in range(len(A)):
            if A[i] != B[i] and have_swapped:
                # print("hi")
                if i == index:
                    have_swapped = True
                else:
                    return False

            elif A[i] != B[i]:
                # print("hi")
                # Look for B[i] in A
                for j in range(i,len(A)):
                    if A[j] == B[i] and B[j] == A[i]:
                        index = j
                        have_swapped = True
                        break

                if index == -1:
                    return False

                have_swapped = True

        return True


    def buddyStrings_1(self, A:str, B:str) -> bool:

        if len(A) != len(B):
            return False

        have_swapped = False
        i = 0

        while i < len(A):
            if A[i] != B[i] and have_swapped:
                return False

            elif A[i] != B[i]:

                if i == len(A)-1:
                    return False

                elif A[i+1] == B[i] and B[i+1] == A[i]:
                    i += 2
                    have_swapped = True

            elif A[i] == B[i]:
                i += 1

        return True

        # if A[-1] != B[-1]:
        #     return False
        #
        # elif A[-1] == B[-1]:
        #     return True

if __name__ == '__main__':
    s = Solution()
    # A = "  "
    # B = "ab"

    A = "abc"
    B = "acd"

    print(s.buddyStrings(A,B))
